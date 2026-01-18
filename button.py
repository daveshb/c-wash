import RPi.GPIO as GPIO
import time

# Configuración básica
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Esperando pulso en pin 17...")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Botón presionado
            print("¡Botón presionado!")
            time.sleep(0.3)  # Debounce simple
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma interrumpido")

GPIO.cleanup()
