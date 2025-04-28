import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/',)
res2 = requests.get('https://news.ycombinator.com/?p=2',)
# Parse Data from 'res' and assign it to soup variable
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Grabbing all the links and point scores and assigning them to the 'links' and 'votes' variables respectively
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

# Define a function that take links and votes as arguments
def create_custom_hn(links, subtext):
    hn = []
    # Loop through all the links
    for idx, item in enumerate(links):
        # Get the title from each index. The .getText() gets the text within the tag
        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))