import hou

class NodeTree():
    def __init__(self, node, find_head=False):
        if find_head:
            self.head = self._find_head(node)
        else:
            self.head = node
        self.tail = self._find_tail(node)

    def _find_head(self, node):
        while len(node.inputs()) > 0:
            node = node.inputs()[0]
        return node

    def _find_tail(self, node):
        while len(node.outputs()) > 0:
            node = node.outputs()[0]
        return node
    
    def _node_at_index(self, idx):
        node = self.head
        for i in range(idx):
            if len(node.outputs()) > 0:
                node = node.outputs()[0]
            else:
                print("Index out of range")
                return None
        return node
    
    def layout_nodes(self, node):
        while len(node.outputs()) > 0:
            node.moveToGoodPosition(move_inputs=False)
            node = node.outputs()[0]
            
    def print_tree(self):
        queue = [self.head]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current)
            for i in current.outputs():
                queue.append(i)

    def insert_at(self, idx):
        node = self._node_at_index(idx)
        if node:
            new_node = node.createOutputNode("null")
            if node != self.tail:
                node.outputs()[0].setInput(0, new_node)
            else:
                self.tail = new_node
            self.layout_nodes(new_node)

    def remove_node(self, idx):
        node = self._node_at_index(idx)
        if node:
            if node == self.head and node == self.tail:
                node.destroy()
            elif node == self.head:
                self.head = node.outputs()[0]
                node.destroy()
            elif node == self.tail:
                self.tail = node.inputs()[0]
                node.destroy()
            else:
                node.outputs()[0].setInput(0, node.inputs()[0])
                node.destroy()




myTree = NodeTree(hou.selectedNodes()[0])
myTree.insert_at(2)
# myTree.remove_node(2)
# myTree.print_tree()
# head = hou.selectedNodes()[0]