
if __name__ == '__main__':
    dic = {'first':[2,1],'second':[2,3],'third':[3,4]}
    temp = dic['third']
    temp = dic['first']
    dic['first'] = dic['third']
    dic['third'] = temp
    dic['third'].sort()
    dic['fourth'] = dic['second']
    del dic['second']
    print dic
