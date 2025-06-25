#Starts a timer for a specified duration and returns the elapsed time.
import time
from pygame import mixer
import os
def start_timer():
    """
    Starts a timer and returns the time elapsed in seconds.
    
    Returns:
        float: The time elapsed in seconds.
    """
    start_time = time.time()
    return start_time

def main():
    # Example usage
    start_time = start_timer()
    timerTime=(input("Enter the timer duration in HH:MM:SS: "))  # Get timer duration from user
    task = input("Enter the task you want to perform: ")  # Get task from user
    print("Starting timer...")
    timerTime = sum(int(x) * 60 ** i for i, x in enumerate(reversed(timerTime.split(':'))))  # Convert HH:MM:SS to seconds
    time.sleep(timerTime)  # Replace with actual process
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.set_volume(2.00)  
    print(f"Timer finished")
    print(task)
    mixer.music.play(3)
    time.sleep(120)

main()