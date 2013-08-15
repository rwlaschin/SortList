import HeapSort
import QuickSort

import random
import cProfile
import timeit

        
# create test
mytests = [ range(0,100),
          range(100,0,-1),
          range(50,0-1) + range(0,50),
          [ random.randint(0,999) for i in range(0,100) ],
          [ random.randint(0,999) for i in range(0,100) ],
          [ random.randint(0,999) for i in range(0,100) ],
          [ random.randint(0,999) for i in range(0,100) ],
          [ random.randint(0,999) for i in range(0,100) ]]

def runheaptests(tests=mytests):
    for l0 in tests:
        HeapSort.heapsort(l0)

def runquicktests(tests=mytests):
    for l0 in tests:
        QuickSort.quickSort(l0,0,len(l0)-1)
        
if __name__ == "__main__":
    #cProfile.run("runheaptests()")
    #cProfile.run("runquicktests()")
    
    t = timeit.Timer("runheaptests()","from __main__ import runheaptests")
    print(t.timeit())
    
    t = timeit.Timer("runquicktests()","from __main__ import runquicktests")
    print(t.timeit())
    pass
