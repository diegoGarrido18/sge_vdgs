nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

nombre_usuario = input("Introduce tu nombre: ").capitalize()

if nombre_usuario in nombres:
    posicion = nombres.index(nombre_usuario)
    print(f"Los nombres que están antes de '{nombre_usuario}' son:")
    print(nombres[:posicion])
else:
    print(f"El nombre '{nombre_usuario}' no se encuentra en la lista.")
