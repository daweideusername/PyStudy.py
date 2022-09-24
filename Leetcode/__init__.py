#https://www.runoob.com/python/python-func-enumerate.html
inorder = ['a','b','c','d']
index = {element: i
         for i, element in enumerate(inorder)}
print(index)
for i ,element in enumerate(inorder):
    print(i,element)

print(enumerate(inorder))