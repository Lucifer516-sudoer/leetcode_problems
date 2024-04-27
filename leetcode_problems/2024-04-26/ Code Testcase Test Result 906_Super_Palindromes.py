# class Solution:
#     def superpalindromesInRange(self, left: str, right: str) -> int:
#         if not left <= right:
#             raise Exception
        
class Solution:
    def superpalindromesInRange(self, left, right):
        l, r, self.ans = int(left) ** 0.5, int(right) ** 0.5, 0
        def helper(s):
            if len(s) < 5:
                for d in '012': 
                    helper(s + d)
            elif s != '0' * 5:
                left = str(int(s))
                coeff = 2 * sum(int(x) ** 2 for x in left)
                if coeff < 10 and l <= int(left + left[::-1]) <= r:
                    self.ans += 1
                coeff -= int(left[-1]) ** 2
                if coeff < 10 and l <= int(left + left[-2::-1]) <= r:
                    self.ans += 1
            return self.ans
        return helper('') + (l <= 3 <= r)
s = Solution()
print(s.superpalindromesInRange(1, 10**18 ))
# from meidum website
    