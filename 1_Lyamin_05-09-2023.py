wordRussLetter = input();

a = 0;

if (wordRussLetter[0] == 'е'):
    a += 1;

for i in range(len(wordRussLetter)):
    if ((wordRussLetter[i] == ' ' and wordRussLetter[i+1] == 'е')):
        a += 1;

print(a);