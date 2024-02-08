def equalPairs(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # result = 0
        # rows = []
        # cols = []

        # for i in range(len(grid)):
        #     l = "".join(map(str, grid[i]))
        #     rows.append("".join(l))

        # for i in range(len(grid)):
        #     temp = ""
        #     for j in range(len(grid)):
        #         temp += str(grid[j][i])
        #     cols.append(temp)

        #     if temp in rows:
        #         multi = rows.count(temp)
        #         result += multi

        
        # return result
        
        result = 0

        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            if temp in grid: 
                multi = grid.count(temp)
                result += multi
        return result

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))