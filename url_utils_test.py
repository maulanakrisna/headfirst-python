
import pprint
from url_utils import gen_from_urls

urls = ('http://talkpython.fm', 'http://pythonpodcast.com', 'http://python.org')

for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}


pprint.pprint(urls_res)
