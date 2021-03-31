# Your code goes here:
def render_person(name, born_date, color, age, gender):
    str_age=str(age)
    text= name +" is a "+str_age+ " years old " + gender + " born in " + born_date + " with " + color + " eyes"
    return (text)


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))