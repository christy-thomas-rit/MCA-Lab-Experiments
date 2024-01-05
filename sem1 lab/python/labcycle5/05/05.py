from graphics import rectangle
from graphics.circle import ar
from graphics.circle import pm
from graphics.threeDgraphics import cuboid
import graphics.threeDgraphics.sphere
print("-----------MENU------------")
print("1.Rectangle\n2.Circle\n3.Cuboid\n4.Sphere")
opt=int(input("Choose an option: "))
if(opt==1):
   l=int(input("Enter the length of rectangle: ")) 
   b=int(input("Enter the breadth of rectangle: "))
   print("\nPerimeter of Rectangle:",rectangle.pm(l,b))
   print("Area of Rectangle:",rectangle.ar(l,b))
elif(opt==2): 
    r=int(input("Enter the radius of circle: "))
    print("\nPerimeter of Circle:",pm(r))
    print("Area of Circle:",ar(r))
elif(opt==3):
    l=int(input("Enter the length of cuboid: "))
    b=int(input("Enter the breadth of cuboid: "))
    h=int(input("Enter the height of cuboid: "))
    print("\nPerimeter of Cuboid:",cuboid.pm(l,b,h))
    print("Total Surface Area of Cuboid:",cuboid.tsa(l,b,h))
    print("Lateral Surface Area of Cuboid:",cuboid.lsa(l,b,h))
    print("Volume of Cuboid:",cuboid.vol(l,b,h))
elif(opt==4):
    r=int(input("Enter the radius of sphere: "))
    print("\nCircumference(Perimeter) of Sphere: ",graphics.threeDgraphics.sphere.pm(r))
    print("Surface Area of Sphere: ",graphics.threeDgraphics.sphere.sa(r))
    print("Volume of Sphere: ",graphics.threeDgraphics.sphere.vol(r))
else:
    print("Please choose a valid option!!!")
