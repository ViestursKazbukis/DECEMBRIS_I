skaitlis=int(input("Ievadi skaitli faktoriālam: "))

faktorials=1

for skaitlis2 in range(1, skaitlis+1):
    faktorials *=skaitlis2

print(f"Faktoriāls tavam ievadītajam skaitlim {skaitlis} ir {faktorials}")