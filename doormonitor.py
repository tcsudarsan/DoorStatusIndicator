import RPi.GPIO as GPIO
import time  # Import the time module

# Define GPIO pins
GPIO_TRIGGER = 23  # Change as needed
GPIO_ECHO = 24  # Change as needed

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure_distance():
    # Trigger the sensor by setting it HIGH for 10 microseconds
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)  # Wait for 10 microseconds
    GPIO.output(GPIO_TRIGGER, False)

    # Record the start and stop times
    start_time = time.time()  # Initialize start_time
    stop_time = time.time()  # Initialize stop_time

    # Save start time when the ECHO pin goes HIGH
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Save stop time when the ECHO pin goes LOW
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calculate the time difference
    time_elapsed = stop_time - start_time
    # Calculate distance based on the speed of sound (34300 cm/s)
    distance = (time_elapsed * 34300) / 2

    return distance

try:
    while True:
        dist = measure_distance()
        if dist > 100:
            print("Door is closed")
        elif dist < 100:
            print("Door is open")
        time.sleep(300)  # Wait for 300 seconds before taking another measurement

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()  # Clean up GPIO settings
