"""
This code is written for education
Naive implementation of the algorithm

Algorithm1: Insertion Sort
"""
import pandas as pd

def main():

    # Read input .txt file
    data = pd.read_csv('./input.csv')
    data = list(map(int, data.columns))

    # Insertion sort O(n^2)
    # iterate for key
    # O(n) for this loop
    for key in range(0,len(data)):
        # resort for "key" value with sorted array data[0:key]
        # O(n) for this operation
        pairwise_sort(data, key)
        print(key,data)

    # Overall algorithm complexity is O(n^2)


def pairwise_sort(arry, key):

    # target value is on the end of list
    val = arry[key]
    for target in list(reversed(range(0,key))):
        if arry[target] > val:
            arry[target+1] = arry[target]
            arry[target] = val
        else:
            return

if __name__ == '__main__':
    main()
