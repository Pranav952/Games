print("welcome to love calculator")

first_name = input("Enter the first person name")
second_name = input("Enter the second person name")
combined_name = first_name + second_name
lower_case_combined_name = combined_name.lower()

t=lower_case_combined_name.count("t")
r=lower_case_combined_name.count("r")
u=lower_case_combined_name.count("u")
e=lower_case_combined_name.count("e")
first_digit=t+r+u+e

l=lower_case_combined_name.count("t")
o=lower_case_combined_name.count("r")
v=lower_case_combined_name.count("u")
e=lower_case_combined_name.count("e")
second_digit=l+o+v+e

score=str(first_digit)+str(second_digit)

total_score=int(score)

if (total_score>90) and (total_score<100):
    print(f"Your love score is {total_score},Your bond is outstanding")
elif (total_score>80) and (total_score<90):
    print(f"Your love score is {total_score},Your bond is excellent")
elif (total_score>70) and (total_score<80):
    print(f"Your love score is {total_score},Your bond is very good")
elif (total_score>60) and (total_score<70):
    print(f"Your love score is {total_score},Your bond is good")
elif (total_score>50) and (total_score<60):
    print(f"Your love score is {total_score},Your bond is above average")
elif (total_score>40) and (total_score<50):
    print(f"Your love score is {total_score},Your bond is average")
elif (total_score>30) and (total_score<40):
    print(f"Your love score is {total_score},Your bond weak")
else:
    print(f"Your love score is {total_score},Not a matching couple")