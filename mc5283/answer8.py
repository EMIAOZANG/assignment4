import os

if __name__ == "__main__":

    d = {'first':[2,1], 'second':[2,3], 'third': [3,4]}
#a.# 
    d['first'] = [3,4]
    d['third'] = [2,1]
#b.#
    d['third'].sort()
#c.#
    d['fourth'] = d['second']
#d.#
    del d['second']

    print d
    


