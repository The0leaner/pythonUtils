class Handler(BaseHandler):
    crawl_config = {
        'header': {
            'User-Agent':'GoogleBot',
            'Host':'www.zhihu.com',
        }

    }

    def __init__(self, title , content):
        self.db = MySQLdb.connect('localhost', 'root', 'nowcoder', 'wenda', charset='utf8')
    def add_question(self, title, content, comment_count):
        try:
            cursor = db.cursor()
            sql = 'insert into question(title, content, user_id, created_date,comment_count) values("%s", "%s", % d, % s, % d)' % (
                                                            'title', 'content', random.randint(1, 10), 'now()', 0)
            print sql
            print cursor.lastrowid
            cursor.execute(sql)
            self.db.commit()
            return qid
        except Exception, e:
            print e
            self.db.rollback()
        return 0

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://zhihu.com/topic/19562940/top-answers', callback=self.index_page, validate_cerf=False)
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a.question_link').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cerf=False)
    @config(priority=2)
    def detail_page(self, response):
        items = response.doc('div.zm-editable-content clearfix').items()
        title = response.doc('spam.zm-editable-content').text()
        html = response.doc('div.zm-editable-content').html()
        #zu-top-feed-list navigable
        if html == None:
            html = ''
        content = html.replace('"', '\\"')
        qid = self.add_question(title, content, sum(1, for x in items))
        return {
                "url": response.url,
                "title": response.doc('title').text(),
                }