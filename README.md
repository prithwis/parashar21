![parashar21 banner](/images/p21-header-003.png)<br>

# Parashar21

Parashar21 is a deterministic Hindu Jyotisha (Vedic Astrology) engine built around the Swiss Ephemeris. Given the place, date, and time of birth, it computes planetary positions, houses, lords, aspects, conjunctions, dashas, and other classical astrological parameters based on the principles of Maharishi Parashara.

The current generation of Parashar21 extends beyond chart computation by producing a **structured semantic description** of the horoscope. This machine-readable representation forms the bridge between deterministic astrological computation and modern Large Language Models (LLMs), enabling comprehensive, context-aware interpretations grounded in classical Jyotisha literature.

The guiding philosophy is simple:

> **Parashar21 performs the mathematics. The LLM performs the interpretation.**

This hybrid neuro-symbolic architecture preserves the precision and repeatability of classical astrological computation while leveraging the reasoning capabilities of contemporary AI systems.

The overall architecture of the project is illustrated below.

![Parashar21 Architecture](/images/p21-Arch-2026.png)<br>

For a detailed description of the system architecture, design rationale, and processing pipeline, see **[Architecture.md](https://github.com/prithwis/parashar21/blob/main/Docs/ARCHITECTURE.md)**.

The historical documentation describing the original Parashar21 implementation has been retained as **[Original README.md](https://github.com/prithwis/parashar21/blob/main/Docs/README-00.md)** for reference.


## Khona21 — AI-Assisted Jyotisha Interpretation

**Khona21** is an experimental interpretation platform that grew out of Parashar21. Named after the legendary Bengali astrologer Khona, it uses an LLM to examine precomputed horoscope data against a curated corpus of Jyotisha literature, currently including works by **James Braha** and **Harihar Majumdar**.

Rather than relying on a fixed set of interpretive rules encoded in software, Khona21 uses a source-grounded analytical workflow to identify planetary configurations, yogas, sign exchanges, cancellations, exceptions, and disagreements between authorities. It then synthesizes the relevant findings into answers to specific questions about a horoscope.

**Current status:** The initial Khona21 implementation and consultation workflow are complete and available for experimentation. The final consultation notebook is **`K21_KonsultKhona`**. Further work will focus on expanding and refining the reference corpus rather than adding complexity to the interpretation pipeline.

Khona21 explores the application of AI to traditional knowledge systems; it does not constitute scientific validation of astrological predictions.

## Getting Started

For step-by-step instructions on generating the Rashi and Navamsha charts and using the output with Google NotebookLM, see the **[Parashar21-LLM User Manual](https://github.com/prithwis/parashar21/blob/main/Docs/UserManual.md)**.

For source-grounded, question-based interpretation using Khona21, use the **`K21_KonsultKhona`** notebook with the required horoscope data and reference corpus. 
