class Node:
	def __init__(self, value):
		self.value = value
		self.prev = self.next = None


class DoublyLinkedList:
	def __init__(self):
		self.head = self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def __iter_reverse__(self):
		node = self.tail
		while node:
			yield node.value
			node = node.prev

	def __str__(self):
		return "[" + "-->".join([str(item) for item in self]) + "]"

	def __str_reverse__(self):
		return "[" + "<--".join([str(item) for item in self.__iter_reverse__()]) + "]"

	def traverse(self, reverse = False):
		return self.__str_reverse__() if reverse else self.__str__()

	def insert(self, value, position = -1):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			return

		if position == 0:
			node.next = self.head
			self.head.prev = node
			self.head = node
			return

		if position == -1:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
			return

		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if position == index:
					print("Condition Met")
					node.next = curr_node.next
					node.prev = curr_node
					curr_node.next.prev = node
					curr_node.next = node
					break
				curr_node = curr_node.next
				index += 1
			else:
				node.prev = self.tail
				self.tail.next = node
				self.tail = node
			return
		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if position == index:
				node.prev = curr_node.prev
				node.next = curr_node
				curr_node.prev.next = node
				curr_node.prev = node
				break
			curr_node = curr_node.prev
			index -= 1
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

	def partition(self, pivot):
		curr_node = self.head
		while curr_node.next:
			# point the curr_node to a node that is >= pivot.
			if curr_node.value < pivot:
				curr_node = curr_node.next
			else:
				break

		while curr_node.next:
			if curr_node.next.value >= pivot:
				curr_node = curr_node.next
				# if the next node's value >= pivot, advance curr_node by one'
			else:
				# if the value is less than pivot, then first remove it from the original position
				tmp_node = curr_node.next
				curr_node.next = curr_node.next.next
				# there are two conditions: the next element to be removed may be a tail or any middle value

				if curr_node.next:
					# the next element is not tail
					curr_node.next.prev = curr_node

				else:
					self.tail = curr_node
				tmp_node.prev = curr_node.prev
				tmp_node.next = curr_node
				# till here.

				# next, we have to insert the extracted node just before the curr node
				# again, we are having two conditions

				if curr_node.prev:
					# if the current node is the head,
					curr_node.prev.next = tmp_node
				else:
					self.head = tmp_node
				curr_node.prev = tmp_node

	def delete(self, position = -1):
		if not self.head:
			print("Linked list is empty. Hence deletion not possible.")
			return

		if position == 0:
			val = self.head.value
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				self.head = self.head.next
				self.head.prev = None
			return val

		if position == -1:
			val = self.tail.value
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				self.tail = self.tail.prev
				self.tail.next = None
			return val

		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:  # Important
				if index == position:
					val = curr_node.next.value
					curr_node.next = curr_node.next.next
					if curr_node.next is None:
						self.tail = curr_node
					return val
				curr_node = curr_node.next
				index += 1
			else:
				print("Delete Index out of bounds Error. No element deleted.")
				return None

		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if index == position:
				val = curr_node.prev.value
				curr_node.prev = curr_node.prev.prev
				if curr_node.prev is None:
					self.head = curr_node
				else:
					curr_node.prev.next = curr_node
				return val
			index -= 1
			curr_node = curr_node.prev
		else:
			print("Delete Index out of bounds Error. No element deleted.")
			return None


ll = DoublyLinkedList()
ll.insert(11)
ll.insert(3)
ll.insert(9)
ll.insert(10)
ll.insert(15)

print(ll.traverse())
print(ll.traverse(reverse = True))

ll.partition(30)

print(ll.traverse())
print(ll.traverse(reverse = True))
