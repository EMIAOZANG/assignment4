import sys


def main():
    a = {'first': [2, 1], 'second': [2, 3], 'third': [3, 4]}
    temp = a['first']
    a['first'] = a['third']
    a['third'] = temp
    a['third'].sort()
    a['forth'] = a['second']
    del a['second']
    print a
