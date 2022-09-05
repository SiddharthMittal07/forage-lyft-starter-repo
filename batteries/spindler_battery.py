from datetime import date

from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_service_date: date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year = self.last_service_date.year + 2)
        return service_threshold_date < self.current_service_date