# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
          return None

        # 해당 root가 p거나 q라면 해당 노드가 lca이다
        if root == p or root == q:
          return root
        
        # 좌측 서브트리를 재귀탐색(Recursion search) -> lca 반환
        left = self.lowestCommonAncestor(root.left, p, q)
        # 우측 서브트리를 재귀탐색
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 좌측, 우측 노드 모두 해당 방향 서브트리의 lca라는 것은
        # 현재 root가 p, q의 lca라는 것
        if left and right:
          return root
        
        # 둘 중 lca인 것을 반환
        return left if left else right