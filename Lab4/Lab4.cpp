#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}  // Constructor
};

class Stack {
private:
    Node* head;   // Points to the top of the stack
    int num;      // Number of elements
    int capacity; // Capacity (not actually used in resizing)

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = 0;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num == capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        num++;
    }
    int pop() {
        if (isEmpty()) {return -1;}
        Node* oldHead = head;
        int val = head->data;
        head = head->next;
        delete oldHead;
        num --;
        return val;
    }

    int peek() {
        if (isEmpty()) return -1;
        return head->data;
    }

    bool isEmpty() {
        return num == 0;
    }

    void increaseCapacity() {
        capacity *= 2;
    }

    bool deleteElement(int val) {
        if(isEmpty()){
            cout<< "This stack is empty."<<endl;
            return false;
        }
        else if (val==head->data){
            pop();
        }
        Node* prev = head;
        Node* curr = head->next;
        while(curr!= nullptr){
            if(curr->data==val){
                prev->next = curr->next;
                delete curr;
                num--;
                return true;
            }
            prev = curr,
            curr= curr->next;
        }
        cout<< "This value does not found."<<endl;
        return false;
    }

};

// Test code
int main() {
    Stack* stack = new Stack(10);
    stack->push(1);
    stack->push(2);
    stack->push(3);
    cout << stack-> deleteElement(0) << endl;



    cout << stack->peek() << endl;


    return 0;
}
