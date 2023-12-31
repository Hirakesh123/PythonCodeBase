class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)


class ElasticCircularQueue:
	def __init__(self, initial_size = 5):  # O(n), n = size of the Circular Linked List
		self.head = self.tail = None
		self.start = self.stop = None
		self.length = initial_size
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
			# print("Data overflow. Queue is full. Cannot enqueue more.")
			node = Node(value)
			if self.stop == self.tail:
				self.stop.next = node
				self.stop = node
				node.next = self.start

			self.tail.next = node
			node.next = self.head
			self.tail = self.tail.next  # Important
			self.length += 1
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


size = 2
print(f"Created a circular queue of size: {size}")
cq1 = ElasticCircularQueue(size)
print(cq1)

print("Enqueuing: 10")
cq1.enqueue(10)
print(cq1)

print("Enqueuing: 20")
cq1.enqueue(20)
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
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

print("Enqueuing: 100")
cq1.enqueue(100)
print(cq1)

print("Enqueuing: 200")
cq1.enqueue(200)
print(cq1)

print(f"De-queuing: {cq1.dequeue()}")
print(cq1)

print("Enqueuing: 300")
cq1.enqueue(300)
print(cq1)

print("Enqueuing: 400")
cq1.enqueue(400)
print(cq1)

print("Enqueuing: 500")
cq1.enqueue(500)
print(cq1)

print("Enqueuing: 600")
cq1.enqueue(600)
print(cq1)

print("Enqueuing: 700")
cq1.enqueue(700)
print(cq1)

print("Enqueuing: 800")
cq1.enqueue(800)
print(cq1)

# OUTPUT:
# Created a circular queue of size: 2
# ( - - )
# Enqueuing: 10
# ( 10 - )
# Enqueuing: 20
# ( 10 20 )
# De-queuing: 10
# ( - 20 )
# Enqueuing: 30
# ( 30 20 )
# Enqueuing: 40
# ( 30 40 20 )
# Enqueuing: 50
# ( 30 40 50 20 )
# Enqueuing: 60
# ( 30 40 50 60 20 )
# Enqueuing: 70
# ( 30 40 50 60 70 20 )
# De-queuing: 20
# ( 30 40 50 60 70 - )
# De-queuing: 30
# ( - 40 50 60 70 - )
# De-queuing: 40
# ( - - 50 60 70 - )
# De-queuing: 50
# ( - - - 60 70 - )
# De-queuing: 60
# ( - - - - 70 - )
# Queue Reset: Last element dequeued
# De-queuing: 70
# ( - - - - - - )
# Data underflow. Cannot dequeue further as the queue is empty
# De-queuing: None
# ( - - - - - - )
# Enqueuing: 100
# ( 100 - - - - - )
# Enqueuing: 200
# ( 100 200 - - - - )
# De-queuing: 100
# ( - 200 - - - - )
# Enqueuing: 300
# ( - 200 300 - - - )
# Enqueuing: 400
# ( - 200 300 400 - - )
# Enqueuing: 500
# ( - 200 300 400 500 - )
# Enqueuing: 600
# ( - 200 300 400 500 600 )
# Enqueuing: 700
# ( 700 200 300 400 500 600 )
# Enqueuing: 800
# ( 700 800 200 300 400 500 600 )
#
# Process finished with exit code 0