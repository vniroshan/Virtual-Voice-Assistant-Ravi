# r=requests.get('https://en.wiktionary.org/w/api.php',params={'action':'query','format':'json','prop':'info','titles':'water','inprop':'url'})
# >>> r
# <Response [200]>
# >>> r.json()
# {'batchcomplete': '', 'query': {'pages': {'3749998': {'pageid': 3749998, 'ns': 0, 'title': 'water', 'contentmodel': 'wikitext', 'pagelanguage': 'en', 'pagelanguagehtmlcode': 'en', 'pagelanguagedir': 'ltr', 'touched': '2019-11-09T17:05:09Z', 'lastrevid': 57947952, 'length': 214308, 'fullurl': 'https://en.wiktionary.org/wiki/water', 'editurl': 'https://en.wiktionary.org/w/index.php?title=water&action=edit', 'canonicalurl': 'https://en.wiktionary.org/wiki/water'}}}}
# >>> pprint(r.json())
# {'batchcomplete': '',
#  'query': {'pages': {'3749998': {'canonicalurl': 'https://en.wiktionary.org/wiki/water',
#                                  'contentmodel': 'wikitext',
#                                  'editurl': 'https://en.wiktionary.org/w/index.php?title=water&action=edit',
#                                  'fullurl': 'https://en.wiktionary.org/wiki/water',
#                                  'lastrevid': 57947952,
#                                  'length': 214308,
#                                  'ns': 0,
#                                  'pageid': 3749998,
#                                  'pagelanguage': 'en',
#                                  'pagelanguagedir': 'ltr',
#                                  'pagelanguagehtmlcode': 'en',
#                                  'title': 'water',
#                                  'touched': '2019-11-09T17:05:09Z'}}}}
# >>> r=requests.get('https://en.wiktionary.org/w/api.php',params={'action':'query','format':'json','prop':'info','titles':'water','inprop':'url'})
#
# PageID converted to URL via CurID parameter.
# e.g. PageID of 2357
# https://en.wiktionary.org/w/index.php?curid=2357
#
# It is assumed the MediaWiki page at full URL still needs to be parsed by some kind of code.
#
# Ref: https://www.mediawiki.org/wiki/API:Tutorial
# Ref: https://medium.com/@ihsavru/fetching-data-with-the-mediawiki-api-db8ad25c96b9
