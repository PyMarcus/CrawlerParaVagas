from parserHTML import Parser
from pandas import DataFrame


def dataframe(titulos, links):
    dt = DataFrame(links, titulos,  columns=['VAGA'])
    print(dt)


class Crawler:
    def __init__(self, url, tagTitulo, tagLink):
        """
        classe construtora, pega parâmetros informados abaixo
        :param url:
        :param tagTitulo:
        :param tagLink:
        """
        self.url = url
        self.tagTitulo = tagTitulo
        self.tagLink = tagLink

    def rastreio(self):
        """
        faz o rastreio
        :return: titulos e links (strings)
        """
        titulos = []
        links = []
        parser = Parser(self.url, self.tagTitulo, self.tagLink)
        bs = parser.parseHtml()
        for titulo in bs.findAll(self.tagTitulo, {'class': 'mb4 fc-black-800 fs-body3'}):
            titulos.append(titulo.text[1:])

        for index, link in enumerate(bs.findAll(self.tagLink, {'class': 's-link stretched-link'})):
            if 'href' in link.attrs:
                if link.attrs['href'] not in links:
                    links.append('https://stackoverflow.com' + link.attrs['href'])

        return dataframe(titulos, links)


if __name__ == '__main__':
    url = 'https://stackoverflow.com/jobs?l=Brazil'
    tagTitulo = 'h2'
    tagLink = 'a'
    crawler = Crawler(url, tagTitulo, tagLink)
    crawler.rastreio()
