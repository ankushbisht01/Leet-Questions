class Solution(object):
    def average(self, salary):
        min = 10000000
        max = 999
        sum = 0 
        for i in salary:
            sum +=i 
            if (i < min):
                min = i
            if (i > max):
                max = i 
        sum = sum - min - max
        average = sum*1.0 / (len(salary)-2)
        return average 
        