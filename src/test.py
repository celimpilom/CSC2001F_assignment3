import os
import random

def openList(arr):
    with open("testout.txt", 'r') as f:
        
        temp = f.readlines()
        temp_arr = temp[1].split(" ")
        if (temp_arr[2] == "Not"):
            collisions = int(temp_arr[6])
            if collisions<5:
                print(arr, "collisions:", collisions)
            

        f.close()


weights = [1,2,3,4,5,6,7,8,9]

for a in range(0,5):
    weights[0]=a
    for b in range(0,5):
     weights[1]=b
     for c in range(0,5):
        weights[2]=c
        for d in range(0,5):
            weights[3]=d
            for e in range(0,5):
                weights[4]=e
                for f in range(0,5):
                    weights[5]=f
                    for g in range(0,5):
                        weights[6]=g
                        for h in range(0,5):
                            weights[7]=h
                            for i in range(0,5):
                                weights[8]=i
                                os.system(f"java -cp bin TestHashTable {0} {a} {b} {c} {d} {e} {f} {g} {h} {i} > testout.txt")
                                # read the file, check if collision is 0 or probably less than 5
                                # if so, print weights to a file, with it's collision number (append to a file)
                                openList(weights)
