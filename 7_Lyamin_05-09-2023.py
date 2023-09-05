words = input("vveditePredlojenie \n");
for i in range(int(len (words))):
    if (words[i] == 'п' and len (words) / 2 > i):
        print('*', end='');
    else:
        print(words[i], end='');