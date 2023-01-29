#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:42:38 2023

@author: Arien
"""
import pandas as pd
import numpy as np

# Time of day parameters
daytime = (7, 16)
evening = (17, 19)
windDown = (20, 21)
sleepHours = (22, 23)
overnight = (0, 6)

# Define brightness
class brightness():
    def __init__(self, period, brightness):
        self.brightness = brightness
        
brightness.overnight = 0
brightness.daytime = 0
brightness.evening = 254
brightness.windDown = 100
brightness.sleepHours = 0

# Set up array of zeros to ensure light defaults to off where there are gaps
dayNames = [0, 1, 2, 3, 4, 5, 6]
zero_array = np.zeros(dtype=np.uint8, shape=(24, len(dayNames)))
brightnessLookup = pd.DataFrame(zero_array, columns=dayNames)

# Create basic weekly routine manually inputting brightnesses for each time range
for dayNames in dayNames:
    brightnessLookup[dayNames][min(overnight):max(overnight)+1] = brightness.overnight
    brightnessLookup[dayNames][min(daytime):max(daytime)+1] = brightness.daytime
    brightnessLookup[dayNames][min(evening):max(evening)+1] = brightness.evening
    brightnessLookup[dayNames][min(windDown):max(windDown)+1] = brightness.windDown
    brightnessLookup[dayNames][min(sleepHours):max(sleepHours)+1] = brightness.sleepHours
    
def getBrightness(triggerTime):
    brightnessSetpoint = brightnessLookup[triggerTime.weekday()].iloc[triggerTime.hour]    
    return brightnessSetpoint