class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def __str__(self):
		return str([x for x in dll])

	def insert(self, value, position = 0):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
			print("LINK LIST HAS BEEN INITIALIZED")
			return
		if position == 0:
			node.next = self.head
			self.head.prev = node
			self.head = node
			print(f"Added to head: {value}")
			return
		if position == -1:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
			return
		if position > 0:
			index, curr_node = 1, self.head
			while curr_node != self.tail:
				if index == position:
					node.next = curr_node.next
					node.prev = curr_node
					curr_node.next.prev = node
					curr_node.next = node
					# curr_node.next.prev = curr_node.next = node
					# above statement is wrong as the associativity of = is right to left
					break
				curr_node = curr_node.next
				index += 1
			else:
				self.tail.next = node
				node.prev = self.tail
				self.tail = node
			return
		index, curr_node = -2, self.tail
		while curr_node != self.head:
			if index == position:
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
			self.head = node

	def traverse(self, reverse = False):
		print("Traversing " + ("Backward:" if reverse else "Forward:"))
		start, target = (self.tail, self.head) if reverse else (self.head, self.tail)
		# Here, parentheses are genuinely required to remove syntactical ambiguity
		while True:
			print(start.value, end = "<--" if reverse else "-->")
			if start == target:
				break
			start = start.prev if reverse else start.next
		print()

	def remove_at_position(self, position = 0):
		if not self.head:
			print("the linked list is empty.")
			return
		if position == 0:
			val = self.head.value
			if self.head == self.tail:
				self.head = self.tail = None
				print("Linked List is now empty")
			else:
				self.head.next.prev = None
				self.head = self.head.next
			return val
		if position == -1:
			val = self.tail.value
			if self.head == self.tail:
				self.head = self.tail = None
				print("Linked List is now empty")
			else:
				self.tail.prev.next = None
				self.tail = self.tail.prev
			return val

		if position > 0:
			index, node = 1, self.head
			while node.next:
				if index == position:
					val = node.next.value
					node.next.next.prev = node
					node.next = node.next.next
					return val
				node = node.next
				index += 1
			return None
		index, node = -2, self.tail
		while node.prev:
			if index == position:
				val = node.prev.value
				node.prev.prev.next = node
				node.prev = node.prev.prev
				return val
			node = node.prev
			index -= 1


dll = DoublyLinkedList()
dll.insert(5)
dll.insert(10, -1)
dll.insert(15, -1)
dll.insert(20, 3)
print(dll)
# dll.insert(5, 200)
# dll.insert(10, -1)
# dll.insert(15, -1)
# dll.insert(20, 0)
# dll.insert(25, 100)
# dll.insert(30, +30)
# print(dll)
# #
# dll.traverse()
# dll.traverse(reverse = True)
#
# print("Removing element from head")
# del_element = dll.remove_at_position(0)
# print(dll, del_element)
#
# print("Removing element from tail:")
# del_element = dll.remove_at_position(-1)
# print(dll, del_element)
#
# print("Removing the element at index 2: ")
# del_element = dll.remove_at_position(2)
# print(dll, del_element)
#
# dll.traverse()
# dll.traverse(reverse = True)
#
# dll.insert(20)
# # dll.insert(30)
#
# dll.traverse()
# dll.traverse(reverse = True)
#
# print("Removing the second last element: -5 ")
# del_element = dll.remove_at_position(-5)
# print(dll, del_element)
#
# dll.traverse()
# dll.traverse(reverse = True)

# print("Removing the second last element: -2 ")
# del_element = dll.remove_at_position(-2)
# print(dll, del_element)
