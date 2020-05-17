class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        mat_trp = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
        for in1 in matrix:
            a = in1.index(min(in1))
            if max(mat_trp[a]) == min(in1):
                result.append(min(in1))

        return result
