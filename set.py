# sets can not store duplicate values(list can store duplicate values)
setA={11,22,33,44,55}
print(setA)

setB={44,55,66,77,88,44,55}
print(setB)

## sets methods
#add() add elements in set
setB={44,55,66,77,88}
setB.add(99)
print(setB)

##pop() removes the last element
setB={44,55,66,77,88}
setB.pop()
print(setB)

##remove() removes the specified element
setA={11,22,33,44,55}
setA.remove(55)
print(setA)

##clear() removes all elements from set
setA={11,22,33,44,55}
setA.clear()
print(setA)


## update() add elements in set
setD = {11,22,33,44}
setD.update([55,66,77,88])
setD.update((99,100))
setD.update({101,102})
print(setD)