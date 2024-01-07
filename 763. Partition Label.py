from collections import defaultdict

s = "ababcbacadefegdehijhklij"
#s = "eccbbbbdec"

di = defaultdict(list)
for index,value in enumerate(s):
    di[value].append(index)

start, end = 0, 0
partitions = []
for i, char in enumerate(s):
    last_index = max(di[char])
    end = max(end, last_index)

    if i == end:
        partitions.append(i - start + 1)
        start = i + 1

print(partitions)
print(di)

