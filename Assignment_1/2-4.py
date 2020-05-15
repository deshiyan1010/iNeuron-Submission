string = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a\
 SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all\
 its citizens"
string = string.split(" ")
#print(string)
string.insert(5,"\n\t")
string.insert(15,"!\n\t\t")
string.insert(20,"\n\t\t\t")

print(" ".join(string))

#Did it manually because the instruction was not given properly / 
#and didnt get any responce to my mail.
