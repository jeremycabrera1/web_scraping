from readline import backend

import requests
from bs4 import BeautifulSoup
import pprint
import re

res = requests.get('https://news.ycombinator.com/jobs')
soup = BeautifulSoup(res.content, 'html.parser')
links = soup.select('.titleline a')

back_end_jobs = []
junior_jobs = []
entry_jobs = []
for link in links:
    title = link.get_text()
    if re.search(r'back\s*end', title, re.IGNORECASE):
        back_end_jobs.append({
            'title': title,
            'link': link['href']
        })
    if re.search(r'\bjunior\b', title, re.IGNORECASE):
        junior_jobs.append({
            'title': title,
            'link': link['href']
        })

    if re.search(r'\bentry\b', title, re.IGNORECASE):
        entry_jobs.append({
        'title': title,
        'link': link['href']
        })

pprint.pprint(entry_jobs)