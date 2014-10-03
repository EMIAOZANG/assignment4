'''


@author: jiminzi
'''

def answer8():
    dictionary = {'first': [2,1],'second':[2,3],'third':[3,4]}
# swap first and  third
    a=dictionary['first']
    dictionary['first']=dictionary['third']
    dictionary['third']=a
# sort the number in third
    dictionary['third'].sort()
#copy second  as 'fourth'
    dictionary['fourth']=dictionary['second']
    del dictionary['second']

    print dictionary
if __name__ == '__main__':
    answer8()