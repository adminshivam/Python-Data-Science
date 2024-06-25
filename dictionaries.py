# Dictonaries
sample = {"abc": "abc", "def": "def"}

print(sample["abc"])
print(sample.get("def"))
print(sample.items());

if("abc" in sample):
  print(sample["abc"])
else:
  print("not found abc")

# copying the dictionary
newDic = sample.copy()
newDic = dict(sample)

print(sample.values())