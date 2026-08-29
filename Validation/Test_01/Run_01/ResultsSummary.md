Certainly. Here is a compact record of **Pilot 1** as it currently stands.

## Parashar21 + NotebookLM — Pilot 1 Summary

### Objective

To test whether **Parashar21 computational horoscope data + NotebookLM interpretation**, using a fixed Jyotisha corpus, could generate specific and biographically discriminating observations about well-known individuals **without being given their identities or biographies**.

Ten subjects with Rodden **AA-rated birth data** were selected. Each was analysed anonymously in a fresh NotebookLM notebook using the same source corpus and frozen General Prompt v1.2. Only the supplied **Rashi chart and Vimshottari Dasha** were permitted; Navamsha and other Vargas were explicitly excluded.

Each report generated exactly four specific predictions. After all reports had been produced, identities were unblinded and predictions were checked against public biographical information.

### Evaluation method

Each report was treated as a 50-mark examination:

* Prediction 1: 10
* Prediction 2: 10
* Prediction 3: 10
* Prediction 4: 10
* General analysis outside the four predictions: 10

Predictions were assessed for specificity, factual correspondence and timing. Incorrect or unverifiable predictions received little or no credit. Posthumous predictions were heavily penalised.

### Results

| Subject          |     P1 |     P2 |     P3 |     P4 | General |       Total |
| ---------------- | -----: | -----: | -----: | -----: | ------: | ----------: |
| Albert Einstein  |      9 |      9 |     10 |     10 |       8 |      **46** |
| Frida Kahlo*     |      3 |     10 |      7 |      2 |       4 |      **26** |
| Tiger Woods      |      6 |      2 |      1 |      9 |       6 |      **24** |
| Muhammad Ali     |      3 |      2 |      9 |      2 |       6 |      **22** |
| Ernest Hemingway |      1 |      5 |      3 |      4 |       7 |      **20** |
| Steve Jobs       |      7 |      0 |      0 |      1 |       6 |      **14** |
| Elvis Presley    |      4 |      0 |      3 |      0 |       6 |      **13** |
| Sanjay Gandhi    |      1 |      4 |      3 |      0 |       4 |      **12** |
| Pablo Picasso    |      0 |      2 |      5 |      0 |       4 |      **11** |
| Marilyn Monroe   |      0 |      0 |      0 |      7 |       3 |      **10** |
| **Total**        | **34** | **34** | **41** | **35** |  **54** | **198/500** |

**Raw score: 39.6%.**

*There is an identified scoring-consistency issue with Kahlo P2. The prediction correctly identified severe marital disruption but placed it in a posthumous period. Under the standard subsequently applied to Ali, Elvis and others, **10/10 is too generous**. This should be corrected before treating 198/500 as the final archival score. A reduction to 5–6 would put the overall result at approximately **38.6–38.8%**.

### Individual assessment

**Einstein — 46/50.** Exceptional result. The report identified scientific/intellectual eminence, the period of major discoveries, international honours, forced exile and later serious cardiovascular danger with unusually good chronological correspondence. This was by far the strongest report.

**Jobs — 14/50.** Some useful general identification of creativity, technical/intellectual ability, wealth, ambition and philosophical interests, but the report missed the defining career sequence—early success, expulsion from Apple, NeXT/Pixar, return and transformation of Apple—and failed badly on later health/longevity.

**Picasso — 11/50.** Correctly detected extraordinary creativity, reputation, wealth and long productivity, but failed to identify visual art. Instead it repeatedly moved toward science, intellectual research and writing. This was a major vocational failure.

**Monroe — 10/50.** One interesting chronological hit around the 1952–54 reversal of fortune, but otherwise poor. It failed to identify acting, glamour, sexuality and mass celebrity and confidently predicted events decades after her death at 36.

**Ali — 22/50.** Considerable useful signal in the broader analysis: physical force, competition, leadership, victory, international prominence and later severe mobility problems. The latter was particularly good. But the final predictions inexplicably converted these indicators into technical/scientific and intellectual careers rather than boxing.

**Kahlo — provisionally 26/50.** Foreign connections and severe marital instability were identified, but the report missed both defining characteristics of her biography: **visual art and catastrophic lifelong physical disability**. Particularly damaging was its positive longevity assessment despite her death at 47.

