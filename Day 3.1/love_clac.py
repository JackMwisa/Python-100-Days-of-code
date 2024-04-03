# true x love

print("Welcome to the love calculator: ")
name1 = input("What is your name: \n").lower()
name2 = input("What is their name: \n").lower()

print(" ")

t = name1.count("t") + name2.count("t")
print(f"T occUrs {t} times")

r = name1.count("r") + name2.count("r")
print(f"R occurs {r} times")

u = name1.count("u") + name2.count("u")
print(f"U occurs {u} times")

e = name1.count("e") + name2.count("e")
print(f"E occurs {e} times \n")


# print(type(t))

l = name1.count("t") + name2.count("t")
print(f"L occUrs {l} times")

o = name1.count("o") + name2.count("o")
print(f"O occurs {o} times")

v = name1.count("v") + name2.count("v")
print(f"V occurs {v} times")

e2 = e
print(f"E occurs {e2} times \n")

percent1 = t+r+u+e
percent2 = l+o+v+e2
score = str(percent1) + str(percent2)

score_int = int(score) 


if score_int < 10 and score_int > 90:
    print(f"your score is {score_int}, you go together like coke and mentos!")
elif score_int >=40 and  score_int <=50:
        print(f"your score is {score_int}, you are alright together!")
else:
    print(f"Your score is {score_int}!")
