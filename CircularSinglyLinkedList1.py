class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = self.tail = None

	def __iter__(self):
		node = self.head

		while node:
			yield node.value
			node = node.next
			if node == self.head:
				return

	def __str__(self):
		return "[" + "-->".join([str(_item) for _item in self]) + "]"

	def insert(self, value, position = -1):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			self.tail.next = self.head
			return

		if position < -1:
			node.next = self.head
			self.head = node
			self.tail.next = self.head
			return

		if position == -1:
			self.tail.next = node
			node.next = self.head
			self.tail = node
			return

		index, curr_node = 1, self.head

		while curr_node.next != self.tail:
			if position == index:
				node.next = curr_node.next
				curr_node.next = node
				break
			index += 1
			curr_node = curr_node.next
		else:
			self.tail.next = node
			node.next = self.head
			self.tail = node

	def traverse_circular(self, turns):
		node = self.head
		if not node:
			print("Traversing through an empty linked list makes no sense.")
			return
		for l in range(turns):
			print(node.value, end = "-->")
			node = node.next

	def delete(self, position):
		if not self.head:
			print("Cannot delete from the linked list as it is already empty.")
			return

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
			val = self.tail.value
			if self.head == self.tail:
				self.head.next = None
				self.head = self.tail = None
			else:
				curr_node = self.head
				while curr_node.next != self.tail:
					curr_node = curr_node.next
				self.tail = curr_node
				self.tail.next = self.head
			return val

		index, curr_node = 1, self.head
		while curr_node != self.tail:
			if position == index:
				val = curr_node.next.value
				curr_node.next = curr_node.next.next
				if curr_node.next == self.head:
					self.tail = curr_node
				return val
			curr_node = curr_node.next
			index += 1
		else:
			print("Delete Index out of range error. No element deleted")
			return None


cll = CircularLinkedList()
print(cll)

cll.insert(10)
cll.insert(20)
cll.insert(30)
print(cll)

print("Inserting at position: 0")
cll.insert(40, 0)
print(cll)

print("Inserting at position: -1")
cll.insert(50, -1)
print(cll)

print("Inserting at position: 3")
cll.insert(60, 3)
print(cll)

print("Deleting at position: 0")
item = cll.delete(0)
print(cll, item)

print("Deleting at position: -1")
item = cll.delete(-1)
print(cll, item)

print("Deleting at position: 4")
item = cll.delete(4)
print(cll, item)


cll2 = CircularLinkedList()
cll2.traverse_circular(10)
