# web-scraping-challenge

Scraping from different sources, storage into Mongo DB and rendering with Flask and HTML

In this project, I was able to demonstrate my web scraping abilities that include:

-> Site inspection
-> Identification of required information and extraction
-> Storing into MongoDB
-> Rendering of HTML templates with pymongo and Flask modules

The initial analysis was carried out with Jupyter notebooks. After proving its feasibility, the script was imported to a single python script file and defined a new function that would gather the whole process into one variable.
The information would be stored with MongoDB using pymongo module. With this information available, a Flask app was designed so the local host would render a HTML site, showing the aforementioned data.

As per the functionality of the site, a link to a /scrape site is included, that would trigger an updated scraping query.
