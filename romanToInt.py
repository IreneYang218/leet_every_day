def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        for i,elem in enumerate(s):
            if elem == 'M':
                integer += 1000
            if elem == 'D':
                integer += 500
            if elem == 'C':
                if i < (len(s) - 1):
                    if s[i+1] in ['D', 'M']:
                        integer -= 100
                    else:
                        integer += 100
                else:
                        integer += 100
            if elem == 'L':
                integer += 50
            if elem == 'X':
                if i < (len(s) - 1):
                    if s[i+1] in ['L', 'C']:
                        integer -= 10
                    else:
                         integer += 10
                else:
                         integer += 10
            if elem == 'V':
                integer += 5
            if elem == 'I':
                if i < (len(s) - 1):
                    if s[i+1] in ['V', 'X']:
                        integer -= 1
                    else:
                        integer += 1
                else:
                        integer += 1
        return integer

def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToNum = {'M':1000,'D':500,'C':100,'L':50, 'X':10,'V':5,'I':1}
        output = 0        
        prev = 0
    
        for romanLetter in s:
            cur = romanToNum[romanLetter]
            output += cur
            if prev < cur:  output -= prev * 2

            prev = cur
            
        
        return output