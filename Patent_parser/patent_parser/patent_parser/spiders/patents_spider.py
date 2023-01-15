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

        # response.css('table p')[1].css('b').get().split('>')[1][:-3]
