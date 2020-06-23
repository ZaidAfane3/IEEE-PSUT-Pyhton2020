class car: 
    model = ""
    color = "White"
    plate_number = ""
    oil = 0 
    location = {"x" : 0, "y":0}

    def move_5meter_up (self):
        self.oil -= 1 
        self.location["y"] += 5
    def move_5meter_down(self):
        self.oil -= 1
        self.location["y"] -= 5 
    
    def move_10meter_right(self):
        self.oil -= 2 
        self.location["x"] += 10 

    def move_10meter_left(self):
        self.oil -= 2 
        self.location["x"] -= 10 


    
bmw = car() 


print (bmw.location["y"])
bmw.move_5meter_up()
print (bmw.location["y"])

ford = car()
print (ford.location["y"])

