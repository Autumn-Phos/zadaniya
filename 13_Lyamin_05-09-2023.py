words = input("vveditepredlojenie \n");

yes = False;

for i in range(len (words)):
    if (words[i] == ')'):
        yes = False;
    
    if (yes):
        print(words[i], end='');
    
    if (words[i] == '('):
        yes = True;   