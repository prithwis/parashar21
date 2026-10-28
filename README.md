![Parashar21 Banner](/images/p21-header-003.png)

# Parashar21 & Khona21

### Two Engines. One Jyotisha Platform.

**Parashar21** and **Khona21** together form an integrated platform for computational and interpretive Hindu Jyotisha (Vedic Astrology). Developed over approximately two decades, the project combines deterministic astronomical calculations with source-grounded reasoning using modern Large Language Models (LLMs).

The two components have distinct but complementary responsibilities:

**Parashar21 computes. Khona21 interprets.**

The project has reached its intended functional maturity with **Version 5.1 (October 2026)**. Active development is complete, and the platform is now available for regular consultation and use.

## Parashar21 — The Computational Engine

Parashar21 is a deterministic Jyotisha engine built around the **Swiss Ephemeris**. Given the place, date and time of birth, it calculates planetary positions, houses, lordships, aspects, conjunctions, Vimshottari Dasha schedules and other classical astrological parameters, following the principles associated with Maharishi Parashara.

Its final implementation produces four structured, LLM-ready text outputs:

- **Rashi:** The natal horoscope, including planetary placements, house relationships and other relevant configurations.
- **Navamsha:** The divisional chart used to supplement natal interpretation.
- **Dasha:** The Vimshottari Dasha schedule, providing the temporal framework for interpretation.
- **Gochar:** Planetary transits, calculated with reference to the natal Moon sign, for assessing current and future periods.

These outputs provide a structured semantic representation of the horoscope, separating the calculation of astrological facts from their subsequent interpretation.

The final computational notebook is **`P21_51_Kast2LLM`**.

## Khona21 — The Interpretive Engine

Named after the legendary Bengali astrologer Khona, **Khona21** is an AI-assisted Jyotisha interpretation platform developed as the companion to Parashar21.

Rather than relying on an extensive collection of hard-coded interpretive rules, Khona21 uses LLMs to examine the calculated horoscope against a curated corpus of classical and contemporary Jyotisha literature, currently comprising works by **James Braha** and **Harihar Majumdar**.

Its source-grounded, multipass reasoning workflow examines planetary configurations, yogas, sign exchanges, cancellations, exceptions and conflicting interpretations.

The process has two principal stages:

1. **Initial Assessment:** A broad examination of the natal horoscope establishes its principal characteristics and important astrological configurations.
2. **Question-Specific Consultation:** The initial assessment is combined with the original reference texts, horoscope data and Dasha schedules to investigate specific questions. Gochar can optionally be included when transit considerations are relevant.

The objective is to produce interpretations that are systematic, transparent and traceable to the underlying astrological sources.

The final consultation notebook is **`K21_51_KhonaPlus`**.

## Architecture — The Parashar–Khona Jugalbandi

The architecture separates two fundamentally different activities: deterministic computation and interpretive reasoning.

Parashar21 supplies consistent, reproducible astronomical and astrological data. Khona21 applies the contextual reasoning capabilities of LLMs to interpret that data using the reference corpus.

This separation allows the computational foundation to remain stable while individual consultations explore different questions, interpretive perspectives and time periods.

![Parashar21 Architecture](/images/p21-Arch-2026.png)

For the system architecture, design rationale and processing pipeline, see [ARCHITECTURE.md](https://github.com/prithwis/parashar21/blob/main/Docs/ARCHITECTURE.md).

The documentation of the original Parashar21 implementation has been preserved as [Original README.md](https://github.com/prithwis/parashar21/blob/main/Docs/README-00.md).

## Getting Started

The platform consists of two Google Colab notebooks, both at **Version 5.1**.

**Step 1 — Parashar21**

Run `P21_51_Kast2LLM` to generate the Rashi, Navamsha, Dasha and Gochar data files. The Rashi and Navamsha calculations require separate runs.

**Step 2 — Khona21**

Run `K21_51_KhonaPlus`, supplying the required horoscope files. The notebook uses its reference corpus and multipass LLM workflow to generate an initial assessment and answer specific questions. Gochar may be included or excluded depending on the consultation.

For further guidance on chart generation and LLM-based interpretation, see the [Parashar21-LLM User Manual](https://github.com/prithwis/parashar21/blob/main/Docs/UserManual.md).

## Development Status — Complete

**Final Version: 5.1 | October 2026**

Parashar21 began as an effort to automate the mathematical and astronomical foundations of traditional Jyotisha. Over the years, it evolved into a comprehensive computational engine, but the challenge of interpreting the resulting horoscopes remained.

The emergence of capable Large Language Models provided the missing interpretive component, leading to the development of Khona21.

With the integration of the two systems, the original objective has been achieved: a working platform that can calculate a horoscope and produce source-grounded interpretations in response to individual questions.

**Active development of Parashar21 and Khona21 has therefore concluded.**

The repository will remain available as working software, technical documentation and a record of the project's evolution over approximately twenty years.

The emphasis now shifts from building the system to using it.

---

**Parashar21 computes. Khona21 interprets.**

*The Jugalbandi is complete.*

![Parashar21 Banner](/images/khona21-v0.png)
