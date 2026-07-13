def arithmetic(nums1,nums2):
    add=nums1+nums2
    sub=nums1-nums2
    multi=nums2*nums1
    div=nums1/nums2
    module=nums1%nums2
    return add,sub,multi,div,module

val1=int(input("Enter the number1"))
val2=int(input("Enter the number2"))
res1,res2,res3,res4,res5=arithmetic(val1,val2)
print(res1,res2,res3,res4,res5)