# Two-Pass Structural Analysis and Audit Workflow

**Documentation note --- 27 September 2026**

## 1. Purpose

Parashar21 (P21) computes the horoscope; NotebookLM interprets it
against a deliberately limited Jyotisha corpus. The workflow described
here was developed to make that interpretation more systematic,
auditable, and resistant to conversational bias.

The key insight is that a single LLM reading is not enough. A useful
workflow separates four different functions:

1.  a **persistent governing instruction** that applies to every
    NotebookLM query;
2.  a **First Pass** that creates a broad structural map of the
    horoscope;
3.  a fresh-context **Audit** that treats the First Pass as an untrusted
    analytical document;
4.  a concise **Second Pass** that records verified corrections,
    qualifications, and omissions.

The resulting First Pass + Second Pass do **not** replace the original
P21 data or the Braha/Harihar corpus. They augment them as precomputed
structural aids.

The working source set therefore becomes:

``` text
P21 computational output
    ├── Chart / Rashi
    ├── Navamsha
    └── Vimshottari Dasha

Primary interpretive corpus
    ├── James Braha
    └── Harihar Majumdar

Precomputed analytical aids
    ├── First Pass
    └── Second Pass
```

For subsequent questions NotebookLM is free to use **all** of these
sources. Chart, Navamsha and Dasha remain primary computational
evidence; Braha and Harihar remain the source of interpretive rules;
First Pass and Second Pass provide an already examined structural map.

------------------------------------------------------------------------

## 2. Why a Persistent NotebookLM Instruction?

NotebookLM provides a configuration field for a custom instruction that
is applied before ordinary chat prompts. This is used as a lightweight
equivalent of a system-level governing instruction.

The objective is **not** to put the entire Jyotisha method into this
field. Experience with NotebookLM suggests that a light touch works
better than an elaborate meta-prompt.

The persistent instruction establishes only the epistemic discipline:

-   use the supplied notebook sources rather than importing outside
    Jyotisha rules;
-   distinguish computational facts from interpretive classifications;
-   treat questions as hypotheses rather than premises to confirm;
-   prefer specific rules over generic indications;
-   expose contradictions and uncertainty;
-   use First Pass and Second Pass as aids rather than substitutes for
    primary evidence.

### Persistent NotebookLM Instruction

``` text
You are a careful and experienced analyst of Hindu/Jyotisha astrology.

Base your analysis ONLY on the chart data and astrological sources provided in this notebook. Do not introduce astrological principles or interpretations from outside these sources.

Treat the computational Chart, Navamsha and Dasha data as primary evidence for astronomical, positional and temporal facts. Use the supplied astrological corpus for interpretive rules and classifications.

Where First Pass and Second Pass are provided, use them as precomputed structural aids, not as substitutes for the primary chart data or corpus. First Pass provides an initial structural analysis; Second Pass contains verified corrections, qualifications and additions. Where Second Pass corrects First Pass, Second Pass takes precedence. You may always return to the primary Chart, Navamsha, Dasha and corpus when answering a question.

Treat every question as something to investigate, not a premise to confirm. Look for relevant evidence both for and against a proposed interpretation.

Give greater weight to specific rules that directly match the chart than to broad or generic astrological indications. If sources or indications conflict, identify the conflict rather than forcing a conclusion.

Distinguish clearly between what the chart states, what the sources state, and what you infer by applying the sources to the chart.

Do not invent missing evidence. If the supplied sources do not support a reliable conclusion, say so.

Cite the relevant sources for your astrological conclusions.

Be concise, analytical and conservative. Your objective is a source-grounded interpretation, not a persuasive horoscope reading.
```

### Important distinction: computational fact vs interpretation

A useful lesson from testing was that P21-generated data should be
authoritative for facts such as longitude, sign, house, lordship, and
Dasha dates. But labels such as *functional benefic* or *functional
malefic* are already interpretations and may be modified by a more
specific Braha/Harihar rule.

In short:

``` text
Longitude / sign / house / lordship / Dasha dates  -> computational evidence
Functional status / strength / yoga interpretation -> corpus-governed interpretation
```

------------------------------------------------------------------------

## 3. First Pass: Building the Structural Map

The First Pass is an **intermediate analytical record**, not a biography
and not a prediction.

Its job is to force a systematic inventory before NotebookLM begins
telling a story about the native. An early version was too house-centric
and could miss planet-level conditions such as Vargottama. The revised
procedure therefore begins with every graha and every house lord, then
moves to houses, yogas/special conditions, and Navamsha.

