# write your solution here
with open("wordlist.txt") as file:
    vocab = file.read()
    vocab = vocab.split()


text = input("Write text: ")
text = text.split()
answ = ""
for word in text:
    flag = True
    for word_vocab in vocab:
        if word.lower() == word_vocab.lower():
            answ += word + " "
            flag = False
    if flag:
        answ += "*" + word + "* "
print(answ[:len(answ) - 1])
