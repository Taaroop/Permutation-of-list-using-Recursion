string = str(input())
li= list(string)

def perm(li):
    if len(li) == 0:
        return []
    elif len(li) == 1:
        return [li]
    else:
        final_li = []
        for i in range(len(li)):
            first_char = li[i]
            rem_li = li[:i] + li[(i+1):]
            for p in perm(rem_li):
                final_li.append([first_char] + p)
        
        return final_li

# Test

count = 0
output = perm(li)
for lst in output:
    print(lst)
    count += 1
print("Count:", count)