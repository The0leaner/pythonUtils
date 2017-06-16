import random
import MySQLdb

class Handler(BaseHandler):
    crawl_config = {
    }
    def __init__(self, title , content):
        self.db = MySQLdb.connect('localhost', 'root', 'nowcoder', 'wenda', charset='utf8')
    def add_question(self):
        try:
            cursor = db.cursor()
            sql = 'insert into question(title, content, user_id, created_date,comment_count) values("%s", "%s", % d, % s, % d)' % (
                                                            'title', 'content', random.randint(1, 10), 'now()', 0)
            print sql
            print cursor.lastrowid
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print e
            self.db.rollback()

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://veex.com/?tab=tech', callback=self.index_page)
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http://veex.com/?tab="]').items():
            self.crawl(each.attr.href, callback=self.tab_page)

    @config(priority=2)
    def tab_page(self, response):
        for each in response.doc('a[href^="http://veex.com/go/"]').items():
            self.crawl(each.attr.href, callback=self.board_page)

    @config(priority=2)
    def board_page(self, response):
        for each in response.doc('a[href^="http://veex.com/t/"]').items():
            url = each.attr.href
            if url.find('#find') > 0:
                url = url[0:url.find('#')]
            self.crawl(each.attr.href, callback=self.detail_page)
        for each in response.doc('a.page_normal').items():
            self.crawl(each.attr.href, callback= self.board_page)

    @config(priority=2)
    def detail_page(self, response):
        title = response.doc('h1').text()
        content = response.doc('div.topic.content').html().replace('"', "\\")
        self.add_question(title, content)
        return {
                "url": response.url,
                "title": response.doc('title').text(),
                }