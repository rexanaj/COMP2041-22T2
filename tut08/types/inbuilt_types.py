"""
What types are avalible as inbuilt types in Python?
"""

# int
# Common use:
age = int(input("What is your age? "))

# float
# Common use:
weight = float(input("What is your weight? "))

# str
num = str(1)

# dict -> key, value pairs
d1 = dict()  # Define an empty dictionary
d2 = {"key": "value"}
d2["hello"] = "world"

# list -> ordered sequence
l1 = list()
l2 = ["hi", "hello", "world"]
l2.append('helloagain')

# tuple -> immutable list
t1 = tuple()
t2 = (1, 2, 3)

# set -> unordered, unique elements
s1 = set()
s1 = {1, 2, 3}
s1.add(3)


# frozenset -> immutable set
f = frozenset()  # "read-only", "const"
