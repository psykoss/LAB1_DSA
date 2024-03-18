class DNode:
	def __init__(self, e, prev=None, next=None):
		self.elem = e
		self.prev = prev
		self.next = next

class DList:
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0
		