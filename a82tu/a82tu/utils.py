import re
from parsel import Selector


def get_movie_list(text):
    """
    返回电影下载地址列表
    yield 名称,下载地址
    """
    sel = Selector(text)
    text = sel.css('.downurl script').extract_first()
    if text is None or text == '':
        return
    urls = re.search(r'GvodUrls1 = "([^"]+)"', text).group(1)
    for i in urls.split('###'):
        yield i.split('$')
