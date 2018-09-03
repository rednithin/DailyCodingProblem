/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
*/

#include<iostream>
using namespace std;

struct Node {
  int value;
  Node * both;
};

class LinkedList {
  int count;
  Node *first, *last;
  Node *XOR(Node *a, Node *b) {
    return (Node *)((long)a ^ (long)b);
  }
  public:
    LinkedList() {
      first = last = NULL;
      count = 0;
    }
    void append(int value) {
      count ++;
      Node *n = new Node;
      n->value = value;
      n->both = NULL;
      if(first == NULL) {
        first = last = n;
      }
      else {
        if(first == last) {
          last->both = XOR(NULL, n);
        } else {
          last->both = XOR(last->both, n);
        }
        n->both = XOR(NULL,last);
        last = n;
      }
    }
    void traverseFirstToLast() {
      string output = "";
      Node *temp = first;
      Node *aux = NULL;
      Node *prev = NULL;
      for(int i = 0; i < count; i++) {
        cout << temp->value << endl;
        aux = XOR(temp->both, prev);
        prev = temp;
        temp = aux;
      }
    }
    void traverseLastToFirst() {
      string output = "";
      Node *temp = last;
      Node *aux = NULL;
      Node *prev = NULL;
      for(int i = 0; i < count; i++) {
        cout << temp->value << endl;
        aux = XOR(temp->both, prev);
        prev = temp;
        temp = aux;
      }
    }
};

int main(int argc, char const *argv[])
{
  LinkedList ll;
  ll.append(1);
  ll.append(2);
  ll.append(3);
  ll.append(4);
  ll.append(5);
  ll.traverseFirstToLast();
  cout << endl;
  ll.traverseLastToFirst();
  return 0;
}




