def maxDepth_v2(root):
        """
        """
        left_depth = 0
        right_depth = 0
        # 
        if root.left:
            left_depth = maxDepth_v2(root.left)
        # 
        if root.right:
            right_depth = maxDepth_v2(root.right)
        # 
        return max(right_depth, left_depth) + 1


def maxDepth(root):
    """
    """
    if not root:
        return 0
    # 
    left_depth = 0
    right_depth = 0
    # 
    if root.left:
        left_depth = maxDepth_v2(root.left)
    # 
    if root.right:
        right_depth = maxDepth_v2(root.right)
    # 
    return max(right_depth, left_depth) + 1

# -------------------------------------------------------------------------------------------------