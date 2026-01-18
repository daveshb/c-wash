#!/usr/bin/env python3
"""
Program for Raspberry Pi
Controls a servo motor with a button
"""

import RPi.GPIO as GPIO
import time
from threading import Thread

# Pin configuration
BUTTON_PIN = 17        # GPIO pin for the button
SERVO_PIN = 18         # GPIO pin for the servo motor (must support PWM)
MOVEMENT_DURATION = 30  # Duration in seconds

# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM object for the servo motor
servo_pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz for servo motor
servo_pwm.start(0)  # Start with 0% duty cycle

def move_servo(duration):
    """
    Moves the servo motor for the specified time
    
    Args:
        duration: Time in seconds the servo should be in motion
    """
    print(f"Moving servo motor for {duration} seconds...")
    
    # Initial position (0 degrees - approximately 2.5% duty cycle)
    servo_pwm.ChangeDutyCycle(2.5)
    time.sleep(1)
    
    # Final position (90 degrees - approximately 7.5% duty cycle)
    servo_pwm.ChangeDutyCycle(7.5)
    
    # Keep the position for the specified time
    time.sleep(duration - 1)
    
    # Return to initial position
    servo_pwm.ChangeDutyCycle(2.5)
    print("Servo motor stopped")
    time.sleep(1)
    servo_pwm.ChangeDutyCycle(0)

def button_callback(channel):
    """
    Callback function when the button is pressed
    Runs in a separate thread to avoid blocking the program
    """
    print("Button pressed")
    # Execute the movement in a separate thread
    thread = Thread(target=move_servo, args=(MOVEMENT_DURATION,))
    thread.start()

# Detect events on the button
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

print("Waiting for you to press the button...")
print("Press Ctrl+C to exit")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram interrupted")
finally:
    servo_pwm.stop()
    GPIO.cleanup()
    print("GPIO cleaned up")
