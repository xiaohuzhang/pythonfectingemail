class basealgo(object):
    def __init__ (self,array):
        self.myarray=array
        
        
    def findmax(self):
        maxhold=0
        for i in self.myarray:
            if maxhold< i:
                maxhold=i
        return i

    def printout(self):
        self.max=self.findmax();
        print self.max
        
def fibonacci(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)

print fibonacci(4)    
    
def fibonaccinorecursion(n):
        a,b=1,1
        for i in range(n-1):
            a,b=b,b+a
        return a
    
print fibonaccinorecursion(4)

def selection_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    for i in range(iter_len-1):
        smallest = sort_list[i]
        location = i
        for j in range(i+1, iter_len):
            if sort_list[j] < smallest: 
                smallest = sort_list[j]
                location = j
        if i != location:
            sort_list[i], sort_list[location] = sort_list[location], sort_list[i]
    return sort_list

#buddle sort
def buddle_sort(myarray):
    length=len(myarray)    
    print length 
    for i in range(length-1):# python array is by default like the c++ array starts from 0 to lenth-1
        for j in range(length-i-1):
            if myarray[j] > myarray[j+1]:
                myarray[j+1],myarray[j]=myarray[j],myarray[j+1]
    return myarray

arraya=[0,4,2,4,2,1]
print arraya
sorta=buddle_sort(arraya)
print sorta
selectionsort=selection_sort(arraya)
print selectionsort