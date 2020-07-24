class Solution(object):
    def destCity(self, paths):
        
        start= []
        dest = []
        
        for a,b in paths:
            start.append(a)
            dest.append(b)
            
        for i in dest:
            if i not in start:
                return i
        