import scraping_github
import user

qtd = 10

input(f"Iremos apresentar as {qtd} pessoas do Trending do Github, press enter para continuar...")

scraping_github.__init__(qtd)

for item in scraping_github.get_list():
	print(item)