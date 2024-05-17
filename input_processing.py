# input_processing.py
# Alireza Ghasemi, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted



class Sensor:

    # Constructor including the initial values added.
    def __init__(self):
        Traffic_light = "green"
        Pedestrain = False
        Vehicle = False

    # using the below function to update traffic light status.
    def Traffic_light(): 
        while True:
            try:
                light_color = input("Enter traffic light color (green/yellow/red) and make sure you are not using capital letters: ").lower()
                if light_color in ["green", "yellow", "red"]:
                    Sensor.light_color = light_color
                    break
                else:
                    raise ValueError("Invalid input. Please enter green, yellow, or red, and make sure the wording is correct and you are not using capital letters.")
            except ValueError as e:
                print(e)

    # using the below function to update traffic light status.
    def Pedestrain(sensor):
        while True:
            try:
                status = input("Is there any pedestrain (only lower case letters)? (yes/no): ").lower()
                if status in ["yes", "no"]:
                    sensor.Pedestrain = status
                    break
                else:
                    raise ValueError("Invalid input. Please enter yes or no.")
            except ValueError as e:
                print(e)

        # using the below function to update traffic light status.
    def Vehicle(sensor):
        while True:
            try:
                status = input("Is there any vehicle (only lower case letters)? (yes/no): ").lower()
                if status in ["yes", "no"]:
                    sensor.Vehicle = status
                    break
                else:
                    raise ValueError("Invalid input. Please enter yes or no.")
            except ValueError as e:
                print(e)

    def print_status(sensor):#this function of print is to print out the result and status of the parameters we defined above based on the input we get from the user.
        print("\nCourse of action:")
        if sensor.Traffic_light == "red" or sensor.pedestrian_detected or sensor.vehicle_detected:
            print("STOP")
        elif sensor.Traffic_light == "green":
            print("Proceed")
        elif sensor.Traffic_light == "yellow":
            print("Caution")
        
        print("\nCurrent status:")
        print(f"The color of the traffic light: {sensor.Traffic_light.capitalize()}")
        print(f"Pedestrian: {'Yes' if sensor.Pedestrain else 'No'}")
        print(f"Vehicle: {'Yes' if sensor.Vehicle else 'No'}")

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
                    update_traffic_light(sensor)
                elif choice == 2:
                    update_pedestrian(sensor)
                elif choice == 3:
                    update_vehicle(sensor)
                else:
                    raise ValueError("Invalid menu option. Please enter a valid number associated with you choice.")
            except ValueError as e:
                print(e)

            print_status(sensor)

    if __name__ == "__main__":
        main()

    
