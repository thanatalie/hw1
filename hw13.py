from collections import Counter


#Get user input#
charSet = list(raw_input("Letter? "))
charSetCounter = Counter(charSet)

#Make word#
def possibleWords(input,charSet):
    for word in wordref:
        char_cout = Counter(word.lower())
        flag = 1

        for character in 'abcdefghijklmnopqrstuvwxyz':
            if char_cout[character] > charSetCounter[character]:
                flag = 0
        if flag==1:
            p.append(word.lower())

# Driver program#
if __name__ == "__main__":
    wordref = [line.strip() for line in open('/usr/share/dict/words')] #Get dictionary#

    p = []
    possibleWords(input,charSet)
    sp=sorted(p, key=len , reverse=True) #sorted words
    print sp
