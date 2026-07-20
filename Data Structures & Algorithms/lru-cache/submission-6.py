class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value

        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0,0)

        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):

        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = nxt
        prev.next = nxt.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt 
        nxt.prev = prev
    
            

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        




# Design a queue with a fixed maximum capacity, "set" at construction.

# q = BoundedQueue(capacity=3)
# Operations:

# enqueue(x) — add to the back. Define what happens when full.
# dequeue() — remove and return the front. Define what happens when empty.
# peek() — return the front without removing. Empty case?
# size() / is_empty() / is_full()


# class BoundedQueue:

#     def __init__(self, capacity):

#         self.capacity = capacity
#         self.store = [None] * capacity

#         self.head = 0
#         self.tail = 0
#         self.current_size = 0

    
#     def enqueue(self, x) -> None:

        
#         if self.current_size >= self.capacity:
#             return False
        
#         else:
#             self.store[self.tail] = x
#             self.current_size += 1
#             self.tail = (self.tail + 1) % self.capacity
#             return True
    
#     def dequeue(self):

#         if self.current_size == 0:
#             return None
        
#         elem = self.store[self.head]
#         self.head = (self.head + 1) % self.capacity
#         self.current_size -= 1
#         return elem
       
    
#     def peek(self):

#         if self.isEmpty():
#             return None     
#         else:
#             return self.store[self.head]

#     def size(self):
#         return self.current_size
    
#     def isEmpty(self):
#         return self.current_size == 0
    
#     def is_full(self):

#         return self.current_size == self.capacity


# Problem 2 — Rolling Request Counter (~40 min)
# You are building rate-limiting infrastructure for an API. 
# Implement a class that tracks requests per user and answers "how many requests has this user made in the last 60 seconds?"
# counter = RequestCounter(window_seconds=60)
# counter.record_request(user_id="u1", timestamp=100)
# counter.record_request(user_id="u1", timestamp=130)
# counter.record_request(user_id="u2", timestamp=140)
# counter.get_count(user_id="u1", timestamp=159)  # → 2
# counter.get_count(user_id="u1", timestamp=161)  # → 1  (the t=100 request expired)

# Requirements:
# Timestamps arrive in non-decreasing order (say out loud why this assumption matters — and what breaks without it).
# get_count counts requests in (timestamp - 60, timestamp].
# Memory should not grow forever — old requests must be evictable somehow.

# class RequestCounter:

#     def __init__(self, window_seconds):
#         self.window_seconds = window_seconds

#         self.counter = {} # users : [queue of requests]
    
#     def record_request(self, user_id, timestamp):

#         if user_id not in self.counter:
#             self.counter[user_id] = deque()
        
#         self.counter[user_id].append(timestamp)
#         return True
    
#     def get_count(self, user_id, timestamp):

#         requests = []

#         if user_id not in self.counter:
#             return 0
        
#         user_queue = self.counter[user_id]
#         cutoff = timestamp - self.window_seconds

#         while len(user_queue) > 0 and user_queue[0] <= cutoff:
#             user_queue.popleft()
            
        
#         return len(user_queue)

    

# Implement a token bucket: a user gets capacity tokens; each request consumes one; 
# tokens refill at refill_rate per second up to capacity.
# limiter = TokenBucket(capacity=10, refill_rate=2)  # 2 tokens/sec
# limiter.allow_request(timestamp=0)   # → True (bucket starts full)

# allow_request(timestamp) → True and consume a token if available, else False.
# Refill is computed lazily — no background threads: on each call, figure out how many tokens accrued since the last call.
# Tokens can be fractional internally; a request needs ≥ 1.

# class TokenBucket:

#     def __init__(self, capacity, refill_rate):

#         self.capacity = capacity
#         self.refill_rate = refill_rate

#         self.last_updated = 0
#         self.current_tokens = capacity

#     def allow_request(self, timestamp) -> bool:

#         time_elapsed = timestamp  -  self.last_updated
#         new_tokens = time_elapsed * self.refill_rate
#         self.current_tokens = min(self.capacity, self.current_tokens + new_tokens)
#         self.last_updated = timestamp

#         if self.current_tokens >= 1:
#             self.current_tokens -= 1
#             return True
        
#         else:
#             return False
