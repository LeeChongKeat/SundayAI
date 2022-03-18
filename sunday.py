from Database import db

from Interface import interface
from time import sleep
from sense_hat import SenseHat
from BotSensor import sensor  


_db = db.Database()
sense = SenseHat()
_interface = interface.Interface(sense)
bot_sensor = sensor.Sensor(sense)

current_stage = 1
is_forward = True


while True:
    _in, current_stage, is_forward = _interface._egg_anim(current_stage, is_forward)
    _action, temperature, humidity, pressure = bot_sensor.get_user_event()
    
    if _action != "":
        _db.insert_new_event(_action, pressure, humidity, temperature)
    sleep(0.3)