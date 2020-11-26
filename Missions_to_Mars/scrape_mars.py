# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as Soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import pymongo
import time

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    # Retrieve the latest news title and paragraph
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    news_soup = Soup(html, 'html.parser')
    time.sleep(1)
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news = news_soup.find_all('div', class_='article_teaser_body')[0].text

    #Feature Image
    base_url = 'https://www.jpl.nasa.gov'
    feature_url = base_url + '/spaceimages/?search=&category=Mars'
    browser.visit(feature_url)
    html = browser.html
    image_soup = Soup(html, 'html.parser')
    image_url=image_soup.find("a", class_ = "button fancybox")["data-fancybox-href"]
    featured_image_url = base_url + image_url

    #Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[2]
    mars_facts_df.columns = ["Description", "Value"]
    mars_html_table = mars_facts_df.to_html()
    mars_html_table.replace('\n', '')

    #Hemisphere
    base_url = 'https://astrogeology.usgs.gov'
    search_url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(search_url)
    html = browser.html
    soup = Soup(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    img_urls = []
    titles = []

    for item in items:
        titles.append(item.find('h3').text.strip())
        url = (base_url + item.find('a')['href'])
        browser.visit(url)
        html = browser.html
        soup = Soup(html, 'html.parser')
        hem_url = base_url+soup.find('img',class_='wide-image')['src']
        img_urls.append(hem_url)
        
    hemisphere_image_urls = []

    for i in range(len(titles)):
        hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})

    hemisphere_image_urls

    for i in range(len(hemisphere_image_urls)):
        print(hemisphere_image_urls[i]['title'])
        print(hemisphere_image_urls[i]['img_url'] + '\n')

    #Dictionary
    mars_dict = {
        "news_title": news_title,
        "news": news,
        "featured_image_url": featured_image_url,
        "fact_table": str(mars_html_table),
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_dict

       