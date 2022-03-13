from pyfiglet import Figlet
custom_fig = Figlet(font='ivrit')
from urllib import response
import requests
from bs4 import BeautifulSoup


url= input("Crawler Pagina Web:")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for a in soup.find_all("a", href=True):
     print("Encontrado:", a['href'] if a['href'].startswith("http") else
str(response.url[:-1] + a['href']))