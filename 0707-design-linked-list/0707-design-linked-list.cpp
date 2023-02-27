class node{
    public:
    node(int val)
    {
        this->val=val;
        this->next=NULL;
    }
    int val;
    node* next;
};
class MyLinkedList {
public:
    MyLinkedList() {
        //node* head;
        this->head=NULL;
        }
        node* head;
    
    int get(int index) {
        node* temp=head;
        int count=0;
        while (count < index) {
        if (temp == NULL) {
            return -1;
        }
        temp = temp->next;
        count++;
    }
    if (temp == NULL) {
        return -1;
    }
    return temp->val;

    }
    
    void addAtHead(int val) {
        node* ptr=new node(val);
        ptr->next=head;
        head=ptr;
        
    }
    
    void addAtTail(int val) {
        node* ptr=new node(val);
        node* temp=head;
        if (temp == NULL) {
            head=ptr;
            return;
        }
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=ptr;
    }
    
    void addAtIndex(int index, int val) {
        if(index==0)
        {
            addAtHead(val);
            return;
        }
        node* ptr = new node(val);
        int count=0;
        node* temp=head;
        while(count<index-1)
        {
            if(temp == NULL)
            {
                return;
            }
            temp=temp->next;
            count++;
        }
        if (!temp) return;
        ptr->next=temp->next;
        temp->next=ptr;
        
    }
    
    void deleteAtIndex(int index) {
        if(head == NULL)
        {
            return;
        }
        if (index==0)
        {
            head=head->next;
            return;
        }
        node* temp=head;
        int count=0;
        while(count<index-1)
        {
            if(temp == NULL)
            {
                return;
            }
            temp=temp->next;
            count++;
        }
        if (temp == NULL || temp->next == NULL) {
        return;
        }
        temp->next=temp->next->next;

        
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */