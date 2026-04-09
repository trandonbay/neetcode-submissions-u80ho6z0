class Solution:
    def countBits(self, n: int) -> List[int]:

        def numOneBits(num):
            bits = 0
            while num:
                num &= num - 1
                bits += 1
            return bits

        res = []
        for i in range(n+1):
            res.append(numOneBits(i))

        return res