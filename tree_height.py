import sys
import threading
import numpy



def compute_height(n, par):
    h = numpy.zeros(n)
    maxh = -1


    for i in range (len(par)):
        l = i
        h_i = 1



        while par[l] != -1:
            if h[l] != 0:
                h_i += h[l] - 1
                
                break
            

            h_i += 1

            l = par[l]

        h[i] = h_i
        maxh = max(maxh, h[i])
    
    return maxh


def main():
    
    txt = input()

    if 'F' in txt:
        file = input()
        file = "test/" + file
        if 'a' not in file:
            
            try:
                with open(file, "r") as f:
                    n = int(f.readline())
                    par = list(map(int, f.readline().split()))
                    print(compute_height(n, par))

            except FileNotFoundError:
                return print("not found")

    if 'I' in input_text:
        n = int(input())
        par = list(map(int, input().split()))
        print(compute_height(n, par))



sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()