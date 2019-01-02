cases = [[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]]

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        for i in range(m):
            A[i] = A[i][::-1]
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

def main():
    s = Solution()
    for c in cases:
        print(s.flipAndInvertImage(c))

if __name__ == '__main__':
    main()
