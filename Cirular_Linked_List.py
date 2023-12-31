class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		if not self.head:
			return
		node = self.head
		while True:
			yield node.value
			if node == self.tail:
				break
			node = node.next

	def __str__(self):
		return str([item for item in self])

	def insert(self, value, position = 0):
		node = Node(value)
		if not self.head:
			node.next = node
			self.head = self.tail = node
			print("Element inserted at head as the list was empty")
			return

		if position == 0:
			node.next = self.head
			self.head = node
			self.tail.next = self.head
			return

		if position == -1:
			node.next = self.head
			self.tail.next = node
			self.tail = node
			return

		index, curr_node = 1, self.head
		while curr_node != self.tail:
			if index == position:
				node.next = curr_node.next
				curr_node.next = node
				break
			index += 1
			curr_node = curr_node.next
		else:
			node.next = self.head
			self.tail.next = node
			self.tail = node

	def traverse(self, count = None):
		if not count:
			node = self.head
			while True:
				print(node.value, end = "-->")
				if node == self.tail:
					break
				node = node.next
		else:
			index = 0
			node = self.head
			while index < count:
				print(node.value, end = "-->")
				node = node.next
				index += 1

	def find(self, value):
		index, node = 0, self.head
		while node:
			if node.value == value:
				return f"Value : {value} found at index: {index}"
			if node == self.tail:
				break
			index += 1
			node = node.next
		return f"Value: {value} not found in the Linked List"

	def delete_item(self, value):
		self.delete_items(value, delete_all = False)
		pass

	def delete_items(self, value, delete_all = True):

		pass

	def delete_at_position(self, position = 0):
		if not self.head:
			return "Linked List is empty"
		if position == 0:
			val = self.head.value
			if self.head == self.tail:
				self.head.next = None
				self.head = self.tail = None
			else:
				self.head = self.head.next
				self.tail.next = self.head
			return val

		if position == -1:
			if self.head == self.tail:
				val = self.head.value
				self.head.next = None
				self.head = self.tail = None
				return val
			node = self.head
			while node.next != self.tail:
				node = node.next
			val = node.next.value
			node.next = self.head
			self.tail = node
			return val

		index, node = 1, self.head

		while node.next != self.tail:
			if position == index:

				val = node.next.value
				if node.next == self.tail:
					node.next = self.head
					self.tail = node
					return val
				node.next = node.next.next
				return val
			node = node.next
			# print("Control is here")
			index += 1
		pass

	def delete_all(self):
		self.head = self.tail = None
		print("All Elements are deleted. Linked List is now empty")
		pass


cll = CircularLinkedList()
print("Inserting 10 at head")
cll.insert(10)
print(cll)
print("Inserting 20 at head")
cll.insert(20)
print(cll)
print("Inserting 30 at head")
cll.insert(30)
print(cll)

print("Inserting 40 at end")
cll.insert(40, -1)
print(cll)
print("Inserting 50 at end")
cll.insert(50, -1)
print(cll)
print("Inserting 60 at end")
cll.insert(60, -1)
print(cll)

print("Inserting 70 at index = 3")
cll.insert(70, 3)
print(cll)

print("Inserting 80 at index 20")
cll.insert(80, 20)
print(cll)

print("Traversing once through the linked list: ")
cll.traverse()

print("\nTraversing 15 steps through the Linked List: ")
cll.traverse(15)

print("\nChecking the presence of 40 in the linked List")
print(cll.find(40))

print("\nChecking the presence of 30 in the linked List")
print(cll.find(30))

print("\nChecking the presence of 80 in the linked List")
print(cll.find(80))

print("\nChecking the presence of 100 in the linked List")
print(cll.find(100))

print("==" * 15)

print("Deleting element at head")
print(f"Value = {cll.delete_at_position(0)}")
print(cll)

print("Deleting 10 elements at tail")
print(f"Value = {cll.delete_at_position(-1)}")
print(cll)

i = 6
print(f"Deleting element at index {i}:")
print(f"Value = {cll.delete_at_position(i)}")
print(cll)

# print(locals())
