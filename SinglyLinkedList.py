class Node:
	def __init__(self, data = 0, nxt = None):
		self.value = data
		self.next = nxt

	def __str__(self):
		return f"({self.value})"


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def __str__(self):
		if not self.head:
			return "Linked List is Empty"
		val = str(self.head)
		n = self.head.next
		while n:
			val += f" ---> {str(n)}"
			n = n.next
		return f"{val}, size = {self.count}"

	def add_head(self, val: Node):
		self.count += 1
		if not self.head:
			self.head = self.tail = val
			return
		val.next = self.head
		self.head = val

	def add_tail(self, val: Node):
		self.count += 1
		if not self.head:
			self.head = self.tail = val
		else:
			self.tail.next = val
			self.tail = self.tail.next  # or val

	def delete(self, val):
		if not self.head:
			print("Linked List is Empty")
			return
		if self.head.value == val.value:
			self.head = self.head.next
			self.count -= 1
			if not self.head:
				self.tail = None
			return
		item = self.head
		while item.next:
			if item.next.value == val.value:
				item.next = item.next.next
				self.count -= 1
				print(f"Deleted Successfully: {val.value}")
				if not item.next:
					self.tail = None
				return
			item = item.next
		else:
			print(f"Value not found = {val.value}")


ll = LinkedList()
print(ll)
print(ll.tail)

ll.add_tail(Node(10))
ll.add_tail(Node(10))
ll.add_tail(Node(10))

print(ll)
print(ll.tail)

print("Adding at Head: 1,2,3")

ll.add_head(Node(1))
ll.add_head(Node(2))
ll.add_head(Node(3))

print(ll)
print("Deleting 30: ")
ll.delete(Node(30))
print(ll)

print("Deleting 3000: ")
ll.delete(Node(3000))
print(ll)

print("-" * 20)
print("Deleting 2: ")
ll.delete(Node(2))
print(ll)

print("Deleting 10 three times: ")
ll.delete(Node(10))
print(ll)
ll.delete(Node(10))
print(ll)
ll.delete(Node(10))
print(ll)

print("Deleting 500: ")
ll.delete(Node(500))
print(ll)
