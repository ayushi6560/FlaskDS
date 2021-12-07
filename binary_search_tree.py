class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def _insert_recursive(self,data,node):
        if data["id"] < node.data["id"] :
            if node.left == None:
                node.left = Node(data["id"])
            else :
                self._insert_recursive(data["id"],node.left)

        elif data["id"] > node.data :
            if node.right == None:
                node.right = Node(data["id"])
            else :
                self._insert_recursive(data["id"],node.right)

        else:
            return

    def insert(self,data):
        if self.root ==None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)



    def _search_recursive(self,blogpost_id,node):

        if node.left == None and node.right == None:
            return False
        
        if blogpost_id == node.data["id"]:
            return node.data

        if blogpost_id < node.data["id"]:
            if blogpost_id == node.left.data["id"]:
                return node.left.data
            else:
                return self._search_recursive(blogpost_id,node.left)

        if blogpost_id > node.data["id"]:
            if blogpost_id == node.right.data["id"]:
                return node.right.data
            else:
                return self._search_recursive(blogpost_id,node.right)


    def search(self,blogpost_id):
        blogpost_id = int(blogpost_id)

        if self.root == None:
            return False

        return self._search_recursive(blogpost_id,self.root)

        