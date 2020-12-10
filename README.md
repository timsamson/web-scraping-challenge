# web-scraping-challenge
<img src="Missions_to_Mars/templates/images/mission_to_mars.png" alt="Mission to Mars">
<br>
<h3>Introduction</h3>

Project scrapes various websites to extract data and combines it into a sumamry webpage. This project uses mongoDB and the chrome extention dirver to accomplish this task. 

<br>
<h3>Web Scraping</h3>
<p>The web scraping is completed by using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, and a Jupyter Notebook file called mssion_to_mars.ipynb is used to complete all the scraping and analysis tasks.</p>
<br>
<h3>MongoDB and Flask App</h3>
<p>MongoDB with Flask templating was used to to create a new HTML page that displays all of the scraped data. Once the scraping code was completed in jupyter notebook, it was then converted into a Python script and function called scrape_mars. When the function is called form teh website via the scrape button, the function opens a new window in ChromeBrowser, completes the scarpe and updates the web page. 
</p>
<br>
<h3>Loading Notebook and HTML page</h3>
<p>All files are contained within a folder calles Mission_to_mars in the repo.</p>
<p>To open the jupyter notebook, please ensure all dependencies below are installed in the environment you which to run the porject in. Launch Jupyter notebook, nagivate to the apporoporate folder and open notebook.
</p>
<p>To launch the HTML file and app, naviagte to thh appropoiate folder within the repo "Missions_to_Mars"</p>
<p>To initiate the scrape, open terminal, ensure that dependencies are loaded and environement is active. Launhc app.py by running "python app.py" in the terminal. Copy the web address and paste into browser. App will navigate to index page. To scrape new date, press the scrape mars button, the flask app will run, scapre hte page and return the most current results from the scraped pages. /p><br>

<h3>Dependencies</h3>
 <ul>
<li>Pandas</li>
<li>Jupyter Notebook</li>
<li>Requests</li>
<li>Splinter</li>
<li>BeautifulSoup</li>
<li>ChromeDriver</li></ul>
