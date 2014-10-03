'''
Created on Sep 30, 2014

@author: ds-ga-1007
'''
def main():
    d={'first':[2,1],'second':[2,3],'third':[3,4]}
    t=d['first']
    d['first']=d['third']
    d['third']=t
    d['third'].sort()
    d['fourth']=d['second']
    del d['second']
    print d
if __name__ == '__main__':
    main()
    