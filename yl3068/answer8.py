#This program is for assignment 4_8

def main():
    d = {'first':[2,1],'second':[2,3],'third':[3,4]}

    #swap the values of the first and third keys

    d['first'], d['third'] = d['third'], d['first']

    #sort the elements of key third
    
    d['third'].sort()

    #add a new key fourth with the value of the key second
    
    d['fourth'] = d['second']

    #delete the key/value pair second

    del d['second']

    #print final dictionary

    print d

if __name__ == '__main__':
    main()



