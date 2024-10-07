func searchBST(root *TreeNode, val int) *TreeNode {
	switch {
  case root == nil:
    return nil
	case root.Val == val:
		return root
	case root.Val < val:
		return searchBST(root.Right, val)
	case root.Val > val:
		return searchBST(root.Left, val)
	}
	return nil
}
