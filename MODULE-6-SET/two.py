#union
A={1,2,3,4}
B={3,4,5,6}
res1=A|B
print(res1)
res2=A.union(B)
print(res2)

#intersection
A1={1,2,3,4}
B1={3,4,5,6}
res11=A1 & B1
print(res11)
resl2=A1.intersection(B1)
print(resl2)

#differnece
A2={1,2,3,4}
B2={3,4,5,6}
resl12=A2-B2
resl13=B2-A2
print(resl12, resl13)
ress1=A2.difference(B2)
ress2=B2.difference(A2)
print(ress1 , ress2)