from typing import *
import math

class Solution:
    def get_angle(self, origin, v):
        v1 = [v[0] - origin[0], v[1] - origin[1]]
        norm = math.sqrt(v1[0]**2 + v1[1]**2)
        x = v1[0] / norm
        y = v1[1] / norm
        if x == 0:
            angle = math.pi / 2
        else:
            angle = math.atan(y / x)
        return round(angle, 10)        
        
    def maxPoints(self, points: List[List[int]]) -> int: 
        if len(points) == 1:
            return 1
        max_val = 0
        #Translate to make every point the origin,
        #and then project every point onto a unit circle and compute the arctan
        #All points on the same line will have the same arctan value
        for i1 in range(len(points)):
            lines = {}
            for i2 in range(i1+1, len(points)):                
                angle = self.get_angle(points[i1], points[i2])
                if angle not in lines:
                    lines[angle] = 1
                lines[angle] += 1
                if lines[angle] > max_val:
                    max_val = lines[angle]
        
        return max_val