class Queue:
	def __init__(self):
		self.data = []

	def __str__(self):
		return "The queue is: ( " + " ".join([str(item) for item in self.data]) + " )"

	def __iter__(self):
		for item in self.data:
			yield item

	def is_empty(self):
		return len(self.data) == 0

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		if not self.is_empty():
			return self.data.pop(0)  # O(n)
		else:
			print("Data Underflow. Cannot dequeue as no data is present")
			return None

	def peek(self):
		if not self.is_empty():
			return str(self.data[-1])
		else:
			print("Cannot peek as the list is empty")
			return None

	def clean(self):
		print("The queue has been reset")
		self.data = []


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)


print(f"Peeking: {q1.peek()}")

print(q1)

odd_queue = Queue()
even_queue = Queue()

while not q1.is_empty():
	element = q1.dequeue()
	if element % 20 == 10:
		even_queue.enqueue(element)
	else:
		odd_queue.enqueue(element)

print("Odd-queue: ")
print(odd_queue)

print("Even-queue: ")
print(even_queue)
