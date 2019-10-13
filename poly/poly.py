#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt


class polygon:
    poly = list()
    def __init__(self):
        self.poly.append([100.0,200.0])
        self.poly.append([100.0,300.0])
        self.poly.append([200.0,300.0])
        self.poly.append([200.0,200.0])
        self.poly.append([100.0,200.0]) #for calculation

        print("polygon : ")
        print(self.poly)

        #pts1 = np.float32([[0,0],[140,0],[0,70]])
    
    
    def calc_cn(self, check_point=[0.0,0.0]):
        print("check_point:" + str(check_point))
        check_x = check_point[0]
        check_y = check_point[1]

        for point in range(len(self.poly)-1):
            print("loop:" + str(point))
            now_pos_x = self.poly[point][0]
            now_pos_y = self.poly[point][1]
            print("now x=" + str(now_pos_x))
            print("now y=" + str(now_pos_y))
            next_pos_x = self.poly[point+1][0]
            next_pos_y = self.poly[point+1][1]
            print("next x=" + str(next_pos_x))
            print("next y=" + str(next_pos_y))
            rule_1 = (now_pos_y <= check_y) and (next_pos_y > check_y)
            print("ruler_1 : " + str(rule_1))
            rule_2 = (now_pos_y < check_y) and (next_pos_y <= check_y)
            print("ruler_2 : " + str(rule_2))
            if rule_1 and rule_2:
                vt = (check_y - now_pos_y) / (next_pos_y - now_pos_y)
                target_x = vt * (next_pos_x - now_pos_x) + now_pos_x
                print("target_x=" + str(target_x))
                rule_3 = check_x < target_x
                print("rule_3 : " + str(rule_3))
            else:
                print("rule_3 is not evaluated")


def main(args):
    print("main start")
    ply = polygon()
    print("calc cn")
    ply.calc_cn()


if __name__ == '__main__':
    main(sys.argv)
    print("end!")