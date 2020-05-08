class Solution:
    def countBits(self, num: int) -> List[int]:
        # values: 0 1 1 2 1 2 2 3 1 2 2  3  2  3  3  4  1  2  2  3  2  3  3  4  2  3  3  4  3  4  4  5  1
        # nums:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
        
        values = [0] * (num + 1)

        for i in range(1, num+1):
            val = values[int(i/2)] + i % 2
            values[i] = val
            
        return values
            
