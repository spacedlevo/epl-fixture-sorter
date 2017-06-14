import requests
from bs4 import BeautifulSoup
import re
import sys
import os

baseurl = 'https://www.premierleague.com/news/'
page_id = sys.argv[1]  # this is the id number in the page URL
season = sys.argv[2]
fix_dirs = './fixtures/' + season + '/'

page = requests.get(baseurl + page_id)
print('Got page content')
content = BeautifulSoup(page.content, 'html.parser')
content = re.sub('<br.*?>', '\n', str(content))  # converts breaklines to newlines
content = re.sub('<.*?>', '', content)  # removes HTML tags
content = re.sub('\(.*\)', '', content)  # removes times

fixtures = re.findall('.+\sv\s.+', content)  # extracts fixtures

if not os.path.exists(fix_dirs):
    os.makedirs(fix_dirs)

i = 0
gw_num = 1
for j in range(0, len(fixtures), 10):
    week = fixtures[i:i + 10]
    with open((fix_dirs + 'gameweek%s.txt') % (gw_num), 'w') as fix_file:
        fix_file.writelines('\n'.join(week))
    gw_num += 1
    i += 10
print("completed downloading fixtures")
