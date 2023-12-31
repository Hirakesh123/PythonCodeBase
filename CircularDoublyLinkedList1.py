class Node:
	def __init__(self, value):
		self.value = value
		self.next = self.prev = None

	def __str__(self):
		return str(self.value)


class CircularDoublyLinkedList:
	def __init__(self):
		self.head = self.tail = None

	def __iter__(self):
		node = self.head
		while True:
			yield node.value
			if node == self.tail:
				return
			node = node.next

	def __iter_rev__(self):
		node = self.tail
		while True:
			yield node.value
			if node == self.head:
				return
			node = node.prev

	def __str__(self):
		return "[" + "-->".join([str(_item) for _item in self]) + "]"

	def __str_reverse__(self):
		return "[" + "<--".join([str(_item) for _item in self.__iter_rev__()]) + "]"

	def traverse(self, reverse = False):
		return self.__str_reverse__() if reverse else self.__str__()

	def insert(self, value, position = 0):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node.next = node.prev = node
			return

		if position == 0:
			node.next = self.head
			node.prev = self.tail
			self.head.prev = node
			self.head = node
			self.tail.next = self.head
			return
		if position == -1:
			node.next = self.head
			node.prev = self.tail
			self.tail.next = node
			self.head.prev = node
			self.tail = node
			return

		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if position == index:
					node.next = curr_node.next
					node.prev = curr_node
					curr_node.next.prev = node
					curr_node.next = node
					break
				curr_node = curr_node.next
				index += 1
			else:
				node.next = self.head
				node.prev = self.tail
				self.tail.next = node
				self.head.prev = node
				self.tail = node
			return

		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if position == index:
				node.next = curr_node
				node.prev = curr_node.prev
				curr_node.prev.next = node
				curr_node.prev = node
				break
			curr_node = curr_node.prev
			index -= 1
		else:
			node.next = self.head
			self.head.prev = node
			node.prev = self.tail
			self.head = node
			self.tail.next = self.head

	def delete(self, position):
		if not self.head:
			print("Data underflow: Linked List is empty. Cannot delete more elements.")
			return
		if position == 0:
			val = self.head.value
			self.head = self.head.next
			self.head.prev = self.tail
			self.tail.next = self.head
			return val

		if position == -1:
			val = self.tail.value
			self.tail = self.tail.prev
			self.tail.next = self.head
			self.head.prev = self.tail
			return val

		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if position == index:
					val = curr_node.next.value
					curr_node.next = curr_node.next.next
					if curr_node.next == self.head:
						self.tail = curr_node
						self.head.prev = curr_node  # This is important
					else:
						curr_node.next.prev = curr_node
					return val
				curr_node = curr_node.next
				index += 1
			else:
				print("Delete index out of bounds error. No item deleted.")
				return None
		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if position == index:
				val = curr_node.prev.value
				curr_node.prev = curr_node.prev.prev
				if curr_node.prev == self.tail:
					self.head = curr_node
					self.tail.next = curr_node  # This is important
				else:
					curr_node.prev.next = curr_node  # This is also important
				return val
			index -= 1
			curr_node = curr_node.prev
		else:
			print("Delete index out of bounds error. No item deleted.")
			return None


ll = CircularDoublyLinkedList()
ll.insert(10, -1)
ll.insert(20, -1)
ll.insert(30, -1)
ll.insert(40, -1)
ll.insert(50, -1)
print(ll)

print("==" * 10)

print("Deleting at: 2")
item = ll.delete(2)
print(ll, item)
print(ll.traverse(reverse = True))