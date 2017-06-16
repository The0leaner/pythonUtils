from pyquery import PyQuery

if __name__ == '__mian__':
	q = PyQuery(open('v2ex.html').read())

	print  q('title').text()
	
	for each in q('div.inner>a').item():
		if each.attr.href.find('tab') > 0:
		    print 1, each.attr.href
		
	for each in q('#Tabs>a').item():
		print 2, each.attr.href

	for each in q('.cell>a[href^="/go/"]').items():
		print 3, each.attr.href
	for each in q('.cell a[href^="/go/"]').items():
		print 4, each.attr.href

	for each in q('span.item_title>a').items():
		print 5, each.html()