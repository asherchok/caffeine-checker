#pip install pprintpp
#pip install search_engine_parser
#https://github.com/bisohns/search-engine-parser
#https://stackoverflow.com/questions/64801043/use-regular-expression-to-extract-numbers-before-specific-words

import pprint, re

from search_engine_parser.core.engines.google import Search as GoogleSearch

print('Enter the name of the food/beverage to check caffeine amount: \n')
query = input('> ')
search_args = ('how much caffeine is in ' + query, 2)
gsearch = GoogleSearch()
gresults = gsearch.search(*search_args)

a = {"Google": gresults}
i = 0
j = 0

list = []
websiteref = []
while i < 10:
    try:
        #print(str(i) + gresults["descriptions"][i])
        caff_in_i = gresults["descriptions"][i]
        caff_web = gresults["links"][i]
        if 'mg of caffeine' or 'of caffeine' in caff_in_i:
            list.append(caff_in_i)
            websiteref.append(caff_web)
        else:
            pass
        i += 1
    except:
        break

units = '|'.join(["caffeine", "mg of caffeine"])
number = '\d+[.,]?\d*'                            
cases = fr'({number})(?:[\s\d\-\+\/]*)(?:{units})'
pattern = re.compile(cases)
# for verification purpose
# for j in list:
#     if pattern.findall(j):
#         print(pattern.findall(j)) # + gresults["links"](j))
# print(list)

for j in list:
    if pattern.findall(j):
        for caf_num in pattern.findall(j):
            print(caf_num + 'mg of caffeine according to')
    print('\n It is not a caffeine-free food/beverage.')
    # else:
    #     print("this is a caffeine-free food/beverage.")