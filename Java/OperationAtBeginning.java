class Node{
    int data;
    Node next;
    Node(int data){
        this.data=data;
        this.next=null;
    }
}

class Stack{
    Node head;
    Stack(){
        this.head=null;
    }

    public void push(int data){
        Node new_node=new Node(data);
        if(head==null)
        {
            head=new_node;
            return;
        }
        new_node.next=head;
        head=new_node;
    }

    public void pop(){
        if(head==null)
        {
            System.out.println("Stack is Empty");
            return;
        }
        System.out.println("popped : "+head.data);
        head=head.next;
    }

    public void display(){
        if(head==null){
            System.out.println("[]");
            return;
        }
        Node temp=head;
        System.out.print("[");
        while(true){
            System.out.print(temp.data);
            temp=temp.next;
            if(temp==null)
            {
                System.out.println("]");
                break;
            }
            else{
                System.out.print(", ");
            }
        }
    }
}

public class OperationAtBeginning {
    public static void main(String[] args) {
        Stack stack=new Stack();

        // insert at beginning

        stack.display();
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
        stack.push(6);
        stack.display();

        // delete at beginning

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
        stack.pop();
        stack.display();
    }
}