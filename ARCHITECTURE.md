# Parashar21 Architecture

## Introduction

Parashar21 is a Python framework for constructing, analysing and reporting horoscope charts based on the principles of classical Hindu astrology (Jyotisha).

The project has evolved over more than ten years and therefore reflects both its original design goals and its subsequent evolution.

Originally, Parashar21 was conceived as a platform for building a searchable repository containing thousands of horoscope charts. Charts were represented as JSON documents and stored in MongoDB so that complex astrological patterns could be searched efficiently.

More recently, the emphasis has shifted towards using Large Language Models (LLMs) as reasoning engines over structured horoscope data. As a result, MongoDB is no longer central to the project, although several components of the original architecture have been retained because they are stable, well-tested and continue to provide a clean processing pipeline.

---

# Overall Processing Pipeline

```
Birth Data (CSV)
        │
        ▼
Swiss Ephemeris
(C61_Cast2JSON)
        │
        ▼
JSON Horoscope
        │
        ▼
chart
(single-row Pandas DataFrame)
        │
        ├────────► Vimshottari Dasha
        │
        ▼
Report Generation
        │
        ├────────► MS Word Report
        ├────────► LLM Chart Input
        └────────► LLM Dasha Input
```

---

# Processing Stages

## Stage 1 – Birth Data

Birth details are read from a CSV file containing:

- Date of Birth
- Time of Birth
- Place of Birth

This is the only external data required for horoscope generation.

---

## Stage 2 – Horoscope Construction

The function

```python
p21swe.C61_Cast2JSON()
```

uses the Swiss Ephemeris library to compute planetary positions and construct the horoscope.

During this stage the horoscope is enriched with intrinsic astrological information, including:

- Graha positions
- Bhavas
- House Lords
- Graha Lordships
- Exaltation and Debilitation
- Own, Friendly and Enemy houses
- Functional Benefic and Malefic status
- Graha Aspects
- Bhava Aspects
- Planetary Conjunctions
- Lord Relationships

The completed horoscope is then serialized into JSON format.

---

## Stage 3 – Working Chart Object

The JSON horoscope is loaded into a single-row Pandas DataFrame called `chart`.

Although this JSON → Pandas conversion originally existed to support MongoDB storage and retrieval, the `chart` object has gradually become the canonical in-memory representation of a horoscope.

Almost every subsequent operation within Parashar21 uses this object.

---

## Stage 4 – Time-dependent Calculations

Some astrological calculations depend on the date of analysis rather than on the natal chart itself.

These include:

- Vimshottari Mahadasha
- Antardasha
- Gochar chart

These calculations are performed after the horoscope has been constructed.

---

## Stage 5 – Report Generation

The function

```python
genChart()
```

generates the final reports.

Current outputs include:

- Human-readable MS Word report
- Structured LLM Chart Input
- Structured LLM Dasha Input

This stage formats existing horoscope information rather than recalculating it.

---

# Additional Calculations

Some calculations were introduced after the original architecture had stabilised.

These include:

- Yoga Detection
- AshtakVarga

At present these are invoked during report generation.

Conceptually they belong to the horoscope itself rather than to the reporting layer, but they remain in their present location to preserve compatibility with the existing code base.

---

# Natal and Gochar

Parashar21 generates two closely related analytical charts.

## Natal

The standard horoscope constructed using the Lagna at birth.

## Gochar

A Moon-based analytical chart in which the natal Moon position is treated as the Lagna.

The Gochar chart is primarily intended for analysing current Mahadasha and Antardasha from the Moon.

---

# Human Reports and LLM Reports

Both human-readable reports and LLM reports are generated from the same underlying horoscope object.

The difference lies only in presentation.

The MS Word report is intended for astrologers.

The LLM reports provide structured textual representations designed to maximise reasoning by Large Language Models.

The LLM pipeline separates:

- Static horoscope information
- Time-dependent Dasha information

This separation has been found to improve the quality of LLM reasoning.

---

# Historical Evolution

Parashar21 has evolved through three distinct phases.

## Phase 1 – Horoscope Construction

Reliable generation of horoscope charts from birth data using Swiss Ephemeris.

## Phase 2 – Searchable Horoscope Repository

Representation of horoscope charts as structured JSON documents suitable for storage and retrieval using MongoDB.

## Phase 3 – LLM-assisted Reasoning

Generation of structured textual representations that enable Large Language Models to reason over horoscope data while keeping horoscope generation deterministic and transparent.

---

# Design Philosophy

Parashar21 deliberately separates **calculation** from **interpretation**.

The framework computes horoscope data deterministically using established astronomical algorithms together with explicit Jyotisha rules.

Interpretation is performed independently by either:

- a human astrologer, or
- a Large Language Model operating on structured textual representations of the horoscope.

This separation allows improvements in interpretative techniques without modifying the underlying horoscope generation engine.

---

# Current Status

Although Parashar21 originally emphasised large-scale storage and retrieval of horoscope charts using MongoDB, the current focus has shifted towards creating high-quality structured inputs for LLM-based reasoning.

The computational core of the project remains unchanged; only the interpretation layer has evolved. This preserves the transparency and reproducibility of horoscope generation while allowing modern AI systems to assist in chart interpretation.