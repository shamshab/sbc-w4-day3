characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

words =input("Enter a word: ")

value = []
sys = []
tmp = ""

for i in words:
    if i in characters:
        if tmp:
            value.append(tmp.strip())
            sys.append(tmp.strip() + i)
            tmp = ""
        else:
            if sys:
                sys[-1] += i
    else:
        tmp += i
if tmp:
    value.append(tmp.strip())


print(sys)
print(value)