class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class SingleLinkList:
    def __init__(self,start=None):
        self.start = start
              
    def is_empty(self):
        return self.start==None
    
    # 1)list can be empty 2)list can have multiple nodes.
    def insert_at_start(self,item): 
        n = Node(item,self.start)
        self.start = n
            
    def insert_at_last(self,item):
        n = Node(item)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
            
    def search(self,item):
            temp = self.start
            while temp is not None:
                if(temp.item==item):
                    return temp
                temp = temp.next
            return None 
            
    def insert_after(self,temp,item):
        if temp is not None:
            n = Node(item,temp.next)
            temp.next = n
            
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
            
    # deletion:
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            
    def delete_item(self,item):
        if self.is_empty():
            pass
        elif self.start.next is None:   # only one element in linked_list
            if self.start.item == item:    
                self.start = None
        else:
            temp = self.start
            if(temp.item == item):
                self.start = temp.next
            while temp.next is not None:
                if(temp.next.item==item):
                    temp.next = temp.next.next 
                    break
                else:
                    temp = temp.next
            
                
                 
            
            
            
            
myList = SingleLinkList() 
       
                        
    
            
            
        
        
        
        
            
            
        
            
        
        
    

# node1 = Node()
sll =SingleLinkList()
sll.insert_at_start(10)
sll.insert_at_last(20)
sll.insert_after(sll.search(10),15)
sll.insert_at_start(5)
sll.insert_at_last(25)
sll.insert_after(sll.search(25),30)


sll.print_list()

