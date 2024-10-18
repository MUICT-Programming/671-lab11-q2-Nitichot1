n=int(input())
lst1=[]
lst2=[]

for i in range(n):
    lst_1=int(input())
    lst1.append(lst_1)
for j in range(n):
    lst_2=int(input())
    lst2.append(lst_2)


def summation(lst1,lst2):
    updated_list=[]
    for i in range(n):
        sum=lst1[i]+lst2[i]
        updated_list.append(sum)
    return updated_list

upd_lst=summation(lst1,lst2)
print(upd_lst)


def find_min_max(upd_lst):
    min_val = min(upd_lst)
    max_val = max(upd_lst)
    return min_val, max_val

lst_min_max=find_min_max(upd_lst)
print(lst_min_max)
