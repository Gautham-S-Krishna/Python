class vehicle:
    def __init__(self,vehicle_id: str,base_rate: float):
        self.vehicle_id = vehicle_id
        self.base_rate = base_rate
    def display_details(self):
        print(f"""Vehicle ID: {self.vehicle_id}
              Base Rate: {self.base_rate}""")
    def rental_charge(self):
        return 0.0
    
class car(vehicle):
    def __init__ (self,vehicle_id: str,base_rate: float,num_seats:int):
        vehicle.__init__(self,vehicle_id,base_rate)
        self.num_seats = num_seats
    def rental_charge(self):
        return self.base_rate * self.num_seats
    
class bike(vehicle):
    def __init__(self,vehicle_id: str,base_rate: float,bike_type: str):
        vehicle.__init__(self,vehicle_id,base_rate)
        self.bike_type = bike_type
    def rental_charge(self):
        return self.base_rate *0.5
def calculate_rental(vehicle: vehicle) -> float:
    return vehicle.rental_charge()
def display_vehicle_info(vehicle: vehicle):
    vehicle.display_details()
    print(f"Rental Charge: {calculate_rental(vehicle)}")
car1 = car("CAR123", 100.0, 4)
bike1 = bike("BIKE456", 50.0, "Mountain")
display_vehicle_info(car1)
display_vehicle_info(bike1)



        
    
        
    
    
        
              