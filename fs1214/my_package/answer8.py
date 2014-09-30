'''
Created on Sep 29, 2014

@author: ds-ga-1007

'''
def main():
    di = {'first':[2, 1], 'second':[2, 3], 'third':[3, 4]}
    #a
    li = di['first']
    di['first'] = di['third']
    di['third'] = li
    #b
    di['third'].sort()
    #c
    di['fourth'] = di['second']
    #d
    del di['second']
    print di
if __name__ == '__main__':
    main()
    
    
    