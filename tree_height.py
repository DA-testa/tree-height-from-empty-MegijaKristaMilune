# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height
    
    h = numpy.zeros(n)
    maxh = -1


    for i in range (len(parents)):
        l = i
        h_i = 1

        while parents[l] != -1:
            if h[l] != 0:
                h_i += h[l] - 1
                break

            h_i += 1

            l = parents[l]

        h[i] = h_i
        maxh = max(maxh, h[i])


    return maxh




def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    input_type = input()

    if 'F' in input:
        input_file = input()
        input_file = "test/" + input_file
        
        
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    print(compute_height(n, parents))

            except FileNotFoundError:
                return print("not found")

    if 'I' in input_text:
        n = int(input())
        parents = list(map(int, input().split()))

        print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
