from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        currentIndex = 2
        resultList = [1, 1]
        while rowIndex >= currentIndex:
            tempList = list()
            tempList.append(1)
            for index in range(len(resultList)):
                if index == 0:
                    continue
                value = resultList[index] + resultList[index - 1]
                tempList.append(value)
            tempList.append(1)
            resultList = tempList
            rowIndex = rowIndex - 1
        return resultList
