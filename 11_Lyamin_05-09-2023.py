from itertools import groupby

def longest_sequence(s):
    counter = 0;
    oldcounter = 0;
    for i in range(len (s)):
        if (s[i] == 'н'):
            counter += 1;
        print(counter)
        if oldcounter <= counter:
            oldcounter = counter;
        if (s[i] != 'н' and s[i-1] == 'н'):
            counter = 0;
        
    return oldcounter, s.replace('!','.');

print(longest_sequence(input()));