# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:09:39 2020

@author: Mayank Joshi
"""

## Loading Selenium and Scrapy
from scrapy import Selector
from selenium import webdriver

chromedriver_path = "C:\\Users\\mayank joshi\\Desktop\\Hacks\\chromedriver.exe"

## Website link
search = "https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced"

## Loading the url in 
try:
    driver = webdriver.Chrome(chromedriver_path) 
    driver.get(search)
except:
    print("Error connecting")
    
start = '01/12/2020'
end = '14/12/2020'

## passing date values
driver.find_element_by_name("date(applicationValidatedStart)").send_keys(start)
driver.find_element_by_name("date(applicationValidatedEnd)").send_keys(end)

## clicking the search button
driver.find_element_by_xpath("//input[@value='Search']").click()

##getting the html page source
html = driver.page_source    
sel = Selector(text = html)

all_links = sel.xpath('//li[@class="searchresult"]/a/@href').extract()

## getting the link to the first application
base = "https://publicaccess.wycombe.gov.uk"
first_link = base + sel.xpath('//li[@class="searchresult"]/a/@href').extract_first()

driver.get(first_link)

html_2 = driver.page_source
sel_2 = Selector(text = html_2)

## Extracting data from table
table = sel_2.xpath('//*[@id="simpleDetailsTable"]//tbody')

rows = table.xpath('//tr')

col_1 = []
col_2 = []

for row in sel_2.xpath('//*[@id="simpleDetailsTable"]//tbody//tr'):
    col_1.append(row.xpath('th//text()')[0].extract().strip())
    col_2.append(row.xpath('td//text()')[0].extract().strip())
    if row.xpath('th//text()')[0].extract().strip() == "Proposal":
        rqrd = row.xpath('td//text()')[0].extract().strip()

print(rqrd)

## Closing the browser
driver.quit()
