words = input("vveditepredlojenie \n").split(' ');

for i in range(len (words)):
    if (words[i][len (words[i])-1] == 'я' or words[i][0] == 'а'):
        print(words[i]);