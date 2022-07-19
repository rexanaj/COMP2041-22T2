"""
What other useful types are available with Python's standard library?
"""

from collections import Counter, defaultdict, OrderedDict

# collections.Counter -> normal dictionary, with default values & some extra functions
counter = Counter()
counter['a'] += 1
counter.most_common()

# collections.defaultDict
# Takes in the `list` function. Can be any factory (a function), like `set`
default_dict = defaultdict(list)
default_dict['a'].append("hello")


# collections.OrderedDict
# Maintains the insertion order
ordered_dict = OrderedDict()
ordered_dict['z'] = "COMP1511"
ordered_dict['a'] = "COMP1521"
ordered_dict['k'] = "COMP1531"
ordered_dict['b'] = "COMP2041"
ordered_dict.keys()


# Normal dictionary doesn't maintain order
# Not guaranteed
d = {}
d['b'] = "world"
d['c'] = "hi"
d['a'] = "hello"
d['d'] = "hiya"
