class User:
	def __init__(self):
		self.repos = ""
		self.username = ""
		self.link = ""

	def get_repos(self):
		return repos

	def get_username(self):
		return username

	def get_link(self):
		return link

	def set_repos(self, repos:str):
		self.repos = repos

	def set_username(self, username:str):
		self.username = username

	def set_link(self, link:str):
		self.link = link

	def __str__(self):
		return f"Username: {self.username}\nRepositório mais famoso: {self.repos}\nLink de perfil: https://github.com/{self.link}\n\n"
