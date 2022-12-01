# Caffeine Checker Python Script
Search results for caffeinated products: \
![alt text](https://github.com/asherchok/caffeine-checker/blob/main/example-1.gif?raw=true) \
Results for non-caffeinated products: \
![alt text](https://github.com/asherchok/caffeine-checker/blob/main/example-2.gif?raw=true)


## Motivation
The goal of this script is to obtain faster search results with lesser keyboard input: skipping the manual process of typing extra keywords like "is there caffeine in X" or "X caffeine content" in Google to check caffeine content in a food or beverage.

## References
The following sources were used to achieve the goal of this project:
- [Search Engine Parser documentation](https://search-engine-parser.readthedocs.io/en/latest/)
- [Keyword extraction with regex](https://docs.python.org/3/library/re.html)

## Environment
- [Python 3.10.8](https://www.python.org/downloads/)

## How to use

Install the following libraries on Windows PowerShell terminal:

```sh
pip install pprintpp
pip install search_engine_parser
```
Save the python file caffeine<nolink>-checker.py to your preferred directory from this repository. Read a quick tutorial on how to navigate directory on PowerShell terminal [here](https://www.itprotoday.com/powershell/how-use-powershell-navigate-windows-folder-structure). 
### Activating the script
At the directory that you had saved the caffeine<nolink>-checker.py script, enter the following onto the terminal:
```sh
python .\caffeine-checker.py
```
### Instructions
Internet connection is required for this script to work (for the search engine). After typing the terminal command, user will be asked to enter the name of the food or beverage into the terminal. Enter desired keyword into the prompt, then the script will do the following automatically:

-Searches "Caffeine content in 
`your input`" on google \
-Obtain the amount of caffeine information from each website's featured snippets (or website description) \
-Display to user website snippets that has caffeine amount keyword in it.

## Limitations
Current version of the script cannot query more than 10 results (i.e. beyond page 1 of google search results) to obtain larger quantity of webpage featured snippet.

## Issues

This work has omitted user agent option to allow faster query speed. If user request several search results in a short amount of time, the query will be flagged for unusual traffic and return the following error: \
![alt text](https://github.com/asherchok/caffeine-checker/blob/main/traffic-error.JPG?raw=true)

Pull requests are welcomed to improve the functionality of the script. Future improvement of this project would be developing a mobile phone app with similar function.

## License
MIT

[//]: # (Comments here will not be read by markdown compiler)
