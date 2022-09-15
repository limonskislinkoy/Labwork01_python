# Part  Int
print("============================================================")
test_var = 256
print(f"Now test_var is ||INTeger|| and contain number = {test_var}")
print(f"Sqrt of our number is = {test_var**0.5}")
print(f"Our number + 10 = {test_var+10}")
print(f"Our number - 10 = {test_var-10}")
print(f"Our number * 10 = {test_var*10}")


#Part Str
print("============================================================")
test_var = "hello"
print(f"Now test_var is ||STRing|| and contain word = '{test_var}'")
print(f"This function check if all of letter in the word are digits = {test_var.isdigit()}")
print(f"Our word with title letter - {test_var.title()}")
print(f"Count of 'l' in out word = {test_var.count('l')}")
print(f"This function check if all of letter in the word is ascii = {test_var.isascii()}")

#Part Str - more than one word
print("============================================================")
test_var = "hello, i`m limonskislinkoy"
print(f"Now test_var is ||STRing|| and contain words = '{test_var}'")
print(f"This function split our string to list of words = {test_var.split()}")
print(f"This function return len of our string(include spaces) = {len(test_var)}")
print(f"This function return out string, but all of letter is upper - {test_var.upper()}")
print(f"Index of comma in out string = {test_var.index(',')}")

#Part list
print("============================================================")
test_var = [0,5,2,1,3,4]
print(f"Now test_var is ||List|| and contain numbers = {test_var}")
print(f"This function return sorted list - {sorted(test_var)}")
print(f"This function return reversed sort - {list(reversed(sorted(test_var)))}")
print(f"This function return reversed list - {list(reversed(test_var))}")
print(f"Len of our list = {len(test_var)}")

#Part tuple
print("============================================================")
test_var = (0,5,2,1,3,4)
print(f"Now test_var is ||Tuple|| and contain numbers = {test_var}")
print(f"This function return index of number - 3 - {test_var.index(3)}")
print(f"This function return size of out tuple in bytes(why so much? usually integer is 4 bytes, but in tuple every new element addition 8 bytes + 40 bytes by start) - {test_var.__sizeof__()}")
print(f"This function return elements with index in range(2,4) - {test_var[2:4]}")
print(f"Len of our  = {len(test_var)}")