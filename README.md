![parashar21 banner](/images/p21-header-003.png)<br>
# Why Parashar21?
Tycho Brahe and his sister Sophia made thousands of observations of the positions of planets over many years and meticulously recorded this data in a vast database. This data was used by Kepler to formulate the Laws of Planetary motion. That in turn led to Newton's laws of gravitation and the emergence of European science in the eighteenth century. Hence the database created by Tycho and Sophia is the start of the journey from ancient magic to modern science.  Today, the same laws can be deduced very easily and quickly from NASA data on planetary positions. <br> <br> Hindu astrology is based on revelations that Sage Parashar experienced and recorded in the [Brihat Parashara Hora Shastra](https://en.wikipedia.org/wiki/Brihat_Parashara_Hora_Shastra). But if we want to introduce analytical rigour in Hindu astrology and come out with some clear and umbiguous rules,  we need a similar database of searchable horoscope charts. Unfortunately, no such database exists because there is no known way to store horoscope chart data efficiently. Parashar21 aspires to create a mechanism to plug this gap.
# What is Parashar21?
Parashar21 is a design or strategy, along with a collection of programs, to store horoscope chart data as a high dimensional, but non-relational data model, so that charts that meet certain criteria can be retrieved easily. 

### What Parashar21 is not!
Parashar21 is not a prediction engine. There is no attempt to interpret horoscope charts. 
# Overview
![workflow](/images/Workflow.png)<br>
### WARNING 
Because of a recent change in the MongoDB installation process, there is a problem with MongoDB installation process
Some notebooks have been fixed with a temporary patch. Others will be fixed as we discover better solutions
Sorry for the inconvenience
### End of WARNING
# Sample Programs
### How to run sample programs

1. [P21_45_01_Cast_Load](https://github.com/prithwis/parashar21/blob/main/P21_45_01_Cast_Load.ipynb) - Load Birthdata from a CSV file, generate horoscope chart data and load the same into a MongoDB database.  
2. [P21_45_02_Pull_Print](https://github.com/prithwis/parashar21/blob/main/P21_45_02_Pull_Print.ipynb) - Read the MongoDB database, retrieve charts that meet a specific pattern, print reports in MS-Word.  
3. [P21_45_04_YogFilter](https://github.com/prithwis/parashar21/blob/main/P21_45_04_YogFilter.ipynb) - Search for specific patterns called Yogs  in the charts stored in the MongoDB database.
4. [P21_45_06_V2_SingleChart](https://github.com/prithwis/parashar21/blob/main/P21_45_06_V2_SingleChart.ipynb)   - Show detailed analysis of one selected chart, including the names of Yogs, if any, that present in the chart. <br>
This last notebook, demonstrates the full cycle of reading birth data from a CSV file, converting it first to a basic horoscope using Swiss Ephemeris modules, enhancing the basic horoscope with Bhavs, Lords, Status (Exalted, Debilitated, Benefic, Malefic & etc.), Aspects and Conjuncts, storing it in a MongoDB database and then retrieving charts that meet certain specifications. In addition, ending dates of Vimsottari Mahadasha are shown<br> 
What is more interesting is that this same notebook, creates a second, Gochar chart for the individual using the natal Moon longitude as the gochar Lagna longitude to generate the chart of a dummy person called Gochar and calculates Bhav data using the Moon-based Rashi as the first bhav. This report also shows the ending dates of the Vimsottari Antardashas and the current and subsequent Mahadasha <br>
A sample report for President Dr APJ Abdul Kalam, is available in [PDF](https://github.com/prithwis/parashar21/blob/main/Sample%20Reports%202/p21_APJAbdulKa_Ras_B_100918.pdf) format while this [MS-Word](https://github.com/prithwis/parashar21/blob/main/Sample%20Reports%202/p21_APJAbdulKa_Ras_B_100918.doc) file explains the structure of the report.<br> 
5. [P21_45_08_TransitTracker](https://github.com/prithwis/parashar21/blob/main/P21_45_08_TransitTracker.ipynb) - Uses the Swiss Ephemeris software to track changes in the position of planets and also their retrograde status over the next couple of days. This can be printed out as text, or -- this is the fun part -- can be seen as a video of planetary 'movement' along with simple audio. A sample video is available in [my Yantrajaal Blog](http://blog.yantrajaal.com/2022/10/the-transit-tracker.html)

The codes are written in Python 3+ and packaged as [Google Colab](https://www.google.com/search?q=what+is+google+colab) Notebooks. The only software needed to run them is a modern browser, similar to Google Chrome. Nothing needs to downloaded or installed. In case the charts need to stored persistently, then a MongoDB database needs to be made available on a remote hosting service along with the MongoDB login credentials. However, both the [YogFilter](https://github.com/prithwis/parashar21/blob/main/P21_45_04_YogFilter.ipynb) and the [Single Chart Analysis](https://github.com/prithwis/parashar21/blob/main/P21_45_06_SingleChart_Details.ipynb) notebooks can be executed with a local MongoDB database that is installed on-the-fly in the Google Colab Virtual Machine. To execute the code, one needs to press the blue "Open in Colab" button to initiate the VM and then execute the code cells in a top to bottom sequence. Reports are generated as MS-Word documents and stored on the Colab VM. They need to be downloaded to a local machine for viewing.
### Additional Codes
The horoscope chart data in a MongoDB database can be accessed in an interactive way using a MERN (MongoDB, Express, React, Node) application to retrieve and disiplay charts. Codes for this are available in the [Khona21 repository](https://github.com/prithwis/khona21)
# Further information
The philosophy that drives this enterprise is articulated in the article [Astrology - an application of Data Science](https://www.linkedin.com/pulse/astrology-an-application-data-science-prithwis-mukerjee/) <br>
A preprint of the paper describing technical aspects is available at [Efficient storage and retrieval of horoscope data on a computer system. A case study using Python and MongoDB](https://www.researchgate.net/publication/358191949_Efficient_storage_and_retrieval_of_horoscope_data_on_a_computer_system_A_case_study_using_Python_and_MongoDB?channel=doi&linkId=61f47fec007fb50447205dcd&showFulltext=true)<br>
More technical information is available in the project [wiki](https://github.com/prithwis/parashar21/wiki) <br>
For a history of this project, visit the [Parashar21 Blog](https://parashar21.blogspot.com/) <br> 
