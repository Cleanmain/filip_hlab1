def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        end = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1
            if start >= len(line):
                break
            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                print(line[start:end].ljust(15) + " Is a word")
                ord = line[start:end].lower()
                words.append(ord)
                start = end - 1
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end + 1
                print(line[start:end].ljust(15) + " Is a number")
                words.append(line[start:end])
                start = end - 1
            else:
                print(line[start].ljust(15) + " Is a symbol")
                words.append(line[start:end])
            start = start + 1
    return words



def countWords(words, stopWords):
    frequencies = {}
    ignorecurrentword = False
    for currentword in words:
        ignorecurrentword = False
        for currentStopword in stopWords:
           if currentword == currentStopword:
               print("Ignore " + currentword)
               ignorecurrentword = True
        if ignorecurrentword != True:
           if currentword not in frequencies.keys():
               frequencies[currentword] = 1
           else:
               number = frequencies[currentword]
               newnumber = number + 1
               frequencies[currentword] = newnumber
    return frequencies


def PrintTopmost(frequencies,n):
    sortedfreqencies = sorted(frequencies.items(), key = lambda item: -item[1])
    topsort = sortedfreqencies[1:n]
    for key, value in topsort:
        print(key.ljust(9)+ "  :", str(value))
















