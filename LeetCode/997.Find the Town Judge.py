from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
          return 1 
        identity_list = [0 for i in range(n)]
        relationship_dict = {}
        
        for relationship in trust:
            give, take = relationship
            if relationship_dict.get(take):
              relationship_dict[take].append(give)
            else:  
              relationship_dict[take] = [give]
            if identity_list[give - 1] == 0:
              identity_list[give - 1] = -1
        
        
        judge = -1
        for person in relationship_dict.keys():
          if identity_list[person - 1] == 0 and len(relationship_dict[person]) == (n - 1):
            return person
        return judge
        
a = Solution()
# b = a.findJudge(2,[[1,2]])
# b = a.findJudge(3, [[1,3],[2,3]])
b = a.findJudge(3, [[1,3],[2,3],[3,1]])
print(b)