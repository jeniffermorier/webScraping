from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.error import HTTPError
from urllib.error import URLError
import os


siteBegin = "http://www.ans.gov.br"
fileTitle = ''

def createFileName(name):
    print(name)
    fileTitle = name

def download_file(download_url):
    urlretrieve(download_url, 'Componente_Organizacional.pdf')

def readingPage():
    res = BeautifulSoup(html.read(), 'html.parser');
    createFileName(res.title)
    tags = res.findAll("a", {"class": "btn btn-primary btn-sm center-block"})
    for tag in tags:
        if 'pdf' in tag.getText():
            site = siteBegin + tag.attrs['href']
            download_file(site)
            print("Download Concluido!")

#*************************************************
try:
    html = urlopen("http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-junho-2020")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    readingPage()

#*************************************************





