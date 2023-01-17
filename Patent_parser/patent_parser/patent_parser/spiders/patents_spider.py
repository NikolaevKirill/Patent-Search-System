import scrapy


class PatentsSpider(scrapy.Spider):
    name = "patents"
    start_urls = [
        "https://new.fips.ru/registers-doc-view/fips_servlet?DB=RUPAT&DocNumber=2640290&TypeFile=html",
        "https://new.fips.ru/registers-doc-view/fips_servlet?DB=RUPAT&DocNumber=2640291&TypeFile=html",
    ]

    def parse(self, response):
        number_of_patent = response.url.split("&")[-2][10:]
        filename = f"patent-{number_of_patent}.html"
        with open(filename, "wb") as f:
            f.write(response.body)

        # keys_data = response.xpath("//table[@id='bib']/tr/td/p/b/text()").getall() данные по патенту
        # date = keys_data[1]
        # quotes = keys_data[4].split('. ')
        # authors = [i.split(',')[0] for i in keys_data[7:-2]]
        # patent_owner = keys_data[-1]
        # country = response.xpath("//table[@class='tp']/tr/td/div[@class='topfield2']/text()").get()
        # type_of_doc = response.xpath("//table[@class='tp']/tr/td/div[@class='topfield2']/text()").getall()[-1]
        # name_spk = response.xpath("//table[@class='tp']/tr/td/div[@class='top7']/ul/li/span/span[@class='i']/text()").getall()
        # date_spk = response.xpath("//table[@class='tp']/tr/td/div[@class='top7']/ul/li/span/text()").getall()
        # spk = [i[0] + i[1] for i in zip(name_spk, date_spk)]
        # name_mpk = response.xpath("//table[@class='tp']/tr/td/div[@class='top7']/ul/li/a/span/text()").get()
        # date_spk = response.xpath("//table[@class='tp']/tr/td/div[@class='top7']/ul/li/a/text()").get()
        # mpl = [i[0] + i[1] for i in zip(name_mpk, date_mpk)]
        # title = response.xpath("//p[@id='B542']/b/text()").get()
        # using_abstract = response.xpath("//div[@id='Abs']/p/text()")[1].get()
        # all_abstract = [i for i in response.xpath("//div[@id='mainDoc']/p/text()")[2:-8].getall() if not  (('\n' in set(i)) and (' ' in set(i)))]
        # sources_of_information = [i for i in all_abstract if (('Источники информации' in i) or ('Патент' in i) or ('Заявка на изобретение' in i))]
        # body_of_abstract = [i for i in all_abstract if not (('Источники информации' in i) or ('Патент' in i) or ('Заявка на изобретение' in i))]
        # ind_patent_claims = [ind for ind, i in enumerate(body_of_abstract)]
        # patent_claims = body_of_abstract[ind_patent_claims+1:]
        # patent_description = body_of_abstract[:ind_patent_claims]
