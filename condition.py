""""
This script  will implement 
our knowledge about conditions.
"""
import time
print("This IT Organization has various skill sets.")
print("Find out if youre a match")
print("! Enter Capiterized Values: ")

print("________________________________________________")
time.sleep(2)

DevOps = ["Jenkins","AWS","Ansible","Bash","python","puppet","Dockers","Kubenetes","Kafka",]
Development = ("NodeJS","Python","Java","C#",".Net","Ruby","PHP","GoLang")
cntr_emp1 = {
    "Name":"Santa",
    "Skill":"Blockchain",
    "Code":"1024",

}
cntr_emp2 = {
    "Name":"Gooni",
    "Skill":"AI",
    "Code":"1218",

}
#how it works
print ("Enter Your Desired skill: AWS,....etc")
time.sleep(2)
usr_skill = input("Enter Your Desired skill:")
#check in the db if we hav this skill
if usr_skill in DevOps:
    print ("We have " + usr_skill + " in DevOps Team")
elif usr_skill in Development:
    print ("We have " + usr_skill + " in Development Team")



elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print ("We have " + usr_skill + " in Contractual Employees")