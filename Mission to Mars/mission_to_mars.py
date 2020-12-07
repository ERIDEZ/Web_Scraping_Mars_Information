#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars - Scrapping - Erick Hernandez

# ## Phase 1 - Defining operation

# In[1]:


# Import of modules

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


# In[2]:


# Definition of browser

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


# ## Phase 2 - Scrapping of news title, description and date

# In[4]:


def scrape_data():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Scrapping for headers only
    
    headlines = soup("div", class_="content_title")
    headlines = list(headlines)
    
    text = (headlines[1])
    text = str(text)
    text_slice = text.split('>')
    my_header = text_slice[2]
    my_header = my_header.replace("</a", "")
    
    
    # Scrapping for description and date only

    my_desc = soup.find("div", class_="article_teaser_body").get_text()
    my_date = soup.find("div", class_="list_date").get_text()

    return f'Header: {my_header} Description: {my_desc} Date: {my_date}'


# In[5]:


# Preview

print(scrape_data())


#  ## Phase 3 - Scrapping of images

# In[6]:


def image_scrape():
    browser = init_browser()
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    image = soup.find("a", class_="button fancybox").get('data-fancybox-href')
    
    # Hacer que encuentre con link y id manual
    
    return f'https://www.jpl.nasa.gov{image}'


# In[7]:


# Preview

print(image_scrape())


# In[8]:


# https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA16028-1920x1200.jpgBB


# Phase 4 - Scrapping of Twitter

# In[8]:


def tweet_scrape():
    
    browser = init_browser()
    
    url = "https://twitter.com/MarsWxReport/with_replies?lang=en"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    tweet = soup.find_all("div", {"class": "css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
    
    # , {"class": "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}
    
    # Hacer que encuentre con link y id manual
    
    return tweet


# In[9]:


print(tweet_scrape())


# In[56]:


# Phase 5 - Scrapping of Facts


# In[61]:


def table_scrape():
    
    browser = init_browser()
    
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    # visitar https://pbpython.com/pandas-html-table.html
    
    table = soup.find_all("table", {"id": "tablepress-p-mars-no-2"})
    #table = pd.DataFrame(table)

    return table


# In[62]:


table_scrape()


# In[3]:


# Phase 6 - Scrapping of hemispheres images


# In[35]:


def cerberus():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    cerberus_img = soup.find_all("div", class_="downloads")
    cerberus_img = list(cerberus_img[0])
    cerberus_img = cerberus_img[5]
    cerberus_img = str(cerberus_img)
    cerberus_img = cerberus_img.split('"')
    cerberus_img = list(cerberus_img)
    cerberus_img = cerberus_img[1]
    cerberus_img = str(cerberus_img)

    return cerberus_img


# In[36]:


print(cerberus())


# In[37]:


def schiaparelli():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    schiaparelli_img = soup.find_all("div", class_="downloads")
    schiaparelli_img = list(schiaparelli_img[0])
    schiaparelli_img = schiaparelli_img[5]
    schiaparelli_img = str(schiaparelli_img)
    schiaparelli_img = schiaparelli_img.split('"')
    schiaparelli_img = list(schiaparelli_img)
    schiaparelli_img = schiaparelli_img[1]
    schiaparelli_img = str(schiaparelli_img)
    
    return schiaparelli_img


# In[38]:


print(schiaparelli())


# In[41]:


def syrtis():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    syrtis_img = soup.find_all("div", class_="downloads")
    syrtis_img = list(syrtis_img[0])
    syrtis_img = syrtis_img[5]
    syrtis_img = str(syrtis_img)
    syrtis_img = syrtis_img.split('"')
    syrtis_img = list(syrtis_img)
    syrtis_img = syrtis_img[1]
    syrtis_img = str(syrtis_img)
    
    return syrtis_img


# In[42]:


syrtis()


# In[43]:


def valles_marineris():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    marineris_img = soup.find_all("div", class_="downloads")
    marineris_img = list(marineris_img[0])
    marineris_img = marineris_img[5]
    marineris_img = str(marineris_img)
    marineris_img = marineris_img.split('"')
    marineris_img = list(marineris_img)
    marineris_img = marineris_img[1]
    marineris_img = str(marineris_img)
    
    return marineris_img


# In[44]:


print(valles_marineris())


# In[45]:


# Dictionary for Hemispheres


# In[46]:


hemisphere_image_urls = {
    "title": "Valles Marineris Hemisphere", "img_url": valles_marineris(),
    "title": "Cerberus Hemisphere", "img_url": cerberus(),
    "title": "Schiaparelli Hemisphere", "img_url": schiaparelli(),
    "title": "Syrtis Major Hemisphere", "img_url": syrtis()
    }


# In[47]:


print(hemisphere_image_urls)


# In[56]:


hemispheres_list = []

for x in hemisphere_image_urls.keys():
    hemispheres_list.append({
        'title': hemisphere_image_urls.keys(x),
        'img_url': hemisphere_image_urls.values(x) 
    })


# In[53]:


hemispheres_list


# In[ ]:




