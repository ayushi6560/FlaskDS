class Node:
    def __init__(self, data= None, next_node = None):
        self.data = data
        self.next_node = next_node


class Data:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hash_Table():
    
    def __init__(self, table_size):

        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = hash_value * ord(i) % self.table_size

        return hash_value

    def add_key_value(self, key,value):
        hashed_key = self.custom_hash(key)
        # print(hashed_key)
        if self.hash_table[hashed_key] == None:
            self.hash_table[hashed_key] = Node(Data(key,value), None)
        else:
            print("here")
            node = self.hash_table[hashed_key]
            while node.next_node:
                # print("inside while")
                node = node.next_node
            # print(node.next_node)
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        
        if self.hash_table[hashed_key] != None:
            node = self.hash_table[hashed_key]
            if node.next_node == None:
                node = self.hash_table[hashed_key]
                return node.data.value
            
            while node.next_node:
                if node.data.key == key:
                    return node.data.value
                node = node.next_node

            if node.data.key == key:
                return node.data.value

            
        return None


    def print_table(self):

        print("{")

        for i, value in enumerate(self.hash_table):

            if value != None:
                llist_string = ""
                node = value
                if node.next_node != None:
                    while node.next_node:
                        # print(f"{node.data.key} : {node.data.value}")
                        llist_string +=  (
                             str(node.data.key) + ":" + str(node.data.value) + "--->"
                        )
                        node = node.next_node

                    llist_string += (node.data.key + ":" + node.data.value) + "---> None"

                    print(f"[{i}] {llist_string}")

                else:
                    print(f"[{i}] {value.data.key}+ ':' + {value.data.value}")

            else :
                print(f"[{i}] {value}")

        print("}")


# ht = Hash_Table(4)
# ht.add_key_value("hi","there")
# ht.add_key_value("hi","here")
# ht.print_table()

                


        
