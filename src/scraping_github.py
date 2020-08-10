import requests
from bs4 import BeautifulSoup
from user import User

url = "https://github.com/trending/developers"

request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')



list_devs = soup.find_all('article', class_='Box-row d-flex')
list_users = list()

def __init__(last=10):#popula os objetos e adiciona a lista.
	for pos in range(0,last):
		user = User()
		user.set_repos(list_devs[pos].find('a',class_="css-truncate css-truncate-target").get('href').split('/')[-1].strip())
		user.set_username(list_devs[pos].find('h1', class_="h3 lh-condensed").text.strip())
		user.set_link(list_devs[pos].find('a',class_="css-truncate css-truncate-target").get('href').split('/')[1].strip())
		list_users.append(user)

def get_list():#retorna lista de objetos populada.
	return list_users
