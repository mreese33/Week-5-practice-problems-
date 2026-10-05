# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
# Question 7: First Repeated Value
# Return the first value that appears more than once in a collection.

def first_repeated_value(values):
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None

print(first_repeated_value([1, 2, 3, 2, 4]))
print(first_repeated_value([5, 6, 7, 8]))
print(first_repeated_value([]))
