"""
This code is written for education
Naive implementation of the algorithm

Algorithm2: Merge Sort
"""
import pandas as pd

def main():

    # Read input .txt file
    data = pd.read_csv('./input.csv')
    data = list(map(int, data.columns))
    print(data)
    merge_sort(data)


def merge_sort(arry):

    if len(arry) <= 1:
        return arry
    else:
        # divide into two list
        n = len(arry)
        L = arry[0:int(n/2)]
        R = arry[int(n/2):]
        print(L, R)
        # get sorted array
        L_sorted = merge_sort(L)
        R_sorted = merge_sort(R)


        # merge - two fingers merge
        L_finger = 0
        R_finger = 0
        sorted_arry = []
        for i in range(len(L_sorted)+len(R_sorted)):

            if L_finger < len(L_sorted) and R_finger < len(R_sorted) and L_sorted[L_finger] > R_sorted[R_finger]:
                sorted_arry.append(R_sorted[R_finger])
                R_finger += 1

            elif L_finger < len(L_sorted) and R_finger < len(R_sorted) and L_sorted[L_finger] < R_sorted[R_finger]:
                sorted_arry.append(L_sorted[L_finger])
                L_finger += 1

            elif L_finger >= len(L_sorted):
                sorted_arry.append(R_sorted[R_finger])
                R_finger += 1

            elif R_finger >= len(R_sorted):
                sorted_arry.append(L_sorted[L_finger])
                L_finger += 1

        print(sorted_arry)
        return sorted_arry


if __name__ == '__main__':
    main()
