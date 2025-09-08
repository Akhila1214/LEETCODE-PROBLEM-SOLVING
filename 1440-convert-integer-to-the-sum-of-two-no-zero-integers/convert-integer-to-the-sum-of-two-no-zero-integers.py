class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(a, b):
            if '0' in a or '0' in b:
                return False
            return True
        for i in range(1, n):
            a = i
            b = n - i
            if check(str(a), str(b)):
                return [i, n- i]