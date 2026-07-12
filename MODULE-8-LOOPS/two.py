# for i in range(1,11,1):
#     print(i)

scores=[2,45,102,4,9,12,45,90,1,0,1]
sum=0;
minimum=scores[0]
maximum=scores[0]
for score in scores:
    sum+=score;
    if(minimum>score):
        minimum=score
    
    if(maximum<score):
        maximum=score


print(f"The sum of the list is the {sum}")
print(f"The maximum number in the list is the {maximum}")
print(f"The minimum number in the list is the {minimum}")