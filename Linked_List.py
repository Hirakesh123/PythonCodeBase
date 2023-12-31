class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = self.tail = None

	def __iter__(self):  # Generator Function
		node = self.head
		while node:
			yield node
			node = node.next

	def __str__(self):
		return str([item.value for item in self])

	def insert(self, value, location = -1):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			return
		if location == 0:
			node.next = self.head
			self.head = node
			return
		if location == -1:
			node.next = None
			self.tail.next = node
			self.tail = node
			return
		tmp_node, index = self.head, 1
		while index < location and tmp_node.next:
			index += 1
			tmp_node = tmp_node.next
		if tmp_node == self.tail:
			node.next = None
			self.tail.next = node
			self.tail = node
		else:
			node.next = tmp_node.next
			tmp_node.next = node

	def traverse(self):
		if not self.head:
			print("The linked List is empty")
			return
		node = self.head
		while node:
			print(node.value)
			node = node.next

	def find(self, value):
		if not self.head:
			return "The linked list is empty"
		node, index = self.head, 0
		while node:
			if node.value == value:
				return f"Value: {value} found at index: {index}"
			index += 1
			node = node.next
		else:
			return f"Value: {value} not found"

	def delete(self, location):
		if not self.head:
			print("Cannot delete any element as the linked list is empty")
			return
		if location == 0:
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				self.head = self.head.next
			print("Value deleted from head")
			return
		if location == -1:
			node = self.head
			while node.next != self.tail:
				node = node.next
			node.next = None
			self.tail = node
			print("Value deleted from tail")
			return
		index, node = 1, self.head
		while node.next:
			if index == location:
				print(f"Value deleted at index: {index}")
				node.next = node.next.next
				if node.next is None:
					self.tail = node
				break
				# This break is extremely important.
			index += 1
			node = node.next


ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(7)
ll.insert(6, 78)
ll.traverse()
val = 2
print(ll.find(val))
# print([item.value for item in ll])

ll.delete(0)
print(ll)
ll.delete(-1)
print(ll)

ll.delete(2)
print(ll)
