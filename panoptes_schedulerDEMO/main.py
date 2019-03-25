import yaml
import os
from unit import Unit
from scheduler import Scheduler

"""set the site information"""
unit_config = os.getcwd() + "\config_file\pocs.yaml"

with open(unit_config, 'r') as u:
    unit_content = yaml.load(u.read())

unit_list = list(range(len(unit_content)))
print(len(unit_content))

for i in range(len(unit_content)):
    unit_list[i] = Unit(unit_content[i]['pan_id'], os.getcwd() + unit_content[i]['field_file'])

"""set the scheduler"""
scheduler = Scheduler(unit_list)

"""test the simple target algorithm with input unit ID"""
scheduler.read_best_option(0)
print(scheduler.best_option)
print(scheduler.unit_list[0].last_field)
scheduler.read_best_option(1)
print(scheduler.best_option)
print(scheduler.unit_list[0].last_field)

"""test the incorporate algorithm with input unit ID"""
scheduler.read_specific_option(1, 'KIC 8462852')
print(scheduler.best_option)
print(scheduler.unit_list[1].last_field)
scheduler.read_best_option(0)
print(scheduler.best_option)
print(scheduler.unit_list[0].last_field)
scheduler.read_specific_option(1, 'KIC 8462852')
print(scheduler.best_option)
print(scheduler.unit_list[1].last_field)