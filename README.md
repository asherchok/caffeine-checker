# Caffeine Checker Python Script

(insert images here of question asked and result printed)
-one image with "ryse pre workout flavor X"
-another similar image but idfferent beverage
-one image with "this food or bev has no caffeine"

For an Android APK version of this script, [click here](insert google drive link)

## About
The goal of this script is to skip the manual process of typing extra keywords like "is there caffeine in X" or "X caffeine content" in Google to check caffeine content of a food or beverage. This script is designed to achieve faster search results with lesser keyword query. The following sources were used to achieve the goal of this project:
- [Search Engine Parser documentation](https://search-engine-parser.readthedocs.io/en/latest/)
- [Number extraction from specific keywords](https://stackoverflow.com/questions/64801043/use-regular-expression-to-extract-numbers-before-specific-words)

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
Internet connection is required for this script to work. When the command above was ran in the terminal, user will be asked to enter the name of the food or beverage into the terminal.

- Unplug the USB device.
- Press '/' key.

To stop the script entirely, press CTRL + BREAK (or pause key on laptop keyboards).

##### (optional)
To change the close window key other than the / key, simply edit Line 14 and change / into any other key. One possible example to close the window with c key instead of / would be:
```sh
      if cv2.waitKey(1) & 0xFF == ord('c'):
```
## Limitations
Current version of the script cannot query more than 10 results (i.e. beyond page 1 of google search results) to obtain larger quantity of webpage featured snippet.

## Issues

(An image with failed word getter with coke as example)

issue: code did not include user agent to allow faster query speed but introduces random chance of getting blocked for many attempts in short amount of time

Pull requests are welcomed to improve the following project. Future improvement of this project would be converting the python file to an executable file so that users can skip all the steps in **How to use** and **Activating the script**.

## License
MIT

[//]: # (Comments here will not be read by markdown compiler)
