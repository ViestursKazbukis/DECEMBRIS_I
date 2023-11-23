ievaditaisskaitlis=int(input("Ievadi skaitli: "))

summa = 0

for skaitlis in range(1,ievaditaisskaitlis+1):
    summa += skaitlis

print(f"Skaitļus summa no 1 līdz {ievaditaisskaitlis} ir: {summa}")