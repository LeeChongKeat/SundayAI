import sys
sys.path.append('/home/pi/Documents/Python/SundayBot/')
from BotSensor import sensor 

class Interface:
    def __init__(self, sense):
        self.sense = sense
        self.background_color = (20,20,20)
        self.inw_color = (192,192,192)
        self.bot_sensor = sensor.Sensor(sense)

        
    def _egg_in_one(self, w, b):
        return [
            b, b, b, w, w, b, b, b,
            b, b, w, b, b, w, b, b,
            b, b, w, b, b, w, b, b,
            b, w, b, b, b, b, w, b,
            b, b, w, b, b, w, b, b,
            b, b, w, b, b, w, b, b,
            b, b, b, w, w, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    
    def _egg_in_two(self, w, b):
        return [
            b, b, b, b, b, b, b, b,
            b, b, b, w, w, b, b, b,
            b, b, w, b, b, w, b, b,
            b, w, b, b, b, b, w, b,
            b, w, b, b, b, b, w, b,
            b, b, w, b, b, w, b, b,
            b, b, b, w, w, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    
    def _egg_in_three(self, w, b):
        return [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, w, w, b, b, b,
            b, w, w, b, b, w, w, b,
            w, b, b, b, b, b, b, w,
            b, w, w, b, b, w, w, b,
            b, b, b, w, w, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    
    def _egg_anim(self, current_stage=1, is_forward=True):
        is_forward = self.get_anim_forward(current_stage, is_forward)
        current_stage = self.next_stage(current_stage, is_forward)
        _in = self.get_anim_move(current_stage)
        
        self.sense.set_pixels(_in)
        self.get_correct_rotation()
        self.change_color_will_temp()
        return _in, current_stage, is_forward
    
    def get_anim_forward(self,current_stage, is_forward):
        if current_stage == 1:
            is_forward = True
        elif current_stage == 3:
            is_forward = False
        return is_forward
    
    def next_stage(self, current_stage, is_forward):
        if is_forward:
            current_stage = current_stage + 1
        else:
            current_stage = current_stage - 1
        return current_stage
    
    def get_anim_move(self,current_stage):
        _in = self._egg_in_one(self.inw_color,self.background_color)
        if current_stage == 2:
            _in = self._egg_in_two(self.inw_color,self.background_color)
        elif current_stage == 3:
            _in = self._egg_in_three(self.inw_color,self.background_color)
        return _in
     
    def get_correct_rotation(self):
        x,y,z = self.bot_sensor.get_accelerometer()
        if x  == -1:
            self.sense.set_rotation(90)
        elif y == 1:
            self.sense.set_rotation(0)
        elif y == -1:
            self.sense.set_rotation(180)
        else:
            self.sense.set_rotation(270)
            
    def change_color_will_temp(self):
        temp = self.bot_sensor.get_temperature()
        if temp < 35:
            self.inw_color = (255,255,255)
        elif temp >=35 and temp < 40:
            self.inw_color = (26,67,155)
        else:
            self.inw_color = (229,0,13)
        
    
    