# hot-topics.yaml: 既知のYAML破損パターンと修復方法

このファイルは `active-crawl-workflow` 実行中に `hot-topics.yaml` でよく遭遇するYAML破損パターンとその修復手順を記録する。

## パターン1: 重複キー (Duplicate YAML Keys)

**症状**: `hot-topics.yaml` の同一トピックブロック内に同じキーが2つ出現する。例:

```yaml
  - slug: yi
    search_hints: [古い値1, 古い値2]     # ← 1つ目 (孤立/古い)
    wiki_pages:
      - concepts/yi
    notes: "..."
    added: 2026-04-17
    last_crawled: 2026-05-16
    search_hints: [新しい値1, 新しい値2, 追加値]  # ← 2つ目 (有効)
    wiki_pages:                                  # ← 重複
      - concepts/yi
```

**原因**: 過去の subagent または人間の編集者が `search_hints:` の更新時に既存キーを上書きせず、新しいブロックを追加した。PyYAML は同じキーの出現を黙って後勝ちで採用するため、先にある古い方の `search_hints:` は無視される。しかし人間の目には読めないため、後に手動編集すると混乱を招く。

**修復手順**:
1. `read_file` で該当トピックブロック全体を正確に読み込む（offset 指定が必要な場合あり）
2. どのキーが重複しているか特定する（`search_hints:`, `wiki_pages:`, `notes:` のいずれか）
3. **古い方（無視される方）のブロックを削除する**:
   - `patch()` で削除部分を `old_string` に指定
   - 旧キー行 + その値行（配列の場合1行以上）をまるごと削除
   - **注意**: 行末の改行やインデントも一致させる必要がある

**例**: yi トピックの重複 `search_hints:` + `wiki_pages:` 削除:

```
old_string: "    search_hints: [原有值1, 原有值2]\n    wiki_pages:\n      - concepts/yi\n"
new_string: ""  # 空文字で削除
```

**検証**: 修復後、再度 `read_file` で該当ブロックを確認。重複キーがなくなり、`slug` 直下にただ一つの `search_hints:` だけがあることを確認する。

## パターン2: 日付の引用符の不一致 (Mixed Date Quoting)

**症状**: トピックによって `last_crawled: 2026-05-26`（裸）と `last_crawled: "2026-05-15"`（引用符付き）が混在する。

**問題点**:
- `patch` で `last_crawled` を変更する際、引用符の有無が異なると2つの異なる文字列として扱われる
- 「同じ `last_crawled` 値を持つ複数トピック」問題が悪化する（裸と引用符付きでさらにバリエーションが増える）

**修復**: 可能であれば統一する。書き込み時に既存の書式に合わせるのが安全。全トピックを裸に統一したい場合は `write_file` で全ファイルを書き換える。

## パターン3: 孤立した空行・コメントの残骸 (Orphaned Lines)

**症状**: 重複キー削除後に不自然な空行やインデントのずれが残る。例:

```yaml
  - slug: yi

    search_hints: [値1, 値2]
```

**修復**: 空行を削除する場合は `patch` で `"\n\n    search_hints"` → `"\n    search_hints"` のように置換。ただし空行はYAMLの可読性に役立つ場合もあるので、過度に詰めない。

## 検証スクリプト

実行可能スクリプト: `scripts/validate-hot-topics-yaml.py`

```bash
python scripts/validate-hot-topics-yaml.py ~/ai-topics-cn/config/hot-topics.yaml
```

`hot-topics.yaml` の構造的健全性をチェックするスクリプト（以下は埋め込み参照用）:

```python
import yaml, sys

with open(sys.argv[1]) as f:
    data = yaml.safe_load(f)

errors = []
for i, topic in enumerate(data.get('topics', [])):
    slug = topic.get('slug', f'index-{i}')
    # 必須キーの存在確認
    for key in ['crawl_policy', 'priority', 'search_hints', 'wiki_pages', 'notes', 'added']:
        if key not in topic:
            errors.append(f"[{slug}] 不足キー: {key}")

if errors:
    for e in errors:
        print(f"ERROR: {e}")
    sys.exit(1)
else:
    print(f"OK: {len(data.get('topics', []))} topics, no structural issues")
```
