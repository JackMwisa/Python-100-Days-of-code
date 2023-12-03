
print("Welcome to the love calculator!")

name1 = input("What is your name? \n")
name1 = name1.lower()
name2 = input("What is their name? \n").lower()
name2 = name2.lower()



t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")

print(f"T occurs {t} times")
print(f"R occurs {r} times")
print(f"U occurs {u} times")
print(f"E occurs {e} times")


print("")
total_tr = t + r + u + e


print(f"L occurs {l} times")
print(f"O occurs {o} times")
print(f"V occurs {v} times")
print(f"E occurs {e2} times")

total_lo = l + o + v + e2

final = str(total_tr) + str(total_lo)

final_int = int(final)


if (final_int > 10) or (final_int < 90):
    print(f"Your score is {final} you go together like coke and mentos")
elif (final_int >= 40) and (final_int <= 50):
    print(f"Your score is {final}, You are alright together")
else:
    print(f"Your score is {final} ")