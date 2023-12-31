class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)


class StaticCircularQueue:  # Fix-sized Queue
	def __init__(self, max_size = 5):  # O(n), n = size of the Circular Linked List
		self.head = self.tail = None
		self.start = self.stop = None
		self.length = max_size
		x = 1
		node = Node("-")
		self.start = node
		curr_node = self.start
		while x < self.length:
			node = Node("-")
			curr_node.next = node
			curr_node = curr_node.next
			x += 1

		self.stop = curr_node
		self.stop.next = self.start

	def __str__(self):
		contents = "( "
		curr_node = self.start
		while True:
			contents += f"{curr_node.value} "
			if curr_node == self.stop:
				break
			curr_node = curr_node.next
		contents += ")"
		return contents

	def is_full(self):
		return self.tail and self.tail.next == self.head

	def is_empty(self):
		return not self.head

	def enqueue(self, value):
		if self.is_empty():
			self.head = self.tail = self.start
			self.head.value = value
		elif self.is_full():
			print("Data overflow. Queue is full. Cannot enqueue more.")
		else:
			self.tail.next.value = value
			self.tail = self.tail.next
		return

	def dequeue(self):
		if self.is_empty():
			print("Data underflow. Cannot dequeue further as the queue is empty")
			return None
		value = self.head.value
		if self.head == self.tail:
			print("Queue Reset: Last element dequeued")
			self.head.value = "-"
			self.head = self.tail = None
		else:
			self.head.value = "-"
			self.head = self.head.next
		return value


size = 5
print(f"Created a circular queue of size: {size}")
cq1 = StaticCircularQueue(size)
print(cq1)

print("Enqueuing: 10")
cq1.enqueue(10)
print(cq1)

print("Enqueuing: 20")
cq1.enqueue(20)
print(cq1)

print("Enqueuing: 30")
cq1.enqueue(30)
print(cq1)

print("Enqueuing: 40")
cq1.enqueue(40)
print(cq1)

print("Enqueuing: 50")
cq1.enqueue(50)
print(cq1)

print("Enqueuing: 60")
cq1.enqueue(60)
print(cq1)

print("Enqueuing: 70")
cq1.enqueue(70)
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)


# OUTPUT:
# Created a circular queue of size: 6
# ( - - - - - - )
# Enqueuing: 10
# ( 10 - - - - - )
# Enqueuing: 20
# ( 10 20 - - - - )
# Enqueuing: 30
# ( 10 20 30 - - - )
# Enqueuing: 40
# ( 10 20 30 40 - - )
# Enqueuing: 50
# ( 10 20 30 40 50 - )
# Enqueuing: 60
# ( 10 20 30 40 50 60 )
# Enqueuing: 70
# Data overflow. Queue is full. Cannot enqueue more.
# ( 10 20 30 40 50 60 )
# De-queuing: 10
# ( - 20 30 40 50 60 )
# De-queuing: 20
# ( - - 30 40 50 60 )
# De-queuing: 30
# ( - - - 40 50 60 )
# De-queuing: 40
# ( - - - - 50 60 )
# De-queuing: 50
# ( - - - - - 60 )
# Queue Reset: Last element dequeued
# De-queuing: 60
# ( - - - - - - )
# Data underflow. Cannot dequeue further as the queue is empty
# De-queuing: None
# ( - - - - - - )
#
# Process finished with exit code 0
