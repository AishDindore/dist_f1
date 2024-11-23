first_name="aishwarya"
last_name="dindore"
print(len(first_name))
print(type(last_name))

# my firstName is sarika and my lastName is pansare
fn="aishwarya"
ln="dindore"
print(f"my first name is",fn,"and my last name is",ln)


fn="aishwarya"
ln="dindore"

# does string does the value by index
print(fn[0])


# how to loop over string - for , for -range , while loop
for x in fn:
    print(x)

for x in range(len(fn)):
    print(fn[x])