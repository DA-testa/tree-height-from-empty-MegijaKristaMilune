import sys
import threading
import numpy



def compute_height(n, parents):
    h = numpy.zeros(n)
    maxh = -1


    for i in range (len(parents)):
        l = i
        h_i = 1



        while parents[l] != -1 :
            if h[l] != 0 :
                h_i += h[l] - 1
                break
            

            h_i += 1

            l = parents[l]

        h[i] = h_i
        maxh = max(maxh, h[i])
    
    return maxh


def main():
    
    input_text = input()

    if 'F' in input_text:
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



sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()