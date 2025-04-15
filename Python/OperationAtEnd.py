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
        temp=self.head;
        while temp.next:
            temp=temp.next;
        temp.next=new_node;
        
    def pop(self):
        if self.head is None:
            print("Stack is Empty");
            return;
        elif self.head.next is None:
            print("popped : ", self.head.data);
            self.head=None;
            return;
        temp=self.head;
        while temp.next.next:
            temp=temp.next;
        print("popped : ", temp.next.data);
        temp.next=None;
        
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