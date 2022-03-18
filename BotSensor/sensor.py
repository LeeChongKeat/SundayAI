from time import sleep

class Sensor:
    def __init__(self, sense):
        self.sense = sense
    
    def get_accelerometer(self):
        self.acceleration = self.sense.get_accelerometer_raw()
        x = self.acceleration['x']
        y = self.acceleration['y']
        z = self.acceleration['z']
        
        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)
        
        return x, y, z
    
    def get_temperature(self):
        return self.sense.get_temperature()
    
    def get_humidity(self):
        return self.sense.get_humidity()
    
    def get_pressure(self):
        return self.sense.get_pressure()
    
    def get_user_event(self):
        _user_action = ""
        temperature = self.get_temperature()
        humidity = self.get_humidity()
        pressure = self.get_pressure()
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    _user_action = "Coding"
                    self.sense.show_message(_user_action)     # Up arrow
                elif event.direction == "down":
                    self.sense.show_letter("D")      # Down arrow
                elif event.direction == "left":
                    _user_action = "Study"
                    self.sense.show_message(_user_action)      # Left arrow
                elif event.direction == "right":
                    _user_action = "Challenge"
                    self.sense.show_message(_user_action)     # Right arrow
                elif event.direction == "middle":
                    _user_action = "Rest"
                    self.sense.show_message(_user_action)      # Enter key
            sleep(0.5)
            self.sense.clear()
            
        return _user_action, temperature, humidity, pressure
        
        