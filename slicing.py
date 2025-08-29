planet1 = "Closest to the sum"
print (planet1)
print (planet1[0]) #first letter 
print (planet1[1]) #second leter
#Negative indexing
print (planet1[-1]) #last letter
print (planet1[-4]) 
print (planet1[-5])

# Slicing a string
var = "Hello"
print (var[0:4]) 
print("💀")
print (var[:])
print (var[:3])
devops = ("Linux","vagrant","Aws", "python", "docker","Kubernetes")
# print (devops[0])
# print (devops[-1])
print (devops[2:4][0])

print ("############################")
print ("Dictionary slicing")
skills = {
    "devops":("Linux","vagrant","Aws", "python", "docker","Kubernetes")
    ,"developemet": ("HTML","CSS","JS","REACT","NODEJS")
}

print (skills ["devops"][0:4][2])
print (skills ["developemet"][2:4][0])
print (skills ["developemet"])