**Hemingway — 20/50.** The upstream analysis detected martial temperament, wit/intellect, foreign residence, emotional instability, anxiety and troubled relationships rather well. Yet the final predictions turned him into an engineer and failed to identify literature. The analysis contained more useful information than the four predictions selected from it.

**Woods — 24/50.** Strong indications of competition, determination, wealth, resilience and sudden reversals. The prediction of severe physical injury/surgery during the period containing his catastrophic 2021 car accident was particularly impressive, although the predicted anatomical region was wrong. Again, vocational identification failed: Woods became a writer/publisher rather than an athlete.

**Elvis — 13/50.** The broader reading detected mass leadership, wealth, property/vehicles, persuasive public presence, sensuality, relationship instability, melancholy and spirituality. Yet it failed to identify music, performance or entertainment and projected academic/literary activity and spirituality long after his death.

**Sanjay Gandhi — 12/50.** Some correspondence with authority, administration, unconventional behaviour, public prominence and sudden reversals, but his proposed profession was legal/judicial. Most seriously, despite repeatedly discussing the 8th lord, Mars, physical danger and sudden changes, the analysis missed his violent accidental death at 33 and continued predicting his life into the twenty-first century.

## Principal findings

The experiment did **not** produce consistent blind predictive accuracy. Performance varied enormously, from Einstein's 46/50 to Monroe's 10/50. The overall score therefore conceals considerable heterogeneity.

Nevertheless, several predictions were sufficiently specific to deserve attention: Einstein's forced exile and later vascular crisis; Ali's severe later mobility impairment; Woods's major injury/surgery during the correct Dasha period; and some correctly identified periods of professional or relationship disruption.

Three systematic weaknesses emerged.

**First, occupational discrimination was poor.** Picasso was not identified as an artist, Hemingway as a writer, Ali or Woods as sportsmen, or Elvis as a performer. The reports often identified plausible underlying characteristics—creativity, communication, competition, physical force, public prominence—but mapped them onto the wrong real-world profession.

**Second, longevity was a serious problem.** Monroe, Kahlo, Hemingway, Elvis and Sanjay Gandhi all died substantially earlier than the system's implied lifespan. NotebookLM nevertheless continued generating confident Dasha-based predictions for periods after their deaths. This is one of the clearest methodological failures in Pilot 1.

**Third, the upstream interpretation was sometimes better than the final prediction selection.** Hemingway and Ali are particularly clear examples. Potentially relevant characteristics appeared in the integrated analysis but were not selected when NotebookLM had to produce four specific predictions. This suggests that part of the problem may lie in converting a large collection of astrological indications into a small number of concrete real-world predictions.

## Implications for Pilot 2

Pilot 1 suggests that another unrestricted four-prediction experiment would add relatively little. A more discriminating second experiment would retain the **same ten charts** but restrict the target domain to:

**career/profession → nature of professional activity → fame/success → professional failure/reversal and timing.**

Using the same subjects would permit direct comparison with Pilot 1 rather than introducing another uncontrolled variable.

A second question worth testing is whether **limited contextual information improves interpretation**. A blind career analysis could first be performed, followed by a separate analysis supplied only with broad occupational/educational context. This would distinguish the ability to *discover* profession from the ability to *interpret a known professional trajectory astrologically*.

Finally, source retrieval should be tightened before Pilot 2. In particular, the remaining problematic HM material could be converted to clean text, while retaining the otherwise frozen corpus. Each subject should continue to use a completely fresh NotebookLM notebook.

### Bottom line

**Pilot 1 result: approximately 40%, with very high variance.**

It does **not provide convincing evidence of reliable blind biographical prediction**. Equally, it is not simply random-looking noise: several unusually specific hits and some recurring useful signals warrant a more tightly controlled experiment.

The most important result may therefore be methodological rather than astrological:

> **Parashar21 + NotebookLM appears substantially better at extracting broad characteristics and occasionally identifying significant timed events than at converting those indications into the correct profession or a coherent blind life history.**

That is the proposition Pilot 2 should now test directly.
