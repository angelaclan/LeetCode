class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        convertedNum = str(x)
        if len(convertedNum) > 5 : 
            print "out of range"
        if convertedNum[0] == '-' :
            newx = abs(x)
            res = str(newx)
            reverseres = res[::-1]
            reverseres = int(reverseres) *-1
            if str(reverseres)[0] == '0' :
                reverseres = reverseres[:1] + reverseres[3:]    
            return reverseres
        
        temp = convertedNum[::-1]
        if  temp[0] == '0':
            temp = temp[:0] + temp[1:]
            return temp
        if x == 0 :
            return 0
        return convertedNum[::-1]