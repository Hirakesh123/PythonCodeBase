class Node:
	def __init__(self, value):
		self.value = value
		self.prev = self.next = None

	def __str__(self):
		return str(self.value)


class CircularDoublyLinkedList:
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
		return str([i for i in self])

	def traverse(self, reverse = False):
		if not self.head:
			return "Linked List is empty. Traversal not possible."

		node = self.head
		s = str(node)
		while True:
			node = node.next
			if node == self.head:
				return s
			if reverse:
				s = f"{node} <-- " + s
			else:
				s += f" --> {node}"
	#
	# def __getitem__(self, item):
	# 	index, node = 0, self.head
	# 	while node:
	# 		if index == item:
	# 			return node.value
	# 		node = node.next
	# 		index += 1
	# 		if node == self.head:
	# 			return None
	# 		else:
	# 			return None

	def __getitem__(self, item):
		if item < 0:
			index, node = -1, self.tail
			while node:
				if index == item:
					return node.value
				node = node.prev
				index -= 1
				if node == self.tail:
					return None
			else:
				return None
		else:
			index, node = 0, self.head
			while node:
				if index == item:
					return node.value
				node = node.next
				index += 1
				if node == self.head:
					return None
			else:
				return None

	def __len__(self):
		count, node = 0, self.head
		while node:
			count += 1
			node = node.next
			if node == self.head:
				return count
		else:
			return None

	@staticmethod
	def insert_between(left_node, right_node, node):
		print("Insert Between")
		node.prev, node.next = left_node, right_node
		left_node.next = right_node.prev = node

	def insert_at_head(self, node):
		print("Insert at head")
		self.insert_between(self.tail, self.head, node)
		self.head = node

	def insert_at_tail(self, node):
		print("Insert at tail")
		self.insert_between(self.tail, self.head, node)
		self.tail = node

	def insert(self, value, position = 0):
		node = Node(value)
		if not self.head:
			self.head, self.tail, node.next, node.prev = node, node, node, node
			return
		if position == 0:
			self.insert_at_head(node)
			return
		if position == -1:
			self.insert_at_tail(node)
			return
		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if index == position:
					self.insert_between(curr_node, curr_node.next, node)
					break
				curr_node = curr_node.next
				index += 1
			else:
				self.insert_at_tail(node)
			return
		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if position == index:
				self.insert_between(curr_node.prev, curr_node, node)
				break
			curr_node = curr_node.prev
			index -= 1
		else:
			self.insert_at_head(node)

	def delete_at_position(self, position = 0):
		if not self.head:
			print("Linked List is empty. Cannot delete more items.")
			return None
		if position == 0:
			val = self.head.value
			if self.head == self.tail:
				self.head.next = self.head.prev = None
				self.head = self.tail = None
			else:
				self.head = self.head.next
				self.tail.next = self.head
				self.head.prev = self.tail
			return val
		if position == -1:
			val = self.tail.value
			if self.head == self.tail:
				self.head.prev = self.head.next = None
				self.head = self.tail = None
			else:
				self.tail = self.tail.prev
				self.head.prev = self.tail
				self.tail.next = self.head
			return val

		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if index == position:
					# curr_node.next.next.prev = curr_node
					curr_node.next = curr_node.next.next
					curr_node.next.prev = curr_node
					if curr_node.next == self.tail:
						self.tail = curr_node
					break
				curr_node = curr_node.next
				index += 1

		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if index == position:
				flag = curr_node.prev == self.head
				# curr_node.prev.prev.next = curr_node
				curr_node.prev = curr_node.prev.prev
				curr_node.prev.next = curr_node
				if flag:
					self.head = curr_node
				break
			curr_node = curr_node.prev
			index -= 1


cdll = CircularDoublyLinkedList()
cdll.insert(10)
print(cdll)
cdll.insert(15, -1)
print(cdll)
cdll.insert(20, -1)
print(cdll)
cdll.insert(25, -3)
print(cdll)
print("Forward Traversal: ", cdll.traverse(), sep = "")
print("\nBackward Traversal: ", cdll.traverse(reverse = True), sep = "")

d_val = cdll.delete_at_position()
print(cdll, d_val)
d_val = cdll.delete_at_position()
print(cdll, d_val)
d_val = cdll.delete_at_position()
print(cdll, d_val)
d_val = cdll.delete_at_position()
print(cdll, d_val)
d_val = cdll.delete_at_position()
print(cdll, d_val)

print(cdll.traverse())

print("Reached Here")
