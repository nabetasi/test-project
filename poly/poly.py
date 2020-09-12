#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt


class polygon:
    def __init__(self):

        self.poly = list()
        self.poly.append([100.0,200.0])
        self.poly.append([100.0,300.0])
        self.poly.append([200.0,300.0])
        self.poly.append([200.0,200.0])
        self.poly.append([100.0,200.0]) #for calculation

        print("polygon : ")
        print(self.poly)

        #pts1 = np.float32([[0,0],[140,0],[0,70]])
    
    
    def calc_cn(self, check_point=[90.0,250.0]):
        print("check_point:" + str(check_point))
        check_x = check_point[0]
        check_y = check_point[1]

        cn = 0

        for point in range(len(self.poly)-1):
            #print("loop:" + str(point))
            now_pos_x = self.poly[point][0]
            now_pos_y = self.poly[point][1]
            #print("now x=" + str(now_pos_x))
            #print("now y=" + str(now_pos_y))
            next_pos_x = self.poly[point+1][0]
            next_pos_y = self.poly[point+1][1]
            #print("next x=" + str(next_pos_x))
            #print("next y=" + str(next_pos_y))
            rule_1 = (now_pos_y <= check_y) and (next_pos_y > check_y)
            #print("ruler_1 : " + str(rule_1))
            rule_2 = (now_pos_y > check_y) and (next_pos_y <= check_y)
            #print("ruler_2 : " + str(rule_2))
            if rule_1 or rule_2:
                vt = (check_y - now_pos_y) / (next_pos_y - now_pos_y)
                target_x = vt * (next_pos_x - now_pos_x) + now_pos_x
                #print("target_x=" + str(target_x))
                rule_3 = check_x < target_x
                #print("rule_3 : " + str(rule_3))
                if rule_3: cn += 1
            #else:
                #print("rule_3 is not evaluated")
        #print("cn = " + str(cn))
        return cn

    def is_in_polygon(self, check_point=[0.0,0.0]):
        cn = self.calc_cn(check_point)
        if cn % 2 == 0:
            print("Out polygon")
            return False
        else:
            print("In polygon")
            return True


def main(args):
    print("main start")
    ply = polygon()
    print("calc cn")
    check = ply.is_in_polygon([0.0,0.0])
    print("point1 is : " + str(check))
    check = ply.is_in_polygon([150.0,250.0])
    print("point2 is : " + str(check))
    check = ply.is_in_polygon([300.0,250.0])
    print("point3 is : " + str(check))
    check = ply.is_in_polygon([101.0,200.0])
    print("point4 is : " + str(check))
    
    print("Turn 2")
    ply = polygon()
    print("calc cn")
    check = ply.is_in_polygon([0.0,0.0])
    print("point1 is : " + str(check))
    check = ply.is_in_polygon([150.0,250.0])
    print("point2 is : " + str(check))
    check = ply.is_in_polygon([300.0,250.0])
    print("point3 is : " + str(check))
    check = ply.is_in_polygon([101.0,200.0])
    print("point4 is : " + str(check))


if __name__ == '__main__':
    main(sys.argv)
    print("end!")
