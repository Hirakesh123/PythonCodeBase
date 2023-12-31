import random


class Node:
	def __init__(self, value):
		self.value = value
		self.next = self.prev = None

	def __str__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = self.tail = None

	def add(self, value):
		node = Node(value)
		if not self.head:
			self.head = self.tail = node
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node

	def delete(self):
		if not self.head:
			print("Linked List Underflow. Cannot delete as the list is empty")
			return
		val = self.tail.value
		self.tail = self.tail.prev
		self.tail.next = None
		return val

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def __str__(self):
		values = [str(item) for item in self]
		return "-->".join(values)

	def __len__(self):
		ans = 0
		node = self.head
		while node:
			ans += 1
			node = node.next
		return ans

	def count_odd(self):
		odd = 0
		for item in self:
			if item % 2 == 1:
				odd += 1
		return odd

	def random_generate(self, n, min_value, max_value):
		self.head = self.tail = None
		for x in range(n):
			num = random.randint(min_value, max_value)
			node = Node(num)
			self.add(node)

	def random_unique_generate(self, n, min_value, max_value):
		self.head = self.tail = None
		num_list = []
		while len(num_list) != n:
			num = random.randint(min_value, max_value)
			if num not in num_list:
				num_list.append(num)
				node = Node(num)
				self.add(node)

	def is_unique(self):

		obj_set = set()
		for item in self:
			obj_set.add(item)
		return len(self) == len(obj_set)


def remove_duplicates(ll: LinkedList) -> LinkedList:
	if not ll.head:
		print("linked List is empty")
		return ll
	obj_list = []
	node = ll.head
	obj_list.append(node.value)
	while node.next:
		if node.next.value in obj_list:
			node.next = node.next.next
			if node.next:
				node.next.prev = node
			else:
				ll.tail = node
		else:
			obj_list.append(node.next.value)
			node = node.next
	return ll


def remove_duplicates1(ll: LinkedList) -> None:
	node = ll.head
	while node != ll.tail:
		curr_node = ll.head
		while True:
			if node.next.value == curr_node.value:
				node.next = node.next.next
				if node.next:
					node.next.prev = node
				else:
					ll.tail = node
				break
			if node == curr_node:
				node = node.next
				break
			curr_node = curr_node.next


def remove_duplicates2(ll: LinkedList) -> None:
	# we need to traverse from head till tail.prev
	# for each element, we need to ensure that it is not present else where from the next node till the end of the list
	curr_node = ll.head
	while curr_node and curr_node != ll.tail:
		tmp_node = curr_node
		while tmp_node and tmp_node != ll.tail:
			if tmp_node.next.value == curr_node.value:
				tmp_node.next = tmp_node.next.next
				if tmp_node.next:
					tmp_node.next.prev = tmp_node
				else:
					ll.tail = tmp_node
					break

			tmp_node = tmp_node.next
		print(ll)
		curr_node = curr_node.next


def remove_duplicates3(ll: LinkedList) -> None:
	curr_node = ll.head
	while curr_node != ll.tail:
		tmp_node = curr_node
		while tmp_node != ll.tail:
			if tmp_node.next.value == curr_node.value:
				tmp_node.next = tmp_node.next.next
				if tmp_node.next:
					tmp_node.next.prev = tmp_node
				else:
					ll.tail = tmp_node
			else:
				tmp_node = tmp_node.next
				# tmp_node should not be stepped unconditionally.
				# This should be stepped forward if the next element is not to be deleted
		# print(ll)
		if curr_node.next:
			curr_node = curr_node.next
		else:
			break


def nth_to_last(ll: LinkedList, n: int) -> (Node, Node):
	"""
	Return Last n elements of the linked list
	if n is greater than the length of the linked list, return the whole linked list.
	:param ll: the linked list object
	:param n: number of elements to be returned from last
	:return: the node address from where, there are n nodes if counted till end
	"""
	if not ll.head:
		return
	start_node = ll.head
	count, curr_node = 1, ll.head

	while count != n:
		if curr_node == ll.tail:
			break
		else:
			count += 1
			curr_node = curr_node.next
	else:
		while curr_node != ll.tail:
			curr_node = curr_node.next
			start_node = start_node.next
		return start_node, ll.tail
	return ll.head, ll.tail


l_list = LinkedList()

l_list.add(11)
l_list.add(11)
l_list.add(11)
l_list.add(11)
l_list.add(11)
l_list.add(11)
l_list.add(12)
l_list.add(19)
l_list.add(20)
l_list.add(17)
l_list.add(15)
l_list.add(29)
l_list.add(13)
l_list.add(11)
l_list.add(11)


print(l_list)
print(f"Is unique: {l_list.is_unique()}")
remove_duplicates3(l_list)
print(l_list)
print(f"Is unique: {l_list.is_unique()}")

start, stop = nth_to_last(l_list, 100)
while True:
	print(f"{start.value}", end = "==>")
	if start == stop:
		break
	else:
		start = start.next
