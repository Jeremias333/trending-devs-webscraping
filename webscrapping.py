import requests
from bs4 import BeautifulSoup
url = "https://github.com/trending/developers"

request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

# Capturando a lista de devs por article
list_devs = soup.find_all('article', class_='Box-row d-flex')

#Capturando o primeiro repo do primeiro dev
repo_1st = list_devs[0].find('a',class_="css-truncate css-truncate-target").get('href').split('/')[-1]
print(repo_1st)

#Capturando o nome do usuário
user_1st = list_devs[0].find('h1', class_="h3 lh-condensed").text
print(user_1st.strip())

#Capturando o nome de usuário do usuário
#username_1st = list_devs[0].find('h1', class_="h3 lh-condensed").get('href').text
#print(username_1st)

print(list_devs[0].find('a',class_="css-truncate css-truncate-target").get('href').split('/')[1])