import keyword
keys = ("except", "raise", "fall")
for i in range(len(keys)) :
    if keyword.iskeyword(keys[i]) :
        print(keys[i] + ": True")
    else :
        print(keys[i] + ": False")
