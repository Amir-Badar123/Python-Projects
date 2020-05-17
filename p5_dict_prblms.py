# "abcbcbca"
# {'a': 2, 'b' : 3, 'c' : 3}

# from list_input import int_input, str_input

import sys

def max_freq(d):
    print(d)
    maxm_freq = - sys.maxsize - 1
    max_elem = ''
    for i in d : 
        if d[i] > maxm_freq:
            maxm_freq = d[i]
            max_elem = i
    return max_elem, maxm_freq

def str_freq(s):
    d = {}
    for i in s:
        if i not in d: # if i in d.keys()
            d[i] = 1
        else:
            d[i] += 1
        # print(d)
    return d

if __name__ == '__main__':
    print(max_freq(str_freq(input("Enter a string : "))))