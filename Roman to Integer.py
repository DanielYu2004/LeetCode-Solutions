class Solution(object):
    def romanToInt(self, s):
        integer_sum = int(0)


        for i in range(len(s)):
            if i == len(s)-1:
                if s[i] == "I":
                    return(integer_sum + 1)
                if s[i] == "V":
                    return(integer_sum + 5)
                if s[i] == "X":
                    return(integer_sum + 10)
                if s[i] == "L":
                    return(integer_sum + 50)
                if s[i] == "C":
                    return(integer_sum + 100)
                if s[i] == "D":
                    return(integer_sum + 500)
                if s[i] == "M":
                    return(integer_sum + 1000)

            next = s[i+1]
            cur = s[i]
            
            if cur == "I" and (next == "V" or next == "X"):
                integer_sum -= 1
            elif cur == "I":
                integer_sum += 1
            if cur == "X" and (next == "L" or next == "C"):
                integer_sum -= 10
            elif cur == "X":
                integer_sum += 10
            if cur == "C" and (next == "D" or next == "M"):
                integer_sum -= 100
            elif cur == "C":
                integer_sum += 100
                
            if cur == "V":
                integer_sum += 5
            if cur == "L":
                integer_sum += 50
            if cur == "D":
                integer_sum += 500
            if cur == "M":
                integer_sum += 1000

        return(integer_sum)
