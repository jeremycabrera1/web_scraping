#Importing libraries
import requests
from bs4 import BeautifulSoup
import re
import pprint

# Getting connection to the hackernew site
res = requests.get('https://news.ycombinator.com/jobs')
# Using Beautiful soup to parse through the content on the page
soup = BeautifulSoup(res.content, 'html.parser')
# Get all the links on the page
links = soup.select('.titleline a')

# Create the lists to output the job titles to
back_end_jobs = []
junior_jobs = []
entry_jobs = []

# Loop through each item in links
for link in links:
    # Strip away the link and get only the text
    title = link.get_text()
    # First append all the backend jobs use re module to get the necessary information
    if re.search(r'back\s*end', title, re.IGNORECASE):
        back_end_jobs.append({
            'Title': title,
            'Link': link['href'],
        })
    # First append all the junior jobs use re module to get the necessary information
    if re.search(r'\bjunior\b', title, re.IGNORECASE):
        junior_jobs.append({
            'Title': title,
            'Link': link['href'],
        })
    # First append all the entry jobs use re module to get the necessary information
    if re.search(r'\bentry\b', title, re.IGNORECASE):
        entry_jobs.append({
            'Title': title,
            'Link': link['href'],
        })

pprint.pprint(back_end_jobs)
