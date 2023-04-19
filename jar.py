# The Jar class represents a jar that can hold a certain number of cookies and allows for depositing
# and withdrawing cookies.
# The class Jar represents a jar that can hold a certain number of cookies and allows for depositing
# and withdrawing cookies.
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0
    
    def __str__(self):
        return "🍪" * self._cookies
    
    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount to deposit must be a non-negative integer.")
        if self._cookies + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar can hold.")
        self._cookies += n
    
    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount to withdraw must be a non-negative integer.")
        if self._cookies - n < 0:
            raise ValueError("Cannot withdraw more cookies than are in the jar.")
        self._cookies -= n
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._cookies
