sentence = input("Enter a String: ")
value = []
tmp = ""

for i in sentence:
    if i == " ":
        value.append(tmp)
        tmp = ""
    else:
        tmp += i
if tmp:
    value.append(tmp)


print(value)