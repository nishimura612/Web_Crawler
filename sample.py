import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'    # Spiderの名前。
    # クロールを開始するURLをリストで指定する。タプルでもok。
    start_urls = ['https://blog.scrapinghub.com']

    # start_urlで指定したページを取得後に呼ばれるメソッド。spider.Responseオブジェクトを受け取る。
    def parse(self, response):
        """
        記事一覧ページから、各記事のタイトルを抜き出す
        """
        # 記事タイトル(h2)を抜き出す
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        # 次のページのリンクを抜き出してたどる
        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
