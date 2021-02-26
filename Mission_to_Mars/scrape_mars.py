#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars - Scrapping - Erick Hernandez

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_header():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    
    soup = BeautifulSoup(html, "html.parser")
    
    headlines = soup("div", class_="content_title")
    headlines = list(headlines)
    
    text = (headlines[1])
    text = str(text)
    text_slice = text.split('>')
    my_header = text_slice[2]
    my_header = my_header.replace("</a", "")
    
    browser.quit()
    
    return my_header
    

def scrape_desc():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    
    soup = BeautifulSoup(html, "html.parser")

    # Scrapping for description only
    try:
        my_desc = soup.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        my_desc = soup.find("div", class_="article_teaser_body")
    except AttributeError:
        my_desc = soup.find("div", class_="article_teaser_body").getText()

    browser.quit()
    
    return my_desc

def image_scrape():
    browser = init_browser()
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    
    html = browser.html
    
    soup = BeautifulSoup(html, 'html.parser')
    
    image = soup.find("a", class_="button fancybox").get('data-fancybox-href')
    
    browser.quit()
        
    return f'https://www.jpl.nasa.gov{image}'


def tweet_scrape():
    
    browser = init_browser()
    
    url = "https://twitter.com/MarsWxReport/"
    
    browser.visit(url)
    
    browser.execute_script("window.scrollTo(1, document.body.scrollHeight);")
    
    html = browser.html
    
    browser.quit()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    tweet_list = soup.find_all("div", class_="css-901oao")
    tweet_list = str(tweet_list)
    
    return tweet_list


def table_scrape():
    
    url = "https://space-facts.com/mars/"
 
    tables = pd.read_html(url)

    my_table = pd.DataFrame(tables[0])
    
    my_table = my_table.rename(columns={0: "Facts", 1: "Data"})
    
    my_table.set_index("Facts")
    
    html_table = my_table.to_html()
    
    return html_table


def cerberus():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url)
    
    html = browser.html
    
    browser.quit()
    
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

def schiaparelli():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url)
    
    html = browser.html
    
    browser.quit()
    
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


def syrtis():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url)
    
    html = browser.html
    
    
    browser.quit()
    
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


def valles_marineris():
    browser = init_browser()
    
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url)
    
    html = browser.html
    
    browser.quit()
    
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

# GENERAL SCRAPPING FUNCTION

def scrape():
    dictionary = {
        "_id": 1,
        "Header": scrape_header(),
        "Description": scrape_desc(),
        "Featured_image": image_scrape(),
        "Facts_table": table_scrape(),
        "Cerberus_img": cerberus(),
        "Schiaparelli_img": schiaparelli(),
        "Syrtis_img": syrtis(),
        "Marineris_img": valles_marineris()
        }
    return dictionary


out_put = scrape()