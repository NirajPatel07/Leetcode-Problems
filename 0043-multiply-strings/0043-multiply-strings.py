class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        first_num=0
        second_num=0
        for i in num1:
            first_num=(first_num*10)+d[i]
        for i in num2:
            second_num=(second_num*10)+d[i]
        return str(first_num*second_num)