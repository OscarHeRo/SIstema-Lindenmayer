import turtle
import tkinter as tk

# Clase para el sistema L
class LSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules
        self.result = axiom

    def generate(self):
        while True:
            next_result = ""
            for char in self.result:
                next_result += self.rules.get(char, char)
            self.result = next_result
            yield self.result

# Función para dibujar usando Turtle
def draw_lsystem(turtle, instructions, distance, angle):
    stack = []
    for cmd in instructions:
        if cmd == 'F':
            turtle.forward(distance)
        elif cmd == '+':
            turtle.left(angle)
        elif cmd == '-':
            turtle.right(angle)
        elif cmd == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

# Función principal
def main(axiom, rules, angle):
    lsystem = LSystem(axiom, rules)

    # Configura Turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    # Posiciona Turtle en el centro
    turtle.setpos(0, 0)
    turtle.setheading(90)  # Orienta Turtle hacia arriba
    turtle.pendown()

    for sequence in lsystem.generate():
        draw_lsystem(turtle, sequence, distance=10, angle=angle)

    turtle.mainloop()  # Mantener la ventana abierta

# Función para obtener la entrada del usuario
def get_user_input():
    root = tk.Tk()
    root.title("Ejemplo Personalizado")

    def submit():
        axiom = axiom_entry.get()
        rule = rule_entry.get()
        angle = int(angle_entry.get())
        main(axiom, {"F": rule}, angle)
        root.destroy()  # Cerrar la ventana principal cuando se dibuje

    tk.Label(root, text="Axioma:").pack()
    axiom_entry = tk.Entry(root)
    axiom_entry.insert(0, "F+F+F+F")  # Placeholder
    axiom_entry.pack()

    tk.Label(root, text="Regla de Producción para F:").pack()
    rule_entry = tk.Entry(root)
    rule_entry.insert(0, "F+F-F-FFF+F+F-F")  # Placeholder
    rule_entry.pack()

    tk.Label(root, text="Ángulo:").pack()
    angle_entry = tk.Entry(root)
    angle_entry.insert(0, "90")  # Placeholder
    angle_entry.pack()

    tk.Button(root, text="Dibujar", command=submit).pack()

    root.mainloop()

# Función para seleccionar ejemplos predeterminados o personalizar
def select_example(selection=None):
    root = tk.Tk()
    root.title("Selecciona un Ejemplo")

    def submit(selection=None):
        if selection is not None:
            if selection == 1:
                main("X", {
                    "F": "FF",
                    "X": "F-[[X]+X]+F[+FX]-X"
                }, angle=22.5)
            elif selection == 2:
                main("F+F+F+F", {
                    "F": "FF+F-F+F+FF"
                }, angle=90)
            elif selection == 3:
                main("F", {
                    "F": "FF+[+F-F-F]-[-F+F+F]"
                }, angle=22.5)
            elif selection == 4:
                main("X", {
                    "F": "FF",
                    "X": "F[+X]F[-X]+X"
                }, angle=20)
            elif selection == 5:
                get_user_input()
        root.destroy()

    tk.Button(root, text="Ejemplo 1", command=lambda: submit(1)).pack()
    tk.Button(root, text="Ejemplo 2", command=lambda: submit(2)).pack()
    tk.Button(root, text="Ejemplo 3", command=lambda: submit(3)).pack()
    tk.Button(root, text="Ejemplo 4", command=lambda: submit(4)).pack()
    tk.Button(root, text="Ejemplo 5", command=lambda: submit(5)).pack()
    tk.Button(root, text="Personalizado", command=get_user_input).pack()

    root.mainloop()

if __name__ == "__main__":
    select_example()
