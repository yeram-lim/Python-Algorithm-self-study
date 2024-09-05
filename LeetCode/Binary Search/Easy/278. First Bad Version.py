# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
  # 리트코드에서 제공하는 API
  return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        first_bad_version = n
        while start < end:
            next_pointer = (start + end) // 2
            if next_pointer == start or next_pointer == end:
                if isBadVersion(start):
                    first_bad_version = start
                break
            is_next_bad = isBadVersion(next_pointer)
            if is_next_bad:
                end = next_pointer
                first_bad_version = next_pointer
            else:
                start = next_pointer
        return first_bad_version
        