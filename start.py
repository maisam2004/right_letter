import string,random
from wonderwords import RandomWord

word_generator = RandomWord()
the_word = word_generator.word()

clue_list=list('?'*len(the_word))
print(clue_list)
whole_letters =string.ascii_letters
print(whole_letters)

print("\u2764\ufe0f")

word = mirror
clu = ['?','?','?','?','?','?']
while True:
    guess= input('guess you letter ')

    for i,l in enumerate(word):
        ln= word.count(l)
        for i in range(ln):
