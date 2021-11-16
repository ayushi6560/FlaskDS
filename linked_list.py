

class Node:
    def __init__(self, data= None, next_node = None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        ll_list = []
        if self.head == None:
            return ll_list
        node = self.head
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list




    def print_ll(self):
        node = self.head

        ll_string = ""
        if node == None :
            print("ll is none")
            return
        while node:
            ll_string += f"{str(node.data)}-->"
            node = node.next_node

        ll_string += "None"

        print(ll_string)


    def insert_beginning(self,data):

        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head 
            return

        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self, data):
        
        if self.head == None:
            self.insert_beginning(data)
            return
        
        

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
            

    def get_user_by_id(self,user_id):
        node = self.head
        
        while node:
            if node.data["id"] == user_id:
                return node.data

            node = node.next_node

        return None
