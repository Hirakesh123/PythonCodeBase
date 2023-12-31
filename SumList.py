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

	def insert(self, value, position = 0):
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


def sum_list(n1, n2) -> DoublyLinkedList:
	ll1, ll2 = n1.head, n2.head
	ans = DoublyLinkedList()
	carry = 0
	while ll1 or ll2:
		v1 = ll1.value if ll1 else 0
		v2 = ll2.value if ll2 else 0
		s = v1 + v2 + carry
		carry = s // 10  # This is important as it is NOT Java
		s %= 10
		ans.insert(s, -1)
		ll1 = ll1.next if ll1 else None
		ll2 = ll2.next if ll2 else None
	if carry != 0:
		ans.insert(carry, -1)
	return ans


a = DoublyLinkedList()
b = DoublyLinkedList()

a.insert(33)

b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)
b.insert(9)

c = sum_list(a, b)

aa = a.traverse(reverse = True)
bb = b.traverse(reverse = True)
cc = c.traverse(reverse = True)

print(f"{aa} + {bb} + {cc}")
