class Stack:
	def __init__(self):
		self.data = []

	def __str__(self):
		return "\n".join([str(item) for item in self.data[::-1]])

	def __iter__(self):
		for item in self.data:
			yield item

	def is_empty(self):
		return len(self.data) == 0

	def push(self, item):
		self.data.append(item)

	def pop(self):
		if not self.is_empty():
			return self.data.pop()
		else:
			return None

	def peek(self):
		if not self.is_empty():
			return self.data[-1]


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

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
