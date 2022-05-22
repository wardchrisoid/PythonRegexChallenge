# PythonRegexChallenge
=================================================================

Hello, this challenge was created to solve the following prompt:
Please write code that takes a chat message string as input and returns a JSON formatted string containing information about its contents. You should look for at least the following features:

1) @mentions - This is a way to mention another user. They always start with '@' and end when hitting a non-word character. 

2) Links - any URLs that are contained in the message, plus the page's current HTML title up to 200 characters max. You can assume that all URLs start with http. 

3) Emoticons - for this exercise, you can assume that emoticons are defined as any alphanumeric string, no longer than 15 characters with no whitespace, contained in parenthesis. 

4) An integer word count of remaining words, not counting any @mentions, links, or emoticons.
====================================================================
# How to Use
1) Clone the git directory
2) Write the strings you would like to process in the inputfile.txt
3) Run main.py in the same directory as inputfile.txt and a blank outputfile.txt
4) Inspect the results in outputfile.txt
