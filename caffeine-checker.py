#pip install pprintpp
#pip install search_engine_parser
#https://github.com/bisohns/search-engine-parser
#https://stackoverflow.com/questions/64801043/use-regular-expression-to-extract-numbers-before-specific-words

import pprint, re
from urllib.parse import urlparse

from search_engine_parser.core.engines.google import Search as GoogleSearch

#input
print('Enter the name of the food/beverage to check caffeine amount: \n')
query = input('> ')
search_args = ('how much caffeine is in ' + query, 2)
gsearch = GoogleSearch()
gresults = gsearch.search(*search_args)

#conditions
a = {"Google": gresults}
i = 0
j = 0
query_limit = 10 #google query limits to only 10 so set it beyond 10 is pointless

#keyword identifier
units = '|'.join(["caffeine", "mg of caffeine"])
number = '\d+[.,]?\d*'                            
cases = fr'({number})(?:[\s\d\-\+\/]*)(?:{units})'
pattern = re.compile(cases)

#list to store all url infos
list = []
websiteref = []

while i < query_limit:
    try: 
        snippet_desc = gresults["descriptions"][i]
        snippet_url = gresults["links"][i]
        list.append(snippet_desc)
        websiteref.append(snippet_url)
        i += 1
    except:
        break

# for verification purpose
# for j in list:
#     if pattern.findall(j):
#         print(pattern.findall(j)) # + gresults["links"](j))

#list to filter out wanted url
list_w_caf = []
web_w_caf = []

for j in list:
    if pattern.findall(j):
        for caf_num in pattern.findall(j):
            list_w_caf.append(caf_num)
            web_w_caf.append(snippet_url)

print(list_w_caf)
print(web_w_caf)

for (k,t) in zip(list_w_caf, web_w_caf):
    print("-->" + k + " mg of caffeine according to " + '\n' + t + '\n')
