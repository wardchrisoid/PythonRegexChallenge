import re
import json
from urllib.request import Request, urlopen

# All imported libraries are included in the standard Python environment

"""
Outputs the processed input string into the appropriate JSON format.
The 'answer' dictionary data type is initialized and assigned the respective JSON categories
If the string lacks a certain JSON category then the empty list is removed from the dictionary. 
Default output is to a file called 'outputfile.txt'
"""


def json_formatting(word_count, mentions, url_pairs, emoticons):
    answer = {
        "emoticons": emoticons,
        "mentions": mentions,
        "links": url_pairs,
        "words": word_count
    }
    if not answer["emoticons"]: answer.pop("emoticons")

    if not answer["mentions"]: answer.pop("mentions")

    if not answer["links"]: answer.pop("links")

    if not answer["words"]: answer.pop("words")

    f = open("outputfile.txt", "a")
    f.write(json.dumps(answer, indent=4))


"""
The method uses regular expressions to identify uses of: mentions, links, emoticons, and the word count
Once these categories have been identified and collected, they are passed to the json_formatting function
An explanation of the regex used:
========================================================================================================================
all_words:   '[\S]+'        || Finds all "words" in the string. Words are consecutive chars delineated by whitespace
mentions:    '@(.*?)\s'     || Scans for a '@' character and then captures the characters until a whitespace char occurs
links: '?:www|https?)[^\s]+'|| Has three patterns for capturing website links. Checks if the word starts with
                            || www, http, or https. Captures all chars after these patterns until a whitespace.
emoticons: '\((\S{0,15})\)' || Captures up to fifteen characters which are surrounded by parenthesis
========================================================================================================================
"""


def regex_scanner():
    f = open("inputfile.txt", "r")
    # Iterate through lines in the file
    for x in f:

        all_words = re.findall("[\S]+", x)
        mentions = re.findall("@(.*?)\s", x)
        links = re.findall("(?:www|https?)[^\s]+", x)
        emoticons = re.findall("\((\S{0,15})\)", x)

        # For word count we subtract the total by the occurrences of other categories
        word_count = len(all_words) - len(mentions) - len(links) - len(emoticons)

        # Initializes data-types used to process and store the informatino from links
        list_of_links = []
        url_pairs = {"url": '', "title": ''}

        for k in links:
            req = Request(k, headers={'User-Agent': 'Mozilla/5.0'})
            resp_data = urlopen(req)
            content = resp_data.read().decode('utf-8')

            # As the page is decoded into utf-8 we can then regex it for it's title.
            title = re.findall("<title>(.*?)<\/title>", content)

            # There may be multiple titles in the page, typically the first one is the correct title.
            title_list = [k, title[0]]

            # zips the initialized url_pairs and title_list together, and appends the result to list_of_links
            list_of_links.append(dict(zip(url_pairs, title_list)))

        # Helper function responsible for output and proper JSON formatting
        json_formatting(word_count, mentions, list_of_links, emoticons)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    regex_scanner()
