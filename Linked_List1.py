class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def __str__(self):
		return str([item for item in self])

	def traverse(self):
		if not self.head:
			print("The linked-list is empty")
			return
		node = self.head
		while node:
			print(node.value)
			node = node.next

	def insert(self, value, position = -1):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			return
		if position == 0:
			node.next = self.head
			self.head = node
			print(f"Element: {value} inserted at head")
			return
		if position == -1:
			self.tail.next = node
			node.next = None
			self.tail = node
			print(f"Element: {value} inserted at tail")
			return
		index, curr_node = 1, self.head
		while curr_node.next:
			if index == position:
				node.next = curr_node.next
				curr_node.next = node
				break
			curr_node = curr_node.next
			index += 1
		else:
			curr_node.next = node
			node.next = None
			self.tail = node

	def delete_all(self):
		self.head = self.tail = None
		print("The linked list is now empty")

	def delete(self, position = 0):
		if not self.head:
			print("The linked list is empty")
			return None
		if position == 0:
			val = self.head.value
			self.head = self.head.next
			print("First node of the linked list is deleted now")
			if not self.head:
				self.tail = None
				print("Deleted the only element in the linked-list")
			return val
		if position == -1:
			node = self.head
			val = self.tail.value
			while node.next != self.tail:
				node = node.next
			node.next = None
			self.tail = node
			print("Last element of the linked-list is deleted")
			return val
		index, node = 1, self.head
		val = 0
		while node.next:
			if index == position:
				val = node.next.value
				node.next = node.next.next
				print(f"Deleted value at index: {position}")
				if not node.next:
					self.tail = node
				break
			node = node.next
			index += 1
		return val


ll = LinkedList()
ll.insert(1)
print(ll)
ll.insert(2)
print(ll)
ll.insert(3)
print(ll)
ll.insert(4, 0)
print(ll)
ll.insert(5, -1)
print(ll)
ll.insert(6, 2)
print(ll)
print("=" * 40)
print(f"Deleted Value = {ll.delete(0)}")
print(ll)
print(f"Deleted Value = {ll.delete(-1)}")
print(ll)
print(f"Deleted Value = {ll.delete(3)}")
print(ll)
