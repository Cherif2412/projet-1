import turtle

# Initialisation de la fenêtre turtle
wn = turtle.Screen()
wn.title("hello in a Square")

# Création d'une tortue
pen = turtle.Turtle()

# Positionner la tortue pour écrire "bonjour"
pen.penup()
pen.goto(-30, 0)
pen.pendown()


# Changer la couleur du texte
pen.color("blue")

# Écrire "hello"
pen.write("bonjour", align="center", font=("Arial", 24, "normal"))

# Positionner la tortue pour dessiner le carré
pen.penup()
pen.goto(-90, 65)
pen.pendown()

# Remettre la couleur par défaut (noir) pour le carré
pen.color("green")

# Dessiner le carré autour de "hello"
for _ in range(4):
    pen.forward(120)
    pen.right(90)

# Cacher la tortue
pen.hideturtle()

# Garder la fenêtre ouverte
turtle.done()
