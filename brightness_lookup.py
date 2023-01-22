#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:42:38 2023

@author: Arien
"""
import pandas as pd
import numpy as np

# Time of day parameters
# daytime = pd.DataFrame(columns=['start', 'finish'])
# daytime.at[0,'start'] = 7
# daytime.at[0,'finish'] = 16
daytime = (7, 16)

# windDown = pd.DataFrame(columns=['start', 'finish'])
# windDown.at[0,'start'] = 21
# windDown.at[0,'finish'] = 22

evening = (17, 19)

windDown = (20, 21)

# sleepHours = pd.DataFrame(columns=['start', 'finish'])
# sleepHours.at[0,'start'] = 22
# sleepHours.at[0,'finish'] = 7

sleepHours = (22, 23)

overnight = (0, 6)

# Define brightness
class brightness():
    def __init__(self, period, brightness):
        self.brightness = brightness
        
brightness.overnight = 10
brightness.daytime = 0
brightness.evening = 254
brightness.windDown = 100
brightness.sleepHours = 10

# Set up array of zeros to ensure light defaults to off where there are gaps
dayNames = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zero_array = np.zeros(dtype=np.uint8, shape=(24, len(dayNames)))
brightnessLookup = pd.DataFrame(zero_array, columns=dayNames)

# Create basic weekly routine manually inputting brightnesses for each time range
for dayNames in dayNames:
    brightnessLookup[dayNames][min(overnight):max(overnight)+1] = brightness.overnight
    brightnessLookup[dayNames][min(daytime):max(daytime)+1] = brightness.daytime
    brightnessLookup[dayNames][min(evening):max(evening)+1] = brightness.evening
    brightnessLookup[dayNames][min(windDown):max(windDown)+1] = brightness.windDown
    brightnessLookup[dayNames][min(sleepHours):max(sleepHours)+1] = brightness.sleepHours