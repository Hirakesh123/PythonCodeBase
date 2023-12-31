class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)


# A stack follows LIFO(Last-In-First-Out Paradigm)
# Item is pushed/popped at head only for O(1) time complexity
# Literally has no limit and performance does never depend on size

class Stack:
	def __init__(self):
		self.head = self.tail = None

	def is_empty(self):
		return self.head is None

	def __iter__(self):
		node = self.head
		while node:
			yield str(node.value)
			node = node.next

	def __str__(self):
		return "\n".join([item for item in self])

	def push(self, value):
		node = Node(value)
		if self.is_empty():
			self.head = self.tail = node
			return
		node.next = self.head
		self.head = node

	def pop(self):
		if self.head and self.head == self.tail:
			print("Popping out the last element in the stack.")
			value = self.head.value
			self.head = self.tail = None
			return value

		if not self.is_empty():
			value = self.head.value
			self.head = self.head.next
			return value

		else:
			print("Data underflow. Cannot pop as the stack is empty")
			return None

	def peek(self):
		if not self.is_empty():
			return str(self.head.value)
		else:
			print("No element to peek as the stack is empty")
			return None


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)

print(s1)

print("Peeking: " + s1.peek())

print(s1.pop())
print(s1.pop())
print("Peeking: " + s1.peek())

print(s1.pop())
print(s1.pop())
print(s1.pop())

print(s1)
