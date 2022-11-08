s="P Y T H O N"

# 1 способ
print(s[::2])

# 2 способ
print(s.replace(' ', ''))

# 3 способ
for i in s:
    if i != " ":
        print(i,end="")

