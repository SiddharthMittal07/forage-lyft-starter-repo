from .tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def  needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3.0