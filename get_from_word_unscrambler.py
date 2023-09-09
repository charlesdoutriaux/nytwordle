import requests

def parse(url, search):

    r = requests.get(url)
    content = r.content.decode()
    cont = True
    words = []
    while cont:
        start = content.find(search)
        # print(content[start-10:start+10])
        content = content[start+len(search):]
        end = content.find(search)
        if end == -1:
            cont = False
        words.append(content[:content.find('"')].upper())
    return words

words = []
url, search = "https://www.wordunscrambler.net/word-list/wordle-word-list",'href="/unscramble/'
wordl_words = parse(url, search)

with open("wordle.txt", "w") as f:
    print(",".join(wordl_words), file=f)
url, search ="https://www.wordunscrambler.net/words/5-letter", "meaning of "
# for i in range()
i = 1
n = 0
nwords = 0
while n!=1:
    if i == 1:
        ext = ""
    else:
        ext = f"?page={i}"
    words += parse(url+ext, search)
    n = len(words) - nwords
    print(i,n)
    nwords += n
    i+=1
    
words = words[:-1]

with open("all_words.txt", "w") as f:
    print(",".join(words), file=f)