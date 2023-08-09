import time
import RPi.GPIO as GPIO
 
# Pin Configuration
sensor_pin = 17 

# Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

def read_soil_moisture():

    moisture = GPIO.input(sensor_pin)
    return moisture

if __name__ == "__main__":
    try:
        while True:
            moisture_value = read_soil_moisture()
            if moisture_value == GPIO.LOW:
                print("Suelo está húmedo")
            else:
                print("Suelo está seco")

            time.sleep(2) # wait around two secons, before next reading  
                        

    except KeyboardInterrupt:
        print("Lectura detenida por el usuario")  #reading stopped by the user
    finally:
        GPIO.cleanup()
