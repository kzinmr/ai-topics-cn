---
source_url: https://dflash.z-lab.ai/
ingested: 2026-04-26
sha256: placeholder
---

# DFlash: Block Diffusion for Flash Speculative Decoding

Paper: https://arxiv.org/abs/2602.06036
Blog: https://dflash.z-lab.ai/
GitHub: https://github.com/z-lab/dflash

Authors: Jian Chen, Yesheng Liang, Zhijian Liu (Z-Lab)

## Overview

**DFlash** is a lightweight **block diffusion** model designed for speculative decoding. It enables efficient and high-quality parallel drafting.

DFlash uses a lightweight block diffusion model to draft an entire block of tokens in a single parallel forward pass, achieving up to **6× lossless acceleration** on Qwen3-8B, nearly 2.5× faster than EAGLE-3.

## Speculative Decoding — The Bottleneck

Speculative decoding works by having a small draft model propose tokens that the large target LLM verifies in parallel. The bottleneck is the drafter: EAGLE-3, the current state of the art, drafts autoregressively, so it's still sequential and caps out around 2-3× speedup.

Diffusion models can generate tokens in parallel, but using them as drafters isn't straightforward. Methods like DiffuSpec and SpecDiff-2 use massive 7B-parameter drafters that are too expensive for real-world serving.

## Key Insight: The Target Knows Best

Large autoregressive LLMs' hidden features implicitly contain information about multiple future tokens (observed by Samragh et al., 2025). DFlash utilizes these hidden features as context, conditioning the draft model to predict future blocks of tokens in parallel. The draft model becomes a **diffusion adapter** that efficiently leverages the deep context features modeled by the large target model.

## How DFlash Works

### 1. Feature Fusion
After prefill or verification, hidden features from layers uniformly sampled across the target model are extracted and fused through a lightweight projection into a compact target context feature.

### 2. KV Injection (Core Innovation)
The fused features are injected directly into the Key/Value projections of every draft model layer and stored in the draft model's KV cache. This is a crucial difference from EAGLE-3, which feeds target features only as input to the first layer. In DFlash, every layer gets the full context, so acceptance length scales with depth.

### 3. Parallel Diffusion Drafting
Conditioned on this rich context (and the last verified token), the drafter predicts the next block of tokens in a single forward pass using block diffusion. All masked positions within a block are decoded in parallel.

### Architecture Design
- The draft model reuses the embedding and LM head from the target model
- Only the intermediate layers are trained, keeping parameter count minimal
- Block construction: anchor tokens randomly sampled from response, remaining positions masked for parallel prediction

## Performance Results

| Metric | Result |
|--------|--------|
| Qwen3-8B Speedup | Up to 6× (lossless) |
| vs EAGLE-3 | Nearly 2.5× faster |
| Block Size | 16 tokens (single denoising step) |
| Drafting Latency | Lower than 1-layer EAGLE-3 generating 8 tokens |

## Supported Models (HuggingFace)

- Qwen3.5-122B-A10B → z-lab/Qwen3.5-122B-A10B-DFlash
- Qwen3.5-35B-A3B → z-lab/Qwen3.5-35B-A3B-DFlash
- Qwen3.5-27B → z-lab/Qwen3.5-27B-DFlash
- Qwen3.5-9B → z-lab/Qwen3.5-9B-DFlash
- Qwen3.5-4B → z-lab/Qwen3.5-4B-DFlash
- Qwen3-Coder-30B-A3B → z-lab/Qwen3-Coder-30B-A3B-DFlash
- Qwen3-8B → z-lab/Qwen3-8B-DFlash-b16
- Qwen3-4B → z-lab/Qwen3-4B-DFlash-b16
- LLaMA-3.1-8B-Instruct → z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat
- Kimi-K2.5 → z-lab/Kimi-K2.5-DFlash
- gpt-oss-20b → z-lab/gpt-oss-20b-DFlash
- gpt-oss-120b → z-lab/gpt-oss-120b-DFlash

## Inference Backends

- **vLLM** — via speculative-config
- **SGLang** — via --speculative-algorithm DFLASH
- **Transformers** — via spec_generate() method (Qwen3 and LLaMA-3.1 only)
- **MLX** — Apple Silicon support

## Significance

DFlash reframes the role of diffusion LLMs entirely. Instead of training massive diffusion models to match autoregressive quality, lightweight diffusion adapters optimized for fast, accurate block prediction achieve both high acceptance rates and low drafting latency, pushing speculative decoding to over 6× lossless speedup.
