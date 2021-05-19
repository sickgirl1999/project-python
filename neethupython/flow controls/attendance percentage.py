held=int(input("enter number of classes held"))
attended=int(input("enter number of classes attended"))
per=(attended/held)*100
print(per)
if per>=75:
    print("eligible to write exam")
else:
    print("not eligible to write exam")