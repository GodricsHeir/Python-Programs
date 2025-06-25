#Sets an audio alarm for a given time
import time
from pygame import mixer
import os

def set_alarm(alarm_time): #waits for the specified alarm time to be reached.
    alarm_hours, alarm_minutes, alarm_seconds = map(int, alarm_time.split(':'))  # Split the input time
    while True:
        current_time = time.localtime()  # Get the current local time
        current_hours = current_time.tm_hour
        current_minutes = current_time.tm_min
        current_seconds = current_time.tm_sec
        
        #check if alarm time is before current time and if so, sets the alarm for the next day
        if (alarm_hours < current_hours or 
            (alarm_hours == current_hours and alarm_minutes < current_minutes) or 
            (alarm_hours == current_hours and alarm_minutes == current_minutes and alarm_seconds < current_seconds)):
            # If the alarm time is before the current time, set it for the next day
            alarm_hours += 24

        if (current_hours == alarm_hours and 
            current_minutes == alarm_minutes and 
            current_seconds == alarm_seconds):
            break  # Exit loop when alarm time is reached
        time.sleep(1)  # Wait for 1 second before checking again


alarm_time= input("Enter the alarm time in HH:MM:SS: ")  # Get alarm time from user
set_alarm(alarm_time)  # Set the alarm
mixer.init()
mixer.music.load("alarm.mp3")  # Load the alarm sound
mixer.music.set_volume(2.00)  # Set volume
print("Alarm ringing!")
mixer.music.play(5)  # Play the alarm sound
time.sleep(45)  # Keep the alarm ringing for 45 seconds