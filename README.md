# dedup-lab

![CI](https://github.com/liuy0421/dedup-lab/actions/workflows/ci.yml/badge.svg)

Detecting near-duplicates and benchmark contamination in LLM training data, and
measuring how removing them changes fine-tuned model evaluations.

**Status:** work in progress.

## Planned
- [x] Unicode-aware text normalization for dedup keys
- [ ] Exact dedup + MinHash/LSH near-duplicate detection (implemented from scratch)
- [ ] Benchmark contamination scan (GSM8K, MMLU) of FineWeb and public SFT datasets
- [ ] Scaled pipeline with Apache Beam
- [ ] LoRA fine-tuning ablation: raw vs. deduplicated SFT data
- [ ] Evaluation with bootstrap confidence intervals

## Development
    uv sync
    uv run pytest