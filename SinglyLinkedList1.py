class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)


class SinglyLinkedList:
	def __init__(self):
		self.head = self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def __str__(self):
		return "[" + "-->".join([str(_item) for _item in self]) + "]"

	def __len__(self):
		return len([_item for _item in self])

	def insert(self, value, position = -1):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			return
		if position == 0:
			node.next = self.head
			self.head = node
			return
		if position == -1:
			self.tail.next = node
			self.tail = node
			return

		index, curr_node = 1, self.head
		while curr_node != self.tail:
			if position == index:
				node.next = curr_node.next
				curr_node.next = node
				break
			curr_node = curr_node.next
			index += 1
		else:
			self.tail.next = node
			self.tail = node

	def delete(self, position):
		if not self.head:
			print("The linked list is empty. Cannot delete more elements")
			return
		if position == 0:
			val = self.head.value
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				self.head = self.head.next
			return val

		if position == -1:
			val = self.tail.value
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				curr_node = self.head
				while curr_node.next != self.tail:
					curr_node = curr_node.next
				self.tail = curr_node
				self.tail.next = None
			return val
		# This part is important
		print("**" * 20)
		index, curr_node = 1, self.head
		while curr_node != self.tail:
			if position == index:
				val = curr_node.next.value
				curr_node.next = curr_node.next.next
				if not curr_node.next:
					self.tail = curr_node
				return val
			curr_node = curr_node.next
			index += 1


sll = SinglyLinkedList()
print(sll)
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)
print(sll)
print("Inserting at index 4")
sll.insert(50, 4)
print(sll)

print("--" * 20)
print("Deleting at index 0")
item = sll.delete(0)
print(sll, item)
print("Deleting at index -1")
item = sll.delete(-1)
print(sll, item)
print("Deleting at index 2")
item = sll.delete(2)
print(sll, item)
print("Deleting at 0 index")
item = sll.delete(0)
print(sll, item)
print("Deleting at index 0")
item = sll.delete(0)
print(sll, item)
print("Deleting at index 0")
item = sll.delete(0)
print(sll, item)

print(sll)
