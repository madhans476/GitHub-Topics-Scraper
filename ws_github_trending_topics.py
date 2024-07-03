import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

output_dir = 'github_topics'
os.makedirs(output_dir, exist_ok=True)

url = 'https://github.com/topics'
baseurl = 'https://github.com'

response = requests.get(url)
# print(response.status_code)
html_str = response.text

soup = BeautifulSoup(html_str, 'html.parser',)
topics = soup.find_all('div', class_='py-4 border-bottom d-flex flex-justify-between')


name = []
description = []
url = []

print(f"Started scraping {url} ...")
print("Scraping the trending Github topics...")
for topic in topics:

    topic_name = topic.find('p', class_ = 'f3 lh-condensed mb-0 mt-1 Link--primary')    #! tag object
    # print(type(topic_name))
    topic_name = topic_name.string              #! string is used to extract only the text from the tag
    # print(type(topic_name))

    topic_desc = topic.find('p', class_ = 'f5 color-fg-muted mb-0 mt-1')         
    topic_desc = topic_desc.string
    topic_desc = topic_desc.strip()             #! strip is used to remove unwnated spaces

    topic_url = topic.find('a', class_ = 'no-underline flex-grow-0')
    topic_url = topic_url['href']               #! 'href' is the attribute of the 'a' tag(topic_url - 'a' tag obj)
    topic_url = baseurl+topic_url


    name.append(topic_name)
    description.append(topic_desc)
    url.append(topic_url)
    # break;
print("Completed scraping the trending Github topics!!!")

dict = {'Name': name, 'Description': description, 'URL': url}

def create_csv(dict, name):
    df = pd.DataFrame(dict)
    csv_filename = os.path.join(output_dir, f"{name}.csv")
    if not os.path.exists(csv_filename):
        df.to_csv(csv_filename, index=False)
        print(f"Created {name}.csv file!!!")
    else:
        print(f"{name}.csv file already exists!!!")

# converting dict ──dataframe──> csv
create_csv(dict, 'Trending_github_topics')


# Getting information out of each topic page
for i in range(len(url)):

    print(f"Scraping top repositories for {name[i]}...")
    response = requests.get(url[i])
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topic_url))
    
    soup = BeautifulSoup(response.text, 'html.parser')
    t_doc = soup.find_all('article', class_='border rounded color-shadow-small color-bg-subtle my-4')


    repo_list = []
    user_list = []
    stars_list = []
    repo_link_list = []

    for doc in t_doc:
        username = doc.find('h3', class_ = 'f3 color-fg-muted text-normal lh-condensed').find('a', class_ = 'Link')
        username = username.string.strip()

        repo_name = doc.find('h3', class_ = 'f3 color-fg-muted text-normal lh-condensed').find('a', class_ = 'Link text-bold wb-break-word')
        repo_name = repo_name.string.strip()

        repo_url = doc.find('h3', class_ = 'f3 color-fg-muted text-normal lh-condensed').find('a', class_ = 'Link text-bold wb-break-word')
        repo_url = baseurl + repo_url['href']

        rating = doc.find('span', class_="Counter js-social-count").string.strip()
        if rating[-1] == 'k':
            stars = int(float(rating[:-1])*1000)
        else:
            stars = int(rating)
        
        repo_list.append(repo_name)
        user_list.append(username)
        stars_list.append(stars)
        repo_link_list.append(repo_url)

        # break
    
    dict = {"Repository name": repo_list, "Username": user_list, "Stars": stars_list, "URL": repo_link_list}
    print(f"Completed scraping top repositories for {name[i]}!!!")

    create_csv(dict, name[i])

print(f"Completed scraping !!!")
    

