class CircularQueue:
	def __init__(self, max_size = 10):
		self.data = []
		self.data.extend(["-"] * max_size)
		self.head, self.tail = -1, -1
		self.MAX_SIZE = max_size

	def __str__(self):
		return "[" + " ".join([str(item) for item in self.data]) + "]"

	# both head and tail will propagate forward for dequeue and enqueue operations respectively.

	def enqueue(self, value):
		# element should be inserted at tail, advancing one index post insertion
		# Data overflow will occur when, tail, advanced by one index, equals to head
		# Important
		if self.tail == -1:
			self.tail = self.head = 0
			self.data[0] = value
			return
		tmp_tail = (self.tail + 1) % self.MAX_SIZE
		if tmp_tail == self.head:
			print("Data Overflow. Queue is already full.")
		else:
			self.tail = tmp_tail
			self.data[self.tail] = value

	def dequeue(self):
		# element should be deleted from head, advancing one index post deletion
		# Queue will be reset when, head == tail.
		# The last element shall be deleted
		# Following which, self.head = self.tail = -1
		# Data underflow will occur when self.head = -1
		# Important
		if self.head == -1:
			print("Data underflow. No element to delete.")
			return None
		value = self.data[self.head]
		self.data[self.head] = "-"

		if self.head == self.tail:
			print("Queue has been reset")
			self.head = self.tail = -1
		else:
			self.head = (self.head + 1) % self.MAX_SIZE

		return value


q1 = CircularQueue(5)
print(q1)

print("Queuing: 10")
q1.enqueue(10)
print(q1)

print("Queuing again: 20")
q1.enqueue(20)
print(q1)

print("Queuing again: 30")
q1.enqueue(30)
print(q1)

print("Queuing again: 40")
q1.enqueue(40)
print(q1)

print("Queuing again: 50")
q1.enqueue(50)
print(q1)

print("Queuing again: 60")
q1.enqueue(60)
print(q1)


print(f"De-queuing: {q1.dequeue()}")
print(q1)
print(f"De-queuing: {q1.dequeue()}")
print(q1)

print("Queuing again: 100")
q1.enqueue(100)
print(q1)

print(f"De-queuing: {q1.dequeue()}")
print(q1)

print(f"De-queuing: {q1.dequeue()}")
print(q1)

print(f"De-queuing: {q1.dequeue()}")
print(q1)

print(f"De-queuing: {q1.dequeue()}")
print(q1)

# OUTPUT:
#
# [- - - - -]
# Queuing: 10
# [10 - - - -]
# Queuing again: 20
# [10 20 - - -]
# Queuing again: 30
# [10 20 30 - -]
# Queuing again: 40
# [10 20 30 40 -]
# Queuing again: 50
# [10 20 30 40 50]
# Queuing again: 60
# Data Overflow. Queue is already full.
# [10 20 30 40 50]
# De-queuing: 10
# [- 20 30 40 50]
# De-queuing: 20
# [- - 30 40 50]
# Queuing again: 100
# [100 - 30 40 50]
# De-queuing: 30
# [100 - - 40 50]
# De-queuing: 40
# [100 - - - 50]
# De-queuing: 50
# [100 - - - -]
# Queue has been reset
# De-queuing: 100
# [- - - - -]
#
# Process finished with exit code 0
