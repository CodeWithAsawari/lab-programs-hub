print("------------FITNESS CLUB--------------")
User_Age=int(input("Enter your Age:"))
if User_Age<0 or User_Age>100:
    print("Age invalid")
elif User_Age<=18:
    print("Category:Minor\n","Not alloted Membership")
elif User_Age<=25:
    print("Category:student\n","You have got Student discount 20%")
elif User_Age<=40:
    print("Category:Adult\n","eligible for membership")
elif User_Age<=60:
    print("Category:Middle\n","You have got membership of gym\n","Recommendation:Health Checkup")
else:
    print("Category:Senior\n","You are eligible for the health awareness program")