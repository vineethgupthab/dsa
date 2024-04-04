class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def is_divisor(divisor, string):
            return all(string[i:i+len(divisor)] == divisor for i in range(0, len(string), len(divisor)))

        gcd_len = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_len]

        if is_divisor(gcd_str, str1) and is_divisor(gcd_str, str2):
            return gcd_str
        else:
            return ""
