# Alireza Ghasemi, ENSF 692 P24
#The program defines a `Sensor` class to monitor and update the status of traffic lights, pedestrians, and vehicles, providing corresponding actions and statuses based on user input. 
#It uses variables such as `traffic_light`, `pedestrian`, and `vehicle` to store and manage the states of these entities. 
#I used ChatGPT to help me understand and write my code and debug it.
# No global variables are permitted


#defining the class Sensor.
class Sensor:

    # Constructor including the initial values added.
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrain = False
        self.vehicle = False

    # using the below function to update traffic light status.
    def update_traffic_light(self, color):
        if color in ['green', 'yellow', 'red']:
            self.traffic_light = color
        else:
            raise ValueError("Invalid traffic light color")

    # using the below function to update pedestrain status.
    def update_pedestrian(self, status):
        if status in ['yes', 'no']:
            self.pedestrain = status =="yes" #the reason for adding this =="yes" part at the end is that to make the function boolean in action meaning that if the result of the input for pedestrain is yes meaning tru do the action required.
        else:
            raise ValueError("Invalid pedestrian status")

        # using the below function to update vehicle status.
    def update_vehicle(self, status):
        if status in ['yes', 'no']:
            self.vehicle = status == "yes"#the reason for adding this =="yes" part at the end is that to make the function boolean in action meaning that if the result of the input for vehicle is yes meaning tru do the action required.
        else:
            raise ValueError("Invalid vehicle status")

    def print_status(self):#this function of print is to print out the result and status of the parameters we defined above based on the input we get from the user.
        print("\nCourse of action:")
        if self.traffic_light == "red" or self.pedestrain or self.vehicle:
            print("STOP")
        elif self.traffic_light == "green":
            print("Proceed")
        elif self.traffic_light == "yellow":
            print("Caution")
        
        print("\nCurrent status:")
        print(f"The color of the Traffic light: {self.traffic_light.capitalize()}")
        print(f"Pedestrian: {'Yes' if self.pedestrain else 'No'}")
        print(f"Vehicle: {'Yes' if self.vehicle else 'No'}")

#main function to execute the program.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:
        try:
            #getting the input from the user regarding their choice.
            choice = int(input("\nPlease select an number associated with the option you wish to choose:\n1. Update traffic light color\n2. Update pedestrian status\n3. Update vehicle status\n0. End program\nChoice: "))
            if choice == 0:
                print("Program ended.")
                break
            elif choice == 1:
                color = input("Enter traffic light color (green, yellow, red): ").lower()
                sensor.update_traffic_light(color)
            elif choice == 2:
                status = input("Is there a pedestrian? (yes, no): ").lower()
                sensor.update_pedestrian(status)
            elif choice == 3:
                status = input("Is there a vehicle? (yes, no): ").lower()
                sensor.update_vehicle(status)
            else:
                raise ValueError("Invalid menu option. Please enter a valid number associated with your choice.")
        except ValueError as e:
            print(e)
        sensor.print_status()

if __name__ == "__main__":
    main()