### First Pass Prompt

``` text
Prepare a rigorous structural analysis of this horoscope using the chart data and corpus in this Notebook. This is an intermediate analytical record, NOT an interpretation of the native's life.

### 1. Grahas and Lords

Systematically examine every graha and every house lord.

For each, check its placement and condition, including where applicable:

- house and sign;
- houses owned;
- own, friendly, neutral or enemy sign;
- exaltation or debilitation, including relevant degree-sensitive conditions;
- conjunctions and aspects;
- benefic/malefic influence, affliction or protection;
- strength or weakness;
- lunar phase where relevant;
- Vargottama status and other relevant Natal–Navamsha relationships;
- special afflictions or doshas explicitly defined by the corpus;
- any other significant condition supported by the corpus.

Do not omit a graha or lord simply because no unusual condition is immediately apparent.

### 2. Houses

Examine all 12 houses for:

- sign and lord;
- condition of the lord;
- occupants and aspects;
- significant conjunctions or relationships;
- strengthening, weakening, affliction, protection or contradictory influences.

Give each house a brief structural assessment such as Strong / Weak / Mixed / Afflicted / Protected / Conflicted / Indeterminate, with supporting evidence.

### 3. Yogas and Special Conditions

Systematically search for significant yogas and special conditions supported by the corpus, including Raja, Dhana, Viparita Raja, Parivartana, important lordship/conjunction combinations, exaltation/debilitation and Neechabhanga / Neechabhanga Raja Yoga.

For each candidate, test the required conditions against the actual chart. Check for exceptions, cancellation, weakening, modification or contradictory evidence.

For every debilitated graha, explicitly check for Neechabhanga or other modification.

### 4. Navamsha

Use the Navamsha where supported by the corpus. Check especially for reinforcement, weakening, dignity changes and Vargottama. Clearly distinguish Natal and Navamsha facts.

### Discipline

Use CHART FACT -> CORPUS RULE -> CONCLUSION. Prefer specific rules over generic indications. Record contradictory evidence and specific exceptions rather than forcing a resolution.

The sole question is:

What astrological conditions and corpus-supported structures are present in this chart?

Do NOT interpret these findings in terms of the native's career, wealth, health, relationships, personality or life events.
```

### Why First Pass is deliberately not exhaustive

The aim is not to encode every Braha/Harihar rule into the prompt. Doing
that would recreate the corpus inside the prompt and encourage
prompt-following at the expense of source-reading.

First Pass is therefore expected to be imperfect. Its omissions are
handled by the next stage.

------------------------------------------------------------------------

## 4. Fresh-Context Audit: Make the Model Review Its Own Work as if Written by Someone Else

After generating First Pass, the NotebookLM chat history should be
cleared before the audit.

This is important. Asking the same conversational instance *"Did you
make any mistakes?"* encourages self-consistency and retrospective
justification. A fresh chat removes much of that conversational
commitment.

The First Pass is then supplied as a source and treated as an
**untrusted analytical document**.

The Audit checks:

-   chart facts;
-   geometry and aspects;
-   corpus-rule application;
-   unsupported conclusions;
-   exceptions and qualifications;
-   internal contradictions;
-   significant structural omissions.

Timing material is intentionally excluded from this audit. Dasha,
planetary maturity, and Nakshatra analysis can create a much larger
search space and are not necessary for auditing the static structural
record.

### Audit Prompt

``` text
Audit the First Pass Analysis against the primary chart data and the Braha and Harihar Majumdar corpus in this Notebook.

Treat the First Pass as an untrusted analytical document to be independently verified, not as an authoritative source.

Check systematically for:

- incorrect chart facts;
- corpus rules that have been misstated or incorrectly applied;
- conclusions not actually supported by the cited corpus;
- specific corpus rules, exceptions or qualifications that contradict or materially modify a First Pass conclusion;
- contradictions within the First Pass itself;
- significant structural conditions, strengths, weaknesses, dignities, afflictions, yogas, doshas or other corpus-supported features that the First Pass has missed.

For every problem found, state:

FIRST PASS CLAIM -> PRIMARY EVIDENCE -> AUDIT VERDICT

Distinguish genuine errors from reasonable differences of interpretation. Do not manufacture omissions merely to make the audit appear comprehensive.

### Scope

Audit only the static structural horoscope analysis.

Do NOT introduce Vimshottari Dasha or other timing analysis, planetary maturity ages, predictive periods, life events, or biographical interpretation.

Do NOT expand into Nakshatra analysis or Nakshatra-dispositor relationships.

The sole question is:

Is the First Pass a complete and internally consistent structural analysis of the horoscope according to the supplied chart data and corpus, and if not, exactly what is wrong or missing?
```

