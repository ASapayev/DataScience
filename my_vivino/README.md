# 02-Data-Science-My-Vivino
Welcome to Our  My Vivino Project
***

## Task
Data collecting and Building wine recommendation system

## Description
Our goal is not only make our customers happy, but do some analysis. Unfortunately, we don’t have the data we need, so let’s get it. 
Where to find the data? Any where. Scrap Vivino / Bevmo / Delectable / Wine-Searcher /

I have chose www.wine.com 

Additionally, we created a prediction system for wine by building an ML model to predict the rating of low-rated wines. And left a link for review, you can find it in the 'link_to_blogpost.txt' folder.

## Installation
Please download http key to download this project, install all required libraries and run.
If you haven't installed the necessary libraries, run the following command in a code cell to install them:
   ```python
   !pip install pandas numpy scikit-learn seaborn matplotlib
   ```

## Usage
To build recommendation system I have used from feature_extraction.text TfidfVectorizer and from metrics.pairwise cosine_similarity of Scikit-Learn library.
### Running the Jupyter Notebook

**Open the Notebook:** Start by opening the Jupyter Notebook file (`my_vivino.ipynb`) in Jupyter Notebook or JupyterLab.
#### NB!
The main function with some lines of code commented out, as web scraping takes more time than I would like to spend on it.
So after selecting and cleaning the data, I saved it to a csv file(`wine_data_for_recomendations.csv`) that you can open and explore at will.


In this Recommendation system you will enter name or type wine in which you are interested and this system will open top 10 most popular wines in wine.com and will open their web pages separately.
All functions are written in the correct order. All you have to do is use the cells in order.


```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
