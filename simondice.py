import random  
import time  

def simon_dice():  
    colores = ["rojo", "verde", "azul", "amarillo"]  
    secuencia = []  
    
    print("¡Bienvenido a Simón Dice!")  
    
    while True:  
        nuevo_color = random.choice(colores)  
        secuencia.append(nuevo_color)  
        print("Simón dice: ", secuencia)  
        time.sleep(2)  # Muestra la secuencia por 2 segundos  
        print("\n" * 50)  # Limpia la consola  

        for color in secuencia:  
            respuesta_usuario = input(f"Adivina el color: ")  
            if respuesta_usuario != color:  
                print("¡Incorrecto! Fin del juego.")  
                return  

        print("¡Correcto! Sigamos jugando.")  

# Ejecuta el juego  
simon_dice()