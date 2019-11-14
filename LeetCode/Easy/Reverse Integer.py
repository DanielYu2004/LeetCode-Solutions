class Solution(object):
    def reverse(self, x):
        y = []
        counter = 0
        negative = False
        num = len(str(x))
        for i in range(num):
            y.append(str(x)[num-i-1])
        print("hi" + y[num-1])
        while(y[num - 1] == "-"):
            counter = counter + 1

            if y[num-1] == "-":
                negative = True
            num = num - 1
        counter = counter * -1
        if counter != 0:
            y = y[:counter]
        print(negative)
        reverse_num = "".join(y).lstrip("0")
        print(reverse_num)
        if reverse_num:
            if int(reverse_num) > 2**31:
                return(0)
        if negative:
            return("-" + "".join(reverse_num)) 
        else:
            if reverse_num:
                return("".join(reverse_num))
                
            else: 
                return(0)

