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

#keyword identifier
units = '|'.join(["mg of caffeine", "milligrams of caffeine", "no caffeine", "zero caffeine"])                 
regex = fr'(?i)((?:\S+\s+){{0,5}})\b({units})\b\s*((?:\S+\s+){{0,5}})'
pattern = re.compile(regex)

for (j,k) in zip(list, websiteref):
    if pattern.findall(j):
        shortened_url = urlparse(str(k)).netloc
        for caf_num in pattern.findall(j):
            caf_num_sum = ' '.join(caf_num)
            abbrv = '... ' + caf_num_sum + ' ...'
            print(abbrv + "\n according to " + shortened_url + '\n[LINK] ' + k + '\n')
            
print("-- End of Results --")
