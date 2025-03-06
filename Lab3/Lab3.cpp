#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;
    LinkedList() : head(nullptr) {}

    void addItem(int val) {
        if (head == nullptr) {
            insertAtHead(val);
        }else {
            insertAtTail(val);
        }
    }

    void insertAtHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }
    void insertAtTail(int val) {
        Node* newNode = new Node(val);
        if (!head) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    int deleteAtHead() {
        Node* temp = head;
        head = head->next;
        int tempData = temp->data;
        delete temp;
        return tempData;
    }

};

class Queue {
    private:
    LinkedList list;
    public:
    int x = 0;
    void enqueue(int val) {
        x = x + 1;
        list.addItem(val);
    }
    void dequeue() {
        if (isEmpty() == false) {
            x = x - 1;
            list.deleteAtHead();
        }
    }
    int top() {
        return list.head->data;
    }
    bool isEmpty() {
        if (x == 0) return true;
        return false;

    }
    int size() {
        return x;
    }

};

int main() {
    Queue queue;
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    cout << queue.top() << endl;
    queue.dequeue();
    cout << queue.top() << endl;
    cout << queue.size() << endl;
    cout << queue.isEmpty() << endl;
    return 0;
}
