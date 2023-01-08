A={0, 3, 4, 5, 7, 9, 11, 18, 47}
B={5, 7, 47}
print("A>B",B)
print("A<B",A<B)
print("A>=B",A>=B)
print("A<=B",A<=B)
print("A==B",A==B)
print("A!=B",A!=B)
print("A^B",A^B)
print("A & B",A&B)
print("A - B",A-B)
print("B - A",B-A)


A={3, 6, 7, 8, 10, 12, 14, 21, 50}
B={8, 10, 50,61}

print(3 in A)
print(8 not in B)
print(A.issubset(B))
print(B.issubset(A))
print(A.issuperset(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))
print(A.union(B))
print(A.intersection(B))
A.update(B)
print(A)

