import numpy as np
import math

class fontMap:        
    
    
    def __init__(self):
        ###CHANGE THIS TO YOUR FILE PATH ON YOUR COMPUTER
        fontMap.f = open("C:/Users/Akshay/R3ND3R3R/fonts/stripped_text.txt", "r", encoding='utf-8-sig') 
        self.font_map = {}
        self.create_arrays()
        self.sorted_keys = list(self.font_map.keys())
        self.sorted_keys.sort()
    
    #Creates a 2d array with each array containing an 8x16 representation of a glyph
    def create_arrays(self):
        cur_letter = []
        count = 0
        while True:
            count += 1
            x = self.f.readline().strip()
            if (count > 16):
                key = self.__find_intensity(cur_letter)
                self.font_map[key] = cur_letter
                count = 1
                cur_letter = []
            if (len(x) == 0):
                break
            else:
                for i in x:
                    if (i == '.'):
                        cur_letter.append(0)
                    elif (i == '@'):
                        cur_letter.append(1)
        self.__verify(self.font_map)

        return self.font_map
    
    def find_glyph(self, intensity):
        ar = np.asarray(self.sorted_keys)
        print(ar)
        index = np.searchsorted(ar, intensity, side="left")
        if index > 0 and (index == len(ar) or math.fabs(intensity - ar[index-1] < math.fabs(intensity - ar[index]))):
            return self.font_map[ar[index-1]]
        else:
            return self.font_map[ar[index]]

            
    def __verify(self, i):
        for j in i.values():
            if (len(j) != 128):
                raise TypeError("glyph incorrect dimensions")

    def __find_intensity(self, arr):
        
        sum = 0.0
        
        for i in arr:
            sum += i
        return sum/len(arr)
#s = fontMap()
#print(s.find_glyph(0.4))