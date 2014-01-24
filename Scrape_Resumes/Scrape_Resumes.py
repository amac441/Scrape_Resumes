
import mechanize
import urllib2  #maybe python3
import urllib
import time
#from selenium import webdriver
#from selenium.common.exceptions import NoSuchAttributeException
#from selenium.webdriver.common.keys import Keys
import threading
import os
import re
from bs4 import BeautifulSoup
import requests
#import httplib2
#from BeautifulSoup import SoupStrainer


#job = business-analyst
#city = omaha-ne
resume_links = []
job = 'business'
city = ""
page_num = 0

resume_url = 'http://www.indeed.com/resumes/' + job + '/in-' + city + '?co=US&start=' + str(page_num)
# additional pages http://www.indeed.com/resumes/business-analyst/in-Omaha-NE?co=US&start=10

url = 'http://www.indeed.com/resumes/business-analyst/in-omaha-ne'

# need to grab links from class "app_name"  -  <div class="app_name"><a target="_blank" href="/r/Andrew-Sherwood/0ab8490c15b74c94?sp=0" rel="nofollow" class="app_link" itemprop="url">Andrew Sherwood</a><span class="location"> - Omaha, NE</span></div>

#response = urllib.urlopen(url).read()

#for link in BeautifulSoup(response, parse_only=SoupStrainer('p',{'class':'app_name'})):
#    if link.has_attr('href'):
#        print link['href']

request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response)
#b = soup.findAll('div', attrs={'class':'app_name'})
##print b
##soup.prettify()

#r = requests.get(url)
#data = r.text
#soup = BeautifulSoup(data)

for a in soup.find_all('div', attrs={'class':'app_name'}):
    #print a
    for link in a.find_all('a'):
        resume_links.append(link.get('href'))

print resume_links

#======= GRAB SPECIFIC RESUME BY HYPERLINK ============

person = []

for res in resume_links:
    print '----------RESUME---------------'
    resume_url = 'http://www.indeed.com' + res
    resume_html = urllib.urlopen(resume_url).read()
    soup = BeautifulSoup(resume_html)
    title = []
    company = []


    for a in soup.find_all('div', attrs={'class':'data_display'}):
        a_soup = BeautifulSoup(a)
        
        for b in a_soup.find_all('p', attrs={'class':'work_title title'}):
            title.append(b.getText().encode('ascii', 'ignore'))

            for c in a_soup.find_all('p', attrs={'class':'work_company'}):
                company.append(c.getText().encode('ascii','ignore'))

            for d in a_soup.find_all('p', attrs={'class':'work_dates'}):
                company.append(d.getText().encode('ascii','ignore'))

            for e in a_soup.find_all('p', attrs={'class':'work_description'}):
                #-- TODO: should perform summarization on this!!
                company.append(e.getText().encode('ascii','ignore'))
    
        #for b in a.find_all('p', attrs={'class':'work_title title'}):
        #    title.append(b.getText().encode('ascii', 'ignore'))
        #    #print b.getText().encode('ascii', 'ignore')
        
        #    for c in a.find_all('p', attrs={'class':'work_company'}):
        #        company.append(c.getText().encode('ascii', 'ignore))

    person = [title, company, dates, desc]

        #for text in a.find_all('a'):
        #    resume_links.append(link.get('href'))

#=====  GRAB TEXT ======

#file = open('notes.txt', 'w+')
#htmlfile = urllib.urlopen(url1)
#htmltext = htmlfile.read()
#print htmltext
##print htmltext
#regex = "AgentIssueId=(.+?)&amp"
#pattern = re.compile(regex)
#issue_id = re.findall(pattern,htmltext)
#print issue_id

#the dropdown for page size
#"ctl00_ctl00_ctl00_BaseContent_Content_BaseContent_agvsAgentIssues_cmbPageSize"

#title of page 2
#"Go to Page 2"

#INPUT#ctl00_BaseContent_tbxPassword.textfield

# ==== CODE WONT WORK B/C INCONTACT IS USING AJAX ====

#need to scan this url and grab all agent issue IDs
#<tr class="gridRowWithHoverClass" onclickjavascript="window.location = 'AgentIssueDetail.aspx?AgentIssueId=39440&amp;issueTypeName=';" onclick="rowClicked(event, this); if (this.captureEvents) this.captureEvents(Event.CLICK);" onmouseover="" onmouseout="">

#file = open('notes.txt', 'w+')
#htmlfile = urllib.urlopen(url1)
#htmltext = htmlfile.read()
#print htmltext
##print htmltext
#regex = "AgentIssueId=(.+?)&amp"
#pattern = re.compile(regex)
#issue_id = re.findall(pattern,htmltext)
#print issue_id