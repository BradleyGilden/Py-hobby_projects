import os
import platform

phase1 = '''            +----+
            |    |
            |    |
            O    |
           /|\   |
           / \   |
                 |
        ==========
'''
phase2 = '''            +----+
            |    |
            |    |
            O    |
           /|\   |
           /     |
                 |
        ==========
'''
phase3 = '''            +----+
            |    |
            |    |
            O    |
           /|\   |
                 |
                 |
        ==========
'''
phase4 = '''            +----+
            |    |
            |    |
            O    |
           /|    |
                 |
                 |
        ==========
'''
phase5 = '''            +----+
            |    |
            |    |
            O    |
            |    |
                 |
                 |
        ==========
'''
phase6 = '''            +----+
            |    |
            |    |
            O    |
                 |
                 |
                 |
        ==========
'''
phase7 = '''            +----+
            |    |
            |    |
                 |
                 |
                 |
                 |
        ==========
'''
phases = [phase2, phase3, phase4, phase5, phase6, phase7]

sentence = ""
copy = ""
car = ""
idx = 0
wordlist = []
i = 0
count = 0
temp = 0

while len(sentence) < 13:
    sentence = input("Enter a sentence that is 13 characters or more: ")
    if len(sentence) < 13:
        print("Try again.", end = " ")

copy = sentence

while i < len(sentence):
    if i % 2 == 0:
        pass
    else:
        wordlist.append(sentence[i])
        sentence = sentence.replace(sentence[i], '_')
        count += 1
    i += 1


if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')
print(phase1)
print("\t" + sentence)


while count > 0:
    car = input()
    if car[0] in wordlist:
        for temp in range(len(sentence)):
            listedstr = list(sentence)
            if copy[temp] == car[0]:
                listedstr[temp] = copy[temp]
                sentence = "".join(listedstr)
        count -= 1
        wordlist.remove(car[0])
    else:
        print(phases[idx])
        idx += 1
    if idx == 6:
        break
    print("\t" + sentence)

print()
if count == 0 and copy == sentence:
    print("Congratulations you won")
else:
    print("You Lost")
