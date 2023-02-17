#light_theme= {
  #  "button""red"
 #   "title""blue"
#}

#dark_theme = {
  #  "button""black"
 #   "title""white"
#}


#cars
car={
    "model" : "ford",
    "year" : "1968",
    "color" : "red",
    "country" : "kenya"
}
#print(car["country"])

person={
    "name" : "Haasan",
    "age" : "19",
    "pets" : {"dog" : "X",
     "cat" : "y"
    }
    }
#print(person["pets"]["cat"])


#profile={}
#profile["username"] = "user123"
#profile["age"] = 20
#profile["email"] = "user123@gmail.com"

def register():
    username=input("enter username:")
    age=eval(input("Enter your age:"))
    email=("enter your email:")
    password=input("enter yor password:")
    #ask for usename
    profile["username"]= username
    profile["email"]= email
    profile["password"]= password
    #ask for age
    #ask for email

register()
get_profile()
change_usernam()
get_profile()