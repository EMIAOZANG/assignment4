def main():

    # create the starting dictionary
    dictionary = {'first': [2, 1], 'second': [2, 3], 'third': [3, 4]}

    # swap the values of first and third
    dictionary['first'], dictionary['third'] = dictionary['third'], dictionary['first']

    # sort the elements of the list with key third
    dictionary['third'].sort()

    # add a new key fourth
    dictionary['fourth'] = dictionary['second']
    
    # delete key/value pair second
    del dictionary['second']

    # print the result
    print dictionary

if __name__ == '__main__':
    main()
    
