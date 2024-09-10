
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        if(self.start==None):
            return True
        
    # insertion:
    # 1 insertion at start:
    def insert_at_start(self,item):
        n = Node(None,item,self.start)
        if(not self.is_empty()):
            self.start.prev = n
        self.start = n
    
    def insert_at_end(self,item):
        temp = self.start
        n = Node(temp,item,None)
        if(not self.is_empty()):
            while temp.next is not None:
                temp = temp.next 
            n.prev = temp           
            temp.next = n
        else:
            self.start = n
                
        
        
    def search(self,value):
        temp = self.start
        if temp is not None:
            while temp is not None:
                if(temp.item == value):
                    return temp
                temp = temp.next
        return None
    
    def insert_after(self,temp,item):
        if temp is not None:
            n = Node(temp,item,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
        
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
            
    def delete_first(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is not None:
                temp.next.prev = None
            self.start = temp.next
            
    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is None:
                self.start=None
                temp = None
                return
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp = None
            
    def delete_item(self,temp):
        if temp is not None:
            if temp.next is not None:
                temp.next.prev = temp.prev
                if temp.prev is None:
                    self.start = temp.next
                
            if temp.prev is not None:
                temp.prev.next = temp.next
           

obj = DoublyLinkedList()

obj.insert_at_end(7)
obj.insert_at_start(5)
obj.insert_after(obj.search(5),6)
# obj.delete_first()
# obj.delete_last()
obj.delete_item(obj.search(7))
obj.print_list()