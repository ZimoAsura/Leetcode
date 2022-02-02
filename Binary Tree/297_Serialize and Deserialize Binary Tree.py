class Codec:
    # 前中后三种遍历在这道题里面都可以，因为会记录空节点
    def serialize(self, root):
        if not root: return '#,'
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
    
    def deserialize(self, data):
        data = data.split(',')[::-1]
        return self.getNode(data)
    
    def getNode(self, data):
        if not data: return None
        val = data.pop()
        if val=='#': return None
        node = TreeNode(val)
        node.left = self.getNode(data)
        node.right = self.getNode(data)
        return node