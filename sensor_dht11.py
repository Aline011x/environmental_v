import Adafruit_DHT
import time

# Configura el tipo de sensor y el pin GPIO al que está conectado
sensor = Adafruit_DHT.DHT11
pin = 4  # Cambia este valor al pin GPIO correcto

while True:
    # Intenta leer los datos del sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Si la lectura fue exitosa, muestra los valores
    if humidity is not None and temperature is not None:
        print("Humedad: {}%".format(humidity))
        print("Temperatura: {}°C".format(temperature))
    else:
        print("Error al leer los datos del sensor")

    # Espera unos segundos antes de la siguiente lectura
    time.sleep(5)
