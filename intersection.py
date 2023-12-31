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
		# print("**" * 20)
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


def intersection(la, lb):
	if not la.head or not lb.head:
		return None, "Either one or both lists are empty"
	l_la, l_lb = len(la), len(lb)
	print(f"Length of la = {l_la}, lb = {l_lb}")
	na, nb = la.head, lb.head
	if na == nb:
		return na, "Lists are identical"
	while l_la != l_lb:
		# This loop ensures that there are n nodes left from tail, for both
		if l_la > l_lb:
			l_la -= 1
			na = na.next
		else:
			l_lb -= 1
			nb = nb.next
	if na == nb:
		# first of all, we need to understand that,
		# only one list would be updated in the above loop.
		# So definitely, either one of them is pointing to the head
		# if head of any list is present in the other list.
		if len(la) > len(lb):
			return na, f"{lb}is the subset of{la}"
		else:
			return na, f"{la}is the subset of{lb}"
	while na != nb:
		# This loop ensures that now we have got the point of intersection
		# after its completion
		na = na.next
		nb = nb.next
	if not na:
		# it is important to understand that, in the above loop,
		# both na and nb are progressing equally.
		# and are equal to each other
		# if na is None, nb is also None
		# as both are having equal number of nodes to the left.
		# we could have also written if not nb instead of na
		return None, "The Lists are disjoint"
	return na, "Lists are over-lapping"


laa, lbb = SinglyLinkedList(), SinglyLinkedList()
laa.insert(10)
laa.insert(20)
laa.insert(30)
laa.insert(40)
laa.insert(50)

lbb.insert(100)
lbb.insert(200)
lbb.insert(300)
lbb.tail.next = laa.head.next.next.next
lbb.tail = laa.tail
lbb.insert(50, 0)

lcc = SinglyLinkedList()
lcc.head = laa.head.next.next
lcc.tail = laa.tail


ldd = SinglyLinkedList()
ldd.insert(12)
ldd.insert(23)
ldd.insert(34)
ldd.insert(45)
ldd.insert(56)

lee = SinglyLinkedList()

# print(laa)
# print(lbb)
# print(lcc)
# print(ldd)
# print(lee)

ll_list = [laa, lbb, lcc, ldd, lee]

for ll_item in ll_list:
	print("--" * 15)
	i_node, msg = intersection(laa, ll_item)
	i_value = i_node.value if i_node else None
	print(f"Value of Intersection: {laa} to {ll_item} = {i_value}")
	print(msg)

# Output:
# ------------------------------
# Length of la = 5, lb = 5
# Value of Intersection: [10-->20-->30-->40-->50] to [10-->20-->30-->40-->50] = 10
# Lists are identical
# ------------------------------
# Length of la = 5, lb = 6
# Value of Intersection: [10-->20-->30-->40-->50] to [50-->100-->200-->300-->40-->50] = 40
# Lists are over-lapping
# ------------------------------
# Length of la = 5, lb = 3
# Value of Intersection: [10-->20-->30-->40-->50] to [30-->40-->50] = 30
# [30-->40-->50]is the subset of[10-->20-->30-->40-->50]
# ------------------------------
# Length of la = 5, lb = 5
# Value of Intersection: [10-->20-->30-->40-->50] to [12-->23-->34-->45-->56] = None
# The Lists are disjoint
# ------------------------------
# Value of Intersection: [10-->20-->30-->40-->50] to [] = None
# Either one or both lists are empty
#
# Process finished with exit code 0
