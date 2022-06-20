![parashar21 banner](/images/p21-header-003.png)<br>
## Casting and storing horoscope charts for Hindu Astrology
# Motivation
Astronomical observations that were made with the naked eye and recorded in a vast database by Tycho Brahe and his sister Sophia were the basis for the formulation of Kepler's Laws of Planetary motion. That in turn led to Newton's laws of gravitation and the emergence of European science in the eighteenth century.  Today, the same laws can be deduced very easily and quickly from NASA data on planetary positions. If we wish to do the same with astrology and come out with some clear and umbiguous rules,  we need a vast database of searchable horoscope data. Unfortunately, that is not available at the moment. Parashar21 aspires to create a mechanism to plug this gap.
# What is Parashar21
Parashar21 is a design or strategy, along with a collection of programs, to store horoscope chart data as a high dimensional, but non-relational data model, so that charts that meet certain criteria can be retrieved easily. In principle, the following types of tasks are demonstrated
1. Read a very minimal set of data that define a horoscope, provided in csv file [like this](https://github.com/prithwis/parashar21/blob/main/data/Test5Data.txt) that has data about 5 people.
2. Use this data to build a richer and more detailed horoscope and convert it into a [JSON  object](https://raw.githubusercontent.com/prithwis/parashar21/main/data/peopleDataTest5.json).
3. Store the horoscopes (or JSON objects) in both (a) a MongoDB database and (b) a txt file
4. Retrieve horoscopes from the MongoDB database based on values of data stored in the fields, using MongoDB query syntax
5. Generate horoscope charts in one of three styles, namely Bengal, North India and South India
6. Generate a report that gives detailed information about the horoscopes.
7. Store the report in a MS Word doc file. [Samples shown here](https://github.com/prithwis/parashar21/tree/main/Sample%20Reports%202)

For a history of this project, visit the [Parashar21 Blog](https://parashar21.blogspot.com/) <br>
A preprint of the paper describing this project is available at [DOI: 10.13140/RG.2.2.19476.58240](https://www.researchgate.net/publication/358191949_Efficient_storage_and_retrieval_of_horoscope_data_on_a_computer_system_A_case_study_using_Python_and_MongoDB?channel=doi&linkId=61f47fec007fb50447205dcd&showFulltext=true)
# Sample / Demo Codes
1. Load Birthdata, generate horoscope charts and load the same into a MongoDB database. See this [notebook](https://github.com/prithwis/parashar21/blob/main/P21_45_Cast_Load.ipynb).
2. Read the MongoDB database and filter out charts that meet a specific pattern. See this [notebook](https://github.com/prithwis/parashar21/blob/main/P21_45_Pull_Print.ipynb).
3. For those not having access to MongoDB installation, a standalone mechanism to install MongoDB in the Colab VM. Load sample data and filter out charts as in point 2. See this [notebook](https://github.com/prithwis/parashar21/blob/main/P21_45_Pull_Print_StandAlone.ipynb).
# Updates
1. As an extension of the search for arbitrary patterns, we now have a way to search for specific [Astrological Yogs](https://github.com/prithwis/parashar21/blob/main/P21_45_YogFilter.ipynb) in the charts stored in the MongoDB database.
2. Rather than search for patterns, get all the details about a [single chart](https://github.com/prithwis/parashar21/blob/main/P21_45_SingleChart_Analysis.ipynb).
