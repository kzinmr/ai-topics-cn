# WeChat Media Spam Pattern

## 識別方法
WeChatメディア記事は毎日のクロールで同一内容が再配信される。ファイル名の末尾ハッシュ（`-8df67f31.md`等）が同一なら重複。

## 典型的なスパムパターン（13-14テンプレートの日次再利用）
以下のタイトルパターンは技術的議論を含まず、毎日記事に出現する場合はspam判定：

- `AI Agent工作流程技术栈与能力基础` → hash `aed7e3c9`
- `LLM泡沫下的AI Agent伪生存` → hash `f691ec7c`
- `Meta前ChatGPT核心成员的技术...` → hash `fdcb9807`
- `一文读透AI四大核心技术LLM+Agent+RAG+Skill` → hash `85240507`
- `个人与大模型LLM自研是大势AI agent抓手` → hash `412878cd`
- `人工智能大数据云计算物联网AI技术碰撞...` → hash `e953f914`
- `从LLM到Agent一张图理清AI核心概念` → hash `88d37227`
- `剖析AI Agent作为核心技术的能力体` → hash `5c8aef97`
- `多日NLP回顾80页大模型Agent综述` → hash `357bad68`
- `大模型前指AIAgents语音交互...SpokenWOZ` → hash `159c78b4`
- `建立端平检测并释疑LiteLLM...` → hash `5be22590`
- `机构AI00单一模态OpenAI...Embodied-Intelligence` → hash `aafeba3f`
- `网传...AI领域最新最全概念图谱...` → hash `d45b3961`
- `让AI文献你的阅读习惯...RSS个人化` → hash `ba001135`
- `AI新热点-瞄准Agent湿漉...` → hash `10937405`

## 処理方法
```bash
# hashが上記のいずれかに一致 → archive/spam/
# 例: find inbox/wechat-media/ -name "*-aed7e3c9.md" -exec mv {} archive/spam/ \;
# 日付が変わっても同一hashのファイルが出現するため、日次クリーンアップ推奨
```

## 例外
- 上記パターンだが1500文字以上の独自技術議論を含む場合は保持
- 新規hashのWeChat記事は個別に品質評価
