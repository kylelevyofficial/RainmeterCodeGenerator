# n = input("How many links should be generated?: ")
def generator():
    print("[Link"+str(counter)+"]")
    # Creates a meter named Link8
    print("Meter=String")
    # Tells the meter it will be text
    print("MeterStyle=StyleText")
    # Tells the meter to use our style created above
    print("SolidColor=0,0,0,1")
    # Creates a transparent box over the text for easier button presses
    print("Text="+linkName)
    # What you want your button to say
    print("LeftMouseUpAction=["+linkURL+"]")
    # Makes it so when you release your left mouse button on the text it will open your link
    print("X=200")
    # Horizontal position relative to your last meter. In this case Link1. Makes it always be this distance apart even if the first moves
    print("Y=35r")
    # Verticle position

counter = 1

n = input("How many links would you like to generate?: ")

for x in range(int(n)):
    linkName = input("What text should be displayed for the link?: ")
    linkURL = input("What is the URL for the link?: ")
    print()
    generator()
    print()
    counter = counter+1
    
temp = input("Press enter to end the program...")