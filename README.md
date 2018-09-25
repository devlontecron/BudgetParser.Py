# BudgetParser.Py
Python project to extract, label, and aggregate expenses from a formatted text file.
To run, call script with arg1= BudgetKeys.json and arg2=inputTextfile (& python budgetParser.py BudgetKeys.json sample.txt)

## Problem Statement:
Develop a program to label and aggregate expenses from a formatted text file.
### Sub problem:
Be able to handle unexpected descriptors in transactions and create labels for future use
Be able to store tags without the use of a database and still recall for future use

## Personal Review:
This project came from wanting to simplify and more personally track expenses for my finances. I noticed having this close granular control on tagging allowed me to categorize transactions more clearly that made sense to me. For example, noting the difference between lunch from work and just eating out in general.<br><br>
The database problem was a fun work around challenge that I’ve thought about countless times but never implemented till now. This provided a perfect solution for quick, easy access to data that would could be called on in the future and by others, so long as they have the file, without the need of a server. <br><br>
This project also was my first major introduction to python helped me understand the ins and outs of the scripting language. I noticed major benefits in how quickly and easily to write out a program with so little coding. The lack of “boiler-plate” code allows for clean and concise code.<br>
However, I also noticed a few faults in python. The type-less object reference caused me to easily get confused and unsure of what to call on what object. While it does offer flexibility for development, it also makes solving problems and knowing the “best” solution hard to see. 
