import math
import sys

##### VOWPAL WABBIT OUTPUT FIRST THEN NEW CSV

def zygmoid(x):
    #I know it's a common Sigmoid feature, but that's why I probably found
    #it on FastML too: https://github.com/zygmuntz/kaggle-stackoverflow/blob/master/sigmoid_mc.py
    return 1 / (1 + math.exp(-x))

with open(sys.argv[2],"wb") as outfile:
    outfile.write("IsClick\n")
    for line in open(sys.argv[1]):
        row = line.strip().split(" ")
        outfile.write("%f\n"%(zygmoid(float(row[0]))))
