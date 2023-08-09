import RPi.GPIO as GPIO
import time

# Pins Configuration
MQ7_PIN = 17  # Change this to pin correctly

# GPIO Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ7_PIN, GPIO.IN)

def read_co_concentration():
    # Reading MQ-7 sensor value 
    co_value = GPIO.input(MQ7_PIN)
    return co_value

if __name__ == "__main__":
    try:
        while True:
            co_concentration = read_co_concentration()
            
            if co_concentration == GPIO.HIGH:
                print("Concentración de CO detectada")
            else:
                print("Concentración de CO normal")
            
            time.sleep(2)  # Before next reading, wait around two seconds 
            
    except KeyboardInterrupt:
        print("Lectura detenida por el usuario")
    finally:
        GPIO.cleanup()