### What the audit demonstrated

Testing showed that an independent audit could catch errors and
omissions that the First Pass had missed: incorrect aspect geometry,
misapplied rulerships, corpus-specific qualifications, degree-sensitive
weakness, retrograde qualifications, doshas, and additional structural
perspectives.

Equally important, the audit itself is **not ground truth**. Different
audits can miss different things. It is a QA mechanism, not an
additional primary corpus.

------------------------------------------------------------------------

## 5. Second Pass: Turn the Audit into a Small Patch

The audit can be long and argumentative. It should **not** be added
directly to the final working source set.

Instead, its useful findings are distilled into a concise Second Pass.

Second Pass has only three jobs:

1.  **CORRECTIONS** --- replace wrong First Pass statements;
2.  **QUALIFICATIONS** --- add important exceptions or limitations;
3.  **ADDITIONAL STRUCTURES** --- record significant static conditions
    First Pass missed.

The Audit itself must not be blindly trusted. Before a finding is
promoted into Second Pass, NotebookLM should verify it against the
original chart data and Braha/Harihar.

The desired mental model is:

``` text
First Pass = map
Audit      = error detector
Second Pass = patch
```

### Second Pass Prompt

``` text
Using the First Pass and its independent Audit, prepare a brief Second Pass supplement containing only material necessary to correct or complete the First Pass.

Include only:

CORRECTIONS — statements in First Pass that must be replaced.

QUALIFICATIONS — important corpus-supported limitations or exceptions to First Pass conclusions.

ADDITIONAL STRUCTURES — significant static structural conditions that First Pass omitted.

For each item, give the corrected or additional finding in one or two concise sentences. Cite the relevant primary source.

Do not repeat correct First Pass material. Do not explain the reasoning at length. Do not reproduce the Audit. Do not interpret implications for the native's life.

Independently verify Audit findings against the chart data and Braha/Harihar before including them.

Exclude Dasha, timing, planetary maturity, Nakshatra analysis and biographical interpretation.

Target length: approximately 500–800 words.

This document is a patch to First Pass. Where it corrects First Pass, Second Pass takes precedence.
```

A useful refinement to the precedence rule is:

> Where Second Pass **corrects** First Pass, Second Pass takes
> precedence. Where it **qualifies or supplements** First Pass, the two
> should be read together.

------------------------------------------------------------------------

## 6. The Final Working Source Set

Once Second Pass is complete, the Audit has served its purpose and need
not remain in the interpretation source set.

The Notebook can now contain:

``` text
Chart
Navamsha
Dasha
Braha
Harihar
First Pass
Second Pass
```

These are not seven equivalent documents.

### Primary computational evidence

**Chart / Rashi**\
Defines natal positions and structural facts.

**Navamsha**\
Provides divisional evidence where supported by the corpus.

**Dasha**\
Provides the temporal activation sequence.

### Primary interpretive evidence

**Braha + Harihar**\
Define the astrological rules against which chart structures are
interpreted.

### Derived analytical aids

**First Pass**\
A precomputed structural map.

**Second Pass**\
A verified patch containing corrections, qualifications, and omissions.

First Pass and Second Pass therefore function rather like a cached
analytical layer. They reduce repeated rediscovery of the chart
structure, but NotebookLM is never restricted to them. For any
substantive question it may return to Chart, Navamsha, Dasha, Braha, and
Harihar.

------------------------------------------------------------------------

## 7. Subsequent Interpretation: Use Everything Relevant

The structural passes are the **Sorcerer's Apprentice**, not the
astrologer.

For an actual question---career, health, writing, wealth, family, a
Dasha period, or an overall reading---NotebookLM should use whatever
parts of the complete notebook are relevant.

For example, an overall analysis should conceptually be able to combine:

``` text
Natal structure
      +
Navamsha reinforcement / modification
      +
Dasha temporal activation
      +
Braha / Harihar rules
      +
First Pass structural map
      +
Second Pass corrections
      =
Integrated interpretation
```

