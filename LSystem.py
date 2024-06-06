import turtle
import asyncio

# Definimos la clase para el sistema L
class LSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules
        self.result = axiom

    def generate(self, iterations):
        for _ in range(iterations):
            next_result = ""
            for char in self.result:
                next_result += self.rules.get(char, char)
            self.result = next_result

# Función asíncrona para dibujar usando Turtle
async def draw_lsystem(turtle, instructions, distance, angle):
    stack = []
    for cmd in instructions:
        if cmd == 'F':
            turtle.forward(distance)
        elif cmd == '+':
            turtle.right(angle)
        elif cmd == '-':
            turtle.left(angle)
        elif cmd == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()
        await asyncio.sleep(0.01)  # Añade un pequeño retraso para ver el dibujo en tiempo real

# Función principal asíncrona
async def main():
    # Configuración inicial del sistema L
    axiom = "F+F+F+F"
    rules = {
        "F": "FF+F-F+F+FF"
    }
    iterations = 4
    distance = 5
    angle = 90

    # Generamos la secuencia del sistema L
    lsystem = LSystem(axiom, rules)
    lsystem.generate(iterations)

    # Configuración inicial de Turtle
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    # Dibujamos el sistema L usando corutinas
    await draw_lsystem(t, lsystem.result, distance, angle)

    # Espera a que la ventana se cierre
    window.mainloop()

# Ejecuta la función principal
asyncio.run(main())