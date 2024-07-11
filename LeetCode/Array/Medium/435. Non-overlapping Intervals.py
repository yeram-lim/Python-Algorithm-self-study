from typing import List

intervals = [[1,2],[2,3],[3,4],[1,3]]

#if sort
# intervals = [[1,2],[2,3],[1,3],[3,4]]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
          return 0
        
        intervals.sort(key=lambda x : x[1])
        
        previous_end = intervals[0][1]
        removed_cout = 0
        
        
        for interval in intervals[1:]:
          current_start = interval[0]
          if previous_end < current_start:
            removed_cout += 1
          else:
            previous_end = interval[1]
            
a=Solution()
a.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])