The persistent instruction deliberately says that First Pass and Second
Pass are **precomputed structural aids, not substitutes for the primary
chart data or corpus**.

This prevents an unintended architecture in which the model interprets
only the summaries and stops consulting the underlying evidence.

------------------------------------------------------------------------

## 8. Clean-Context Testing and Confirmation Bias

One of the most important operational lessons is that NotebookLM can
construct persuasive explanations around a premise already present in
the conversation.

Therefore, when testing a proposition seriously:

1.  clear the chat history;
2.  retain the same sources and persistent instruction;
3.  phrase the new question neutrally;
4.  do not tell NotebookLM the answer expected;
5.  accept disagreement rather than reformulating until the desired
    answer appears.

A useful example is to avoid:

``` text
Why does the chart show publisher rejection but eventual author recognition?
```

and instead ask independently:

``` text
Examine the horoscope and identify what the corpus supports regarding:

(a) writing and authorship,
(b) institutional or commercial publication of written work, and
(c) public recognition arising from written or intellectual work.

Analyse these independently before comparing them.

Do not assume that any of these outcomes has occurred or will occur. Distinguish direct corpus support from your own synthesis. Use all relevant Chart, Navamsha, Dasha, First Pass and Second Pass evidence.
```

The second form treats the proposition as a hypothesis rather than
feeding the desired narrative to the model.

------------------------------------------------------------------------

## 9. Current P21 + NotebookLM Workflow

The resulting operational pipeline is:

``` text
                    ┌──────────────────────┐
                    │ P21 Computation      │
                    │ Chart / D9 / Dasha   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Braha + Harihar      │
                    │ Curated Corpus       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ FIRST PASS           │
                    │ Structural Map       │
                    └──────────┬───────────┘
                               │
                         clear chat
                               │
                               ▼
                    ┌──────────────────────┐
                    │ AUDIT                │
                    │ Adversarial QA       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ SECOND PASS          │
                    │ Verified Patch       │
                    └──────────┬───────────┘
                               │
                               ▼
        ┌─────────────────────────────────────────────┐
        │ FINAL WORKING NOTEBOOK                      │
        │ Chart + Navamsha + Dasha                    │
        │ Braha + Harihar                             │
        │ First Pass + Second Pass                    │
        └──────────────────────┬──────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ User Questions       │
                    │ Fresh context where  │
                    │ independence matters │
                    └──────────────────────┘
```

The Audit is intentionally absent from the final working notebook. It is
**QA machinery**. Its verified output survives through Second Pass.

------------------------------------------------------------------------

## 10. Design Principles

The workflow can be summarized in a few principles.

### Light prompts, strong process

Do not attempt to reproduce the entire corpus inside prompts. NotebookLM
appears to work better when prompts specify the task and epistemic
discipline but leave source retrieval and synthesis to the model.

### Specific over generic

A broad planetary or house indication should not override a specific
corpus rule directly matching the chart.

### Construction and criticism are separate jobs

The model that constructs First Pass should not be asked immediately to
defend or critique it in the same conversational context.

### Derived analysis never replaces primary evidence

First Pass and Second Pass accelerate and stabilize interpretation. They
do not become a new astrological corpus.

### Audit the auditor

Audit findings are hypotheses until checked against Chart/Navamsha and
Braha/Harihar.

### Do not repair every omission by enlarging the prompt

If every missed rule is added to First Pass, the prompt eventually
becomes an unwieldy substitute for the corpus. The Audit + Second Pass
mechanism exists precisely to avoid this.

### Keep biography downstream

Structural analysis should proceed:

``` text
Chart + Corpus -> Interpretation
```

not:

``` text
Known Biography -> Search for an Astrological Explanation
```

When retrospective validation is explicitly desired, it should be
treated as a separate exercise.

------------------------------------------------------------------------

## 11. Status

This workflow does not change the P21 computational code or the
Braha/Harihar corpus. It is an **interpretation-layer protocol** built
around NotebookLM.

It therefore fits the current P21 development position: computational
and corpus work can remain stable while prompt and interpretation
methodology continue to be experimentally refined.

The principal methodological result is:

> **P21 supplies the computation. Braha and Harihar supply the rules.
> First Pass constructs the map. Audit attacks the map. Second Pass
> patches it. NotebookLM then interprets the complete evidence for the
> question actually being asked.**

This converts NotebookLM from a one-shot horoscope generator into a more
disciplined **analysis--verification--interpretation pipeline**.
