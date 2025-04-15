class Node:
    def __init__(self, data):
        self.data=data;
        self.next=None;
        
class Stack:
    def __init__(self):
        self.head=None;
        
    def push(self, data):
        new_node=Node(data);
        if self.head is None:
            self.head=new_node;
            return;
        new_node.next=self.head;
        self.head=new_node;
        
    def pop(self):
        if self.head is None:
            print("Stack is Empty");
            return;
        print("popped : ", self.head.data);
        self.head=self.head.next;
        
    def display(self):
        if self.head is None:
            print("[]");
            return;
        temp=self.head;
        res=[];
        while temp:
            res.append(temp.data);
            temp=temp.next;
        print(res);
        
if __name__=="__main__":
    stack=Stack();
    
    stack.display();
    
    # push operation at beginning
    
    stack.push(1);
    stack.display();
    stack.push(2);
    stack.display();
    stack.push(3);
    stack.display();
    stack.push(4);
    stack.display();
    stack.push(5);
    stack.display();
    
    # pop operation at beginning
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();