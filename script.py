import RPi.GPIO as GPIO
import time

# Configuración básica
GPIO.setmode(GPIO.BCM)
SERVO_PIN = 24
BUTTON_PIN = 17
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Frecuencia típica para servos: 50 Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def mover_grado(angulo):
    # Conversión aproximada: 0°->2.5%, 180°->12.5%
    duty = 2.5 + (angulo / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(4)  # pequeña pausa para que el servo se mueva
                pwm.ChangeDutyCycle(0)  # detener señal para evitar zumbidos

def activar_servo(duration=2):
    """Mueve el servo durante 30 segundos"""
    print(f"Servo activado por {duration} segundos...")
    start_time = time.time()
    while time.time() - start_time < duration:
        mover_grado(0)
        mover_grado(90)
        mover_grado(180)
    print("Servo detenido")

# Detectar evento del botón


try:
    print("Esperando que presiones el botón...")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Botón presionado
            print("Botón presionado!")
            activar_servo()
            time.sleep(0.3)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()