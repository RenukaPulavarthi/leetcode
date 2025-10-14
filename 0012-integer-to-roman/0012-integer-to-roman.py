class Solution:
    def intToRoman(self, num: int) -> str:
        nums_map = {1000 :'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ""
        for i in nums_map:
            # print(i, num)
            if i <= num:
                z = num // i
                # print(nums_map[i])
                ans += (nums_map[i] * z)
                num = num % i
        return ans

            

