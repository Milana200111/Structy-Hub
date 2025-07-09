## is binary search tree

Write a function, *is\_binary\_search\_tree*, that takes in the root of a binary tree. The function should
return a boolean indicating whether or not the tree satisfies the *binary search tree* property.

A [Binary Search Tree](https:#en.wikipedia.org/wiki/Binary_search_tree) is a binary tree where all
values within a node's left subtree are smaller than the node's value and all values in a node's
right subtree are greater than the node's value.

#### test_00:

```python
a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> True
```

#### test_01:

```python
a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(15)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19

is_binary_search_tree(a) # -> False
```

#### test_02:

```python
a = Node(12)
b = Node(5)
c = Node(15)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     15
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> True
```

#### test_03:

```python
a = Node(12)
b = Node(5)
c = Node(10)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     10
#  / \     \
# 3   9     19

is_binary_search_tree(a) # -> False
```

#### test_04:

```python
q = Node(54)
r = Node(42)
s = Node(70)
t = Node(31)
u = Node(50)
v = Node(72)
w = Node(47)
x = Node(90)

q.left = r
q.right = s
r.left = t
r.right = u
s.right = v
u.left = w
v.right = x

#       54
#     /    \
#    42     70
#   / \      \
# 31   50     72
#     /        \
#    47         90

is_binary_search_tree(q) # -> True
```
