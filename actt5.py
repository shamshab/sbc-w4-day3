user = input("Enter a sentence: ")
lis = []
new = []

for char in user:
    if char.isalpha():
        lis.append(char)
    else:
        if lis:
            new.append("".join(lis))
            lis.clear()

if lis:
    new.append("".join(lis))

print(new)
