import wordfreq
import sys
import urllib.request

def main():
    response = urllib.request.urlopen(sys.argv[3])
    lines = response.read().decode("utf8").splitlines()

    #file_article = open(sys.argv[3], encoding="utf-8")
    file_stopwords = open(sys.argv[2], encoding="utf-8")
    number = sys.argv[4]

    words = wordfreq.tokenize(lines)

    stopwords = []
    for char in file_stopwords:
        stopwords.append(char.replace("\n", ""))


    Workwords = wordfreq.countWords(words,stopwords)
    print(Workwords)
    print(wordfreq.PrintTopmost(Workwords,int(number) + 1))
    file_stopwords.close()
    #file_article.close()
main()


