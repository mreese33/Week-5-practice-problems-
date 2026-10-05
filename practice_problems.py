"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False

# I chose a set because it keeps track of the product IDs that have already been seen.
# It checks and adds IDs in O(1) time on average, and going through the full list is O(n).
# This makes it easy to find a duplicate without checking every ID against each other.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop(0)

# I chose a queue because the tasks need to stay in the order they were added.
# Adding a task to the end is O(1), while removing the first task from this list is O(n).
# This works because the oldest task is always the first one removed.

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

# I chose a set because it only keeps unique values and does not add duplicates.
# Adding a value is O(1) on average, and getting the number of unique values is O(1).
# This makes it easy to keep track of how many different values have been added.

print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")

print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)

print(tracker.get_unique_count())