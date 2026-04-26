---
source_url: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
ingested: 2026-04-26
sha256: placeholder
---

# TurboQuant: Redefining AI efficiency with extreme compression

March 24, 2026

Amir Zandieh, Research Scientist, and Vahab Mirrokni, VP and Google Fellow, Google Research

We introduce a set of advanced theoretically grounded quantization algorithms that enable massive compression for large language models and vector search engines.

Vectors are the fundamental way AI models understand and process information. Small vectors describe simple attributes, such as a point in a graph, while "high-dimensional" vectors capture complex information such as the features of an image, the meaning of a word, or the properties of a dataset. High-dimensional vectors are incredibly powerful, but they also consume vast amounts of memory, leading to bottlenecks in the key-value cache, a high-speed "digital cheat sheet" that stores frequently used information under simple labels so a computer can retrieve it instantly without having to search through a slow, massive database.

Vector quantization is a powerful, classical data compression technique that reduces the size of high-dimensional vectors. This optimization addresses two critical facets of AI: it enhances vector search, the high-speed technology powering large-scale AI and search engines, by enabling faster similarity lookups; and it helps unclog key-value cache bottlenecks by reducing the size of key-value pairs, which enables faster similarity searches and lowers memory costs. However, traditional vector quantization usually introduces its own "memory overhead" as most methods require calculating and storing (in full precision) quantization constants for every small block of data. This overhead can add 1 or 2 extra bits per number, partially defeating the purpose of vector quantization.

Today, we introduce TurboQuant (to be presented at ICLR 2026), a compression algorithm that optimally addresses the challenge of memory overhead in vector quantization. We also present Quantized Johnson-Lindenstrauss (QJL), and PolarQuant (to be presented at AISTATS 2026), which TurboQuant uses to achieve its results. In testing, all three techniques showed great promise for reducing key-value bottlenecks without sacrificing AI model performance. This has potentially profound implications for all compression-reliant use cases, including and especially in the domains of search and AI.

## How TurboQuant Works

TurboQuant is a compression method that achieves a high reduction in model size with zero accuracy loss, making it ideal for supporting both key-value (KV) cache compression and vector search. It accomplishes this via two key steps:

1. **High-quality compression (the PolarQuant method)**: TurboQuant starts by randomly rotating the data vectors. This clever step simplifies the data's geometry, making it easy to apply a standard, high-quality quantizer to each part of the vector individually. This first stage uses most of the compression power (the majority of the bits) to capture the main concept and strength of the original vector.

2. **Eliminating hidden errors**: TurboQuant uses a small, residual amount of compression power (just 1 bit) to apply the QJL algorithm to the tiny amount of error left over from the first stage. The QJL stage acts as a mathematical error-checker that eliminates bias, leading to a more accurate attention score.

## QJL: The Zero-Overhead, 1-Bit Trick

QJL uses a mathematical technique called the Johnson-Lindenstrauss Transform to shrink complex, high-dimensional data while preserving the essential distances and relationships between data points. It reduces each resulting vector number to a single sign bit (+1 or -1). This algorithm essentially creates a high-speed shorthand that requires zero memory overhead. To maintain accuracy, QJL uses a special estimator that strategically balances a high-precision query with the low-precision, simplified data. This allows the model to accurately calculate the attention score (the process used to decide which parts of its input are important and which parts can be safely ignored).

## PolarQuant: A New "Angle" on Compression

PolarQuant addresses the memory overhead problem using a completely different approach. Instead of looking at a memory vector using standard coordinates (i.e., X, Y, Z) that indicate the distance along each axis, PolarQuant converts the vector into polar coordinates. This results in two pieces of information: the radius, which signifies how strong the core data is, and the angle indicating the data's direction or meaning. Because the pattern of the angles is known and highly concentrated, the model no longer needs to perform the expensive data normalization step because it maps data onto a fixed, predictable "circular" grid where the boundaries are already known, rather than a "square" grid where the boundaries change constantly. This allows PolarQuant to eliminate the memory overhead that traditional methods must carry.

## Performance Results

- TurboQuant achieves **6× memory reduction** in AI workloads
- Near-lossless quality at 3-bit precision
- Applied to both KV cache compression and vector search simultaneously
- Presented at ICLR 2026 (PolarQuant) and AISTATS 2026 (QJL)
