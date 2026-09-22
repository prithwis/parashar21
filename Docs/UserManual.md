# Parashar21-LLM User Manual

The Parashar21-LLM pipeline can be used without detailed knowledge of either Python or LLM technology. However, a basic familiarity with GitHub, Google Colab, and Google NotebookLM is useful.

## 1. Open the Parashar21 notebook

Go to the Parashar21 GitHub repository:

`https://github.com/prithwis/parashar21/tree/main`

Open the notebook:

`P21_51_Chart2LLM.ipynb`

Click the blue **Open in Colab** button to open the notebook in Google Colab.

## 2. Enter the birth details

Locate the cell containing the birth details of the default person, actress Rekha:

```python
%%writefile peopleData.csv
Gender,DoB_Day,DoB_Mon,DoB_Year,DoB_Time,TZ_OffHours,PoB_Lat,PoB_Lon,TZ_Name,TZ_Type,Name,tag1,tag2,tag3,tag4,tag5,tag6
F,10,10,1954,11:00,5.5,13.08,80.27,IST,standard,RekhaG,Actor,nil,Dancer,nil,nil,nil
```

Replace the second line with the birth details of the person whose horoscope you wish to analyse.

## 3. Generate the Rashi chart

Locate the following code:

```python
p21.AnalysisType = 'Rashi'       # one of ['Rashi','Navamsa']
#p21.AnalysisType = 'Navamsa'    # one of ['Rashi','Navamsa']
```

Leave it as shown above to generate the **Rashi (birth) chart**.

Run the entire notebook once.

This generates:

* `chart.txt` — birth-chart information in LLM-readable form
* `dasha.txt` — Vimshottari Dasha information in LLM-readable form

Two `.doc` files are also generated. These contain similar information, together with Gochar data, in a more human-readable format.

Download `chart.txt` and `dasha.txt` from Colab to your computer.

## 4. Generate the Navamsha chart

Change the option above by commenting out the Rashi line and uncommenting the Navamsha line:

```python
#p21.AnalysisType = 'Rashi'      # one of ['Rashi','Navamsa']
p21.AnalysisType = 'Navamsa'     # one of ['Rashi','Navamsa']
```

Run the notebook again.

It is not necessary to rerun the entire notebook. You can start from the cell containing:

```python
!rm *.doc
!rm *.json
!rm *.txt
```

and run all cells below it.

This generates:

* `navamsa-chart.txt`
* `navamsa-dasha.txt`

`navamsa-dasha.txt` is simply another copy of the previously generated Dasha information and can be ignored.

Download `navamsa-chart.txt` to your computer.

You should now have the three files required for LLM analysis:

* `chart.txt`
* `navamsa-chart.txt`
* `dasha.txt`

## 5. Create a NotebookLM notebook

Open:

`notebooklm.google.com`

Create a new notebook.

**Note:** A Google Colab notebook and a Google NotebookLM notebook are two entirely different things. Colab is being used to generate the horoscope data; NotebookLM is being used to analyse it.

Upload the following three files:

* `chart.txt`
* `navamsa-chart.txt`
* `dasha.txt`

Also upload one or more texts containing the astrological corpus that you want NotebookLM to use.

Corpus texts in PDF form are acceptable. However, OCR errors introduced while converting printed material into machine-readable text can seriously impair retrieval and analysis. **Clean `.txt` files are preferable whenever available.**

## 6. Begin the astrological analysis

Start with a simple, general prompt such as:

> You are an Indian/Hindu astrologer who has been asked to give an opinion on the horoscope of a native.
>
> The horoscope is provided through three text files: `chart.txt` containing the birth chart, `navamsa-chart.txt` containing the Navamsha chart, and `dasha.txt` containing the Vimshottari Dasha periods.
>
> You are also given text files containing rules and interpretations of Hindu astrology.
>
> Use only these supplied files. Do not use any other file, URL, website, or external source of astrological information.
>
> Based on these sources, give an overall assessment of the birth chart and Navamsha chart. Identify the major strengths, weaknesses, and particularly significant features, and explain how each may manifest in the native's life.
>
> Identify important combinations or yogas wherever supported by the sources. Where multiple sources support the same conclusion, mention this. Where the sources differ or disagree, identify the disagreement and explain how you interpret it in the context of this horoscope.
>
> Jai Parashar.

## 7. Continue conversationally

After the initial assessment, ask specific questions in ordinary conversational language.

There is no need to use elaborate or highly structured prompts. Questions can concern career, education, wealth, marriage, family, health, major life events, particular Dasha periods, or any other issue of interest.

Where useful, provide NotebookLM with relevant facts about the native's actual life. This allows subsequent questions to be more focused and resembles a normal consultation with an astrologer.

The objective is not to test whether the LLM can guess the native's biography. The objective is to use the calculated horoscope, Dasha information, and supplied astrological corpus to explore questions about the native's life in a source-grounded manner.
