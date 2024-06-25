# Tuple values not changes
sampleTuple = tuple((1,2,4,2,5,6,2,7))
alsoTuple = (1,2,4,2,5,6,2,7)


print(sampleTuple.count(2))
(a, *b, c) = sampleTuple

print(a)
print(b)
print(c)