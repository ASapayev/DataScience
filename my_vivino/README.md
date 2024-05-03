# 02-Data-Science-My-Vivino

<div class="row">
<div class="col tab-content">
<div class="tab-pane active show" id="subject" role="tabpanel">
<div class="row">
<div class="col-md-12 col-xl-12">
<div class="markdown-body">
<p class="text-muted m-b-15">
</p><h2>My Vivino</h2>
<table>
<thead>
<tr>
<th>Technical details</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Submit file</td>
<td>my_vivino.ipynb</td>
</tr>
</tbody>
</table>
<hr>
<p>My Vivino is an online marketplace. We have a vast wine database, and we have 27 million users, mainly in North America.</p>
<p>One of our leading services is a wine recommendation system. It starts to be a little old. Rules-based. We are selling wine based on our customer visit/research.</p>
<p>You've just finished a meeting with your product manager. Data science is the future, and our competitor <code>my_wine.com</code> has invested a lot in it.</p>
<p>Following your suggestion, my_vivino's CEO has decided to allocate a budget to move forward on the data science project you've proposed.</p>
<p><em>Which project?</em></p>
<p>What are the success criteria?</p>
<ul>
<li>During our next meeting, you will have to show us some data (plot? report?) of what you've been building.</li>
<li>Impact on the business. We need to make our customers happy.</li>
</ul>
<p>What to expect?</p>
<ul>
<li>Slides presentation.</li>
<li>And the DevOps team should be able to push it to production.</li>
</ul>
<p>You've heard the CEO will be joining the meeting. It's a reminder if you do well, you can quickly expect the promotion you are expecting.</p>
<h2>Technical specification</h2>
<p>What is to be a Data Scientist?</p>
<ol>
<li>Data Collecting / Cleaning</li>
<li>Data Exploration</li>
<li>Data Visualization</li>
<li>Machine Learning</li>
<li>Communication</li>
</ol>
<p>You will have to prove yourself in each of these. We are confident you've already done it! :)</p>
<p>Where to find the data?
Any where. Scrap Vivino / Bevmo / Delectable / Wine-Searcher / ...</p>
<p>It's an open project. You are free to find something you find will be useful to do some data analysis on:</p>
<ul>
<li>rating system?</li>
<li>comments system? detect most valuable comments?</li>
<li>wine suggestion?</li>
<li>wine classification?</li>
<li>wine quality?</li>
<li>size of the market analysis?</li>
<li>suggestion base on a meal recipe?</li>
</ul>
<p>Reminder, it will be one of your portfolio projects. You can find a lot of different ideas. Plagiarism is not tolerated in the company either here. :-)
If you don't find enough information on wine, why not moving to the Whisky market, Beer market, or Coca? any beverage market? :-)</p>
<p>You are in data <strong>science</strong>, so your blog post needs to report as a "scientific experiment"; you need to write your assumption, every step of the experiment, and the conclusion.
Usually, with an opening to what you follow, what to experiment next?</p>
<p>The scope is vast. You will find your idea :)</p>
<p>How will this project be graded?</p>
<ul>
<li>Your code</li>
<li>Your code quality</li>
<li>Your slides quality</li>
<li>Business impact</li>
<li>Your blog post (You can inspire yourself from this fascinating <a href="https://kubernetes.io/blog/2020/05/my-exciting-journey-into-kubernetes-history/" target="_blank">blog post</a> on Kubernetes.)</li>
</ul>

<p></p>
</div>

</div>
</div>
</div>
<div class="tab-pane" id="resources" role="tabpanel">
<div class="row">
<div class="col-xl-12">
<div class="row text-center">
<div class="col p-t-10 f-12">
<p>
How To Use Jupyter In Docode
</p>
</div>
</div>
<div class="row text-center">
<div class="col">
<frame frameborder="0" src="https://www.youtube.com/embed/J5MpsvScKzE"></frame>
</div>
</div>

</div>
</div>
</div>
</div>
</div>



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
