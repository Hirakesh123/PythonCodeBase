class Stack:
	def __init__(self, max_size = 10):
		self.data = []
		self.MAX_SIZE = max_size
		self.length = 0

	def __str__(self):
		return "\n".join([str(item) for item in self.data[::-1]])

	def __iter__(self):
		for item in self.data:
			yield item

	def is_empty(self):
		return len(self.data) == 0

	def push(self, item):
		if len(self.data) < self.MAX_SIZE:
			self.data.append(item)
		else:
			print(f"Data over-flow. Cannot push as the Stack has reached the max limit = {self.MAX_SIZE} elements ")

	def pop(self):
		if not self.is_empty():
			return self.data.pop()
		else:
			return None

	def peek(self):
		if not self.is_empty():
			return self.data[-1]


s1 = Stack(5)
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(70)


print(s1)
print("Peeking into s1: ")
print(s1.peek())

print("Checking whether the stack is empty or not")
print(s1.is_empty())

print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

print("Peeking into s1 again after several pop operations.")
print(s1.peek())

print("Checking whether the stack is empty")
print(s1.is_empty())
