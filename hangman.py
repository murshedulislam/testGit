import random
strs = ["strange","abate","umbrella","hanging","science"]
s = strs[random.randint(0,3)]
k = ''
for i in range(0, 5, 2):
    k = k + s[i]
#z = k
li = []
li.extend(s)
li2 = []
m = 0
"""replacing all the missing letters with '_'"""
for i in k:

    s = s.replace(i, '_')
    m= m + 1
li2.extend(s)
#print(s)
#print(z)
count = 3
print('\nYou got : {}\n'.format(s))
print('You have {} guesses to win the game.\n'.format(count))

while count > 0:
    if len(k) == 0:
        print("\nCongratulations! You won.")
        break

    x = input("Guess a letter : ")

    if x in k:
        li3 = [i for i, e in enumerate(li) if e == x]#find the indexes of the guessed letter from the original word
        for i in range(len(li3)):
            li2[li3[i]] = x#replace the '_' with the correct guessed letter
        k = k.replace(x, '')#remove the already correct guessed letter from the missing letters list
        print("\nLetter {} is correct.\n".format(x))
        print(''.join(li2))
        print('\n')


    else:
        print("\nNope {} is not one of the missing letters.\n".format(x))
        print(''.join(li2))
        count = count -1
        if count > 0:
            print("\nYou have {} guesses left.\n".format(count))
if count == 0:
    print("\nYou lost.")
