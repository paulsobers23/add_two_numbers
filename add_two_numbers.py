"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Problem: Given two input of numbers, turn it into reverse linked list and add it and return a new reverse linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Example: 127 + 71 = (7 -> 2 -> 1 ) + (7 -> 1) 
Output: 198 = (8 -> 9 -> 1)

Algorithim:
Given two nodes, loop through the linked list 
Create a total variable 
While looping through nodes , tranverse throughout the list and add to the total variable
After you have the total of both nodes, create a reverse linked list from that number and return the newly created linked list.


"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)
        
    
def add_two_numbers(num1: Node, num2: Node) -> Node:
    current1 = num1
    current2 = num2
    carry = 0
    sum_list = Node()
    current_sum = sum_list
    
    while current1 or current2 or carry:
        total = current1.data + current2.data + carry
        if total > 9:
            carry = 1
            total -= 10
            current_sum.next = Node(total)
        else:
            carry = 0
            current_sum.next = Node(total)
            
        current1 = current1.next
        current2 = current2.next
        current_sum = current_sum.next
    
    return sum_list.next
        
        
        