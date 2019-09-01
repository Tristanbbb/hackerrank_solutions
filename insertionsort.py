#!/bin/python
def insertionSort(ar):
    lastItemIndex=len(ar)-1
    temp=ar[lastItemIndex]
    sorted=False
    cpt=lastItemIndex-1
    while(sorted==False):
        #print "temp = %d" % temp
        if(ar[cpt]>temp and cpt>=0):
            ar[cpt+1]=ar[cpt]
        else:
            #print 'cpt+1 = %d' % (cpt+1)
            ar[cpt+1]=temp
            sorted=True
        cpt -= 1
        #print(ar)
        for i in range(len(ar)):
            print '%d' % ar[i],
        print ""
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
