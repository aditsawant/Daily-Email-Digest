# Since all the methods below are not inter-related, no need to encapsulate all these in a single Content class. 
# We can just have content.py as a Pythod module that contains all the useful methods.
import csv
import random
import json
from urllib import request

def getWikiArticle():
    try:
        data = json.load(request.urlopen('https://en.wikipedia.org/api/rest_v1/page/random/summary'))
        return {'title': data['title'],
                'extract': data['extract'],
                'url': data['content_urls']['desktop']['page']}
    except Exception as e:
        print(e)

def getRandomQuote(quotesCSV = 'Quotes.csv'):
    try:
        with open(quotesCSV) as csvfile:
            quotes = [{'quote': line[0],
                        'book': line[1],
                        'author': line[2]} for line in csv.reader(csvfile)]
    except Exception as e:
        quotes = [{'quote': 'Default Quote',
                    'book': 'The Book',
                    'author': 'Me'}]
    
    return random.choice(quotes)

if __name__ == '__main__':
    # Testing getWikiArticle
    # wiki = getWikiArticle()
    # if(wiki == None):
    #     print('wiki is None')
    # print(f'{wiki["title"]}:\n {wiki["extract"]}\n at the URL: {wiki["url"]}')
    # print("This is a new line\n")



    # Testing getRandomQuote
    quote = getRandomQuote()
    print("\n\n" + quote['quote'])
    print(" - By " + quote['author'] + " in " + quote['book'] + "\n\n")

    # quote = getRandomQuote(quotesCSV = None)
    # print("\n\n" + quote['quote'])
    # print(" - By " + quote['author'] + " in " + quote['book'] + "\n\n")