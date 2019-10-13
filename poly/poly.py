#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt


class polygon:
    poly = list()
    def __init__(self):
        self.poly.append([100,200])
        self.poly.append([100,300])
        self.poly.append([200,300])
        self.poly.append([200,200])

        print("polygon : ")
        print(self.poly)

        #pts1 = np.float32([[0,0],[140,0],[0,70]])
    
    
    def calc_cn(self):
        #for edge in polygon.length:
        print(self.poly)


def main(args):
    print("main start")
    ply = polygon()
    print("calc cn")
    ply.calc_cn()


if __name__ == '__main__':
    main(sys.argv)
    print("end!")