from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


class Parser():
    def __init__(self, url, tagTitulo, tagLink):
        """
        class construtora, indique os itens solicitados abaixo
        :param url:
        :param tagTitulo:
        :param tagLink:
        """
        self.url = url
        self.tagTitulo = tagTitulo
        self.tagLink = tagLink

    def parseHtml(self):
        """
        Faz o  parse do html vindo através da uri
        :return: html parseado pelo bs4
        """
        try:
            htmlRequest = urlopen(self.url)
        except HTTPError:
            print("Error no servidor, provavelmente, 404 - página não encontrada - ou 500")
        except URLError:
            print("URL informada está incorreta, verifique novamente.")
        else:
            return BeautifulSoup(htmlRequest.read(), 'html.parser')



if __name__ == '__main__':
    url = 'https://stackoverflow.com/jobs?l=Brazil'
    tagTitulo = 'h2'
    tagLink = 'a'
    crawler = Parser(url, tagTitulo, tagLink)
    crawler.parseHtml()
