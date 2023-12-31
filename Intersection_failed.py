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
					# print("Condition Met")
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


def intersection(l1, l2):
	if (not l1) or (not l2):
		print("Either one or Both Linked Lists are empty")
		return None
	if l1.tail == l2.tail and l1.head == l2.head:
		print("Both the lists are identical")
		return l1.head
	if l1.tail != l2.tail:
		print("Linked Lists are disjoint")
		return None
	n1, n2 = l1.tail, l2.tail
	# Till now, n1 and n2 are pointing to the same Node object
	while True:
		print("Iterated: ")
		if (n1 == l1.head and n2 != l2.head) or (n1 != l1.head and n2 == l2.head):
			print("One is subset of the other")
			return n1
		if n1 != n2:
			print("Intersection Point returned")
			return n1.next if n1 else n2.next
		n1, n2 = n1.prev, n2.prev


def intersection1(l1, l2):
	if (not l1) or (not l2):
		print("Either or both the Linked-Lists are empty")

		return None
	if l1.tail != l2.tail:
		print("The Linked-lists are disjoint")
		print(l1.tail.value, l2.tail.value)
		return None
	if l1.head == l2.head:
		print("Both lists are identical")
		return l1.head
	n1, n2 = l1.tail, l2.tail
	while n1 and n2 and n1 == n2:
		n1 = n1.prev
		n2 = n2.prev

	if n1:
		return n1.next
	elif n2:
		return n2.next
	else:
		print("Both the lists are identical")
		return l1.head


la, lb = DoublyLinkedList(), DoublyLinkedList()
la.insert(10)
la.insert(20)
la.insert(30)
la.insert(40)
la.insert(50)
la.insert(60)
la.insert(70)

lb.head, lb.tail = la.head.next.next.next, la.tail

lb.insert(100, 0)
lb.insert(200, 1)


print("Tail Values: ")
print(la.tail.value, lb.tail.value)

print("lb.head.value")
print(lb.head.value)

print("showing both linked lists")
print(la)
print(lb)

print("Printing intersection value: ")
intersection_node = intersection(la, lb)
print(intersection_node.value)

lc = DoublyLinkedList()
lc.head = intersection_node

print(lc)

print(la.traverse(reverse = True))
print(lb.traverse(reverse = True))
