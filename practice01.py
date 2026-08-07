ask_username = input("Apna username bataye\n")
count = 0
with open("users.txt") as u:
    for user in u:
        if ask_username == user.strip():
            
            print(f"Welcomeback {ask_username}")
            break

    else:
            
     print("User not found please sign up")



cart = [
    {"item": "Pizza", "price": 200, "qty": 2},
    {"item": "Coke",  "price": 40,  "qty": 3},
    {"item": "Fries", "price": 90,  "qty": 1},
]

# step1 function chahiye
# for loop chahiye jo pizza se total tak  print kare
# do value ka multiplication aur sab ka addition karke total nikalo




   
total = 0

for c in cart:
    m = c['price']
    l = c['qty']
    n = c['item']
    item_total = m * l
    
    print(f"{n} x{c['qty']} = {item_total}")


    total = total + item_total
    

print(f"--------------\n          {total}")

      

   
   



# step1 top_post(posts) function banao
# step 2 ek loop jo check kare highest likes
# step 3 condition aisi jo highest likes find kare
# step 4 return caption kare last me
# and then print 


posts = [
    {"caption": "Sunset at beach", "likes": 340},
    {"caption": "Morning coffee",  "likes": 120},
    {"caption": "Goa trip",        "likes": 890},
    {"caption": "New phone",       "likes": 455},
]


def top_post(posts):
    caption = ""
    likes = 0
    for p in posts:

       m = p['likes']
       if m > likes:
          likes = m
          caption = p['caption']

    return caption

print(top_post(posts))

      