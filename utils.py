#to find the title in the list of scraped links
def binarySearch(word, wordList):
    first = 0
    last = len(wordList) - 1
    found = False
    while first <= last and not found:
        middle = (first + last)//2
        if wordList[middle] == word:
            found = True
        else:
            if word < wordList[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found


def create_url(title):
    return "https://en.wikipedia.org/wiki/" + title.replace(' ', '_')


def parse_title(url):
    return url.replace("https://en.wikipedia.org/wiki/", "").replace("_", " ")

def path_finder(group):
    if group['parent']:
        path_finder(group['parent'])
        print(' -> ', end = '')
    print(group['title'], end = '')

