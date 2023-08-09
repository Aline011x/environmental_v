import time
import RPi.GPIO as GPIO

# aditional harware requeriment o analogic convertion module to digital (ADC) (compatibility rasperry pi) 

# Pin Configuration

ANALOG_PIN = 0

def read_ph_value():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ANALOG_PIN, GPIO.IN)

    analog_value = GPIO.input(ANALOG_PIN)
    GPIO.cleanup()

    # Perform analogic value convertion to pH (calibration referent)
    ph_value = 7 - (float(analog_value) - 225) * (7 - 4) / (1023 - 225)
    return ph_value

if __name__ == "__main__":
    try:
        while True:
            ph_value = read_ph_value()
            print(f"Valor de pH: {ph_value:.2f}")
            time.sleep(2)  
            
    except KeyboardInterrupt:
        print("Lectura detenida por el usuario")