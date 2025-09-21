current_year = 2025
name = input("please input your name")
age = int(input("please input your age"))
birth_year = current_year - age
current_tuple = (current_year, birth_year)
total_hobby = 0
hobbies = []
while total_hobby != 3:
    hobby = input("input a hobby please")
    hobbies.append(hobby)
    total_hobby +=1
set_hobby = set(hobbies)
info = {
    "Name": name,
    "Age" : age,
    "Hobbies": set_hobby

}
def main():
   print(f" your name is {info['Name']} your age is {info['Age']} and your hobbies are {info['Hobbies']}")
   print(f" this is the current year and the year you were born in {current_tuple}")

main()
