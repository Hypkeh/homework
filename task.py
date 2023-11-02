import os

#1
os.mkdir("C:\Users\MendygulovN\Desktop\dsdasd\watch_me")



#2
os.rename("C:\Users\MendygulovN\Desktop\dsdasd\Nina_Stoletova.jpg", "C:\Users\MendygulovN\Desktop\dsdasd\Stoletova_Nina.jpg")
os.rename("C:\Users\MendygulovN\Desktop\dsdasd\Misha_Perelman.jpg", "C:\Users\MendygulovN\Desktop\dsdasd\Perelman_Misha.jpg")

#3
list = os.listdir("C:\Users\MendygulovN\Desktop\dsdasd\list")
print(list)

with open('list.txt', 'w') as file:
    file.write(list)
    


