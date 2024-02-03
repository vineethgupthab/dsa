class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=x;count=0;num=0
        if i>0:
            while i>=10:
                if count==0:
                    num=i%10
                    i = int(i/10)
                    count+=1
                else:
                    num=num*10+(i%10)
                    i=int(i/10)
            num=num*10+i
            if x==num:
                return True
            else:
                return False
        elif i>=0 and i<10:
            return True
        else:
            return False