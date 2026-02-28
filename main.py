class Vehicle:
    company_name = "National Transport Services"
    
    def __init__(self, vehicle_id , plate_number, capacity):
            self.vehicle_id = vehicle_id
            self.plate_number = plate_number
            self.capacity = capacity
            self._status = "available"
    def start(self):
        self._status = "On Trip"
        return f"Vehicle {self.plate_number} started trip."
    def stop(self):
        self._status = "available"
        return f"Vehicle {self.plate_number}  trip completed."  
    def get_status(self):        
        return self._status 

    
class Bus(Vehicle):
    def __init__(self, vehicle_id, plate_number, capacity, route_number):
        super().__init__(vehicle_id, plate_number, capacity)
        self.route_number = route_number
    
    def calculate_fare(self, distance):
        fare_per_km = 2.5
        total_fare = fare_per_km * distance
        return  f"Total fare: ${total_fare}"
 
    
class Driver:
    def __init__(self, driver_id, name, license_number):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.assigned_vehicle = None    
    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle
        return f"Driver {self.name} assigned to vehicle {vehicle.plate_number}."
   
        
class Route:
    def __init__(self, route_number, start_point, end_point,distance):
        self.route_number = route_number
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance
    def route_info(self):
        print(f"Route {self.route_number}: {self.start_point} to {self.end_point}, Distance: {self.distance} km")

class Maintenance:
    @staticmethod
    def perform_service(vehicle):
        vehicle._status = "under maintenance"
        return f"Vehicle {vehicle.plate_number} is under maintenance."
        
class MiniBus(Bus):
    def calculate_fare(self, distance):
        return distance * 3.0 

route1 = Route("R001", "City A", "City B", 100)          
minibus1 = MiniBus("B001", "ABC-123", 5000, route1.route_number)
bus1 = Bus("B002", "XYZ-789", 4000, route1.route_number)
driver1 = Driver("D001", "John Doe", "L123456")


print(driver1.assign_vehicle(minibus1))
print(minibus1.start()) 
print(minibus1.calculate_fare(10))
print(bus1.calculate_fare(10))
print(minibus1.stop()) 
print(Maintenance.perform_service(minibus1)) 
