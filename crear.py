#-----------STEFYY- CREAR MIEMBRO----------------
from rich.console import Console
# Qué necesita un miembro? -> id, nombre, tipo de suscripción
# console = Console()  # Inicializamos la consola de Rich para usarla en este módulo
#rich es una biblioteca de Python que permite crear interfaces de usuario en la terminal con estilos y colores. 
# En este código, se utiliza para imprimir mensajes estilizados y para manejar la entrada del usuario de manera más atractiva.
console = Console()
#escribimos el mismo diccionario que esta en main para trabajar sobre los mismos datos
def crear_miembro(gimnasio):
    console.print("\n[bold cyan]➕ CREAR NUEVO MIEMBRO[/bold cyan]")

    nombre = console.input("[green]Nombre del miembro: [/green]").strip()

    console.print("[green]Tipo de suscripción:[/green]")
    console.print("  [bold]1.[/bold] Mensual")
    console.print("  [bold]2.[/bold] Anual")

    try:
        opcion = int(console.input("[green]Elige (1 o 2): [/green]"))

        if opcion == 1:
            tipo = "Mensual"
        elif opcion == 2:
            tipo = "Anual"
        else:
            console.print("[red]⚠ Opción inválida.[/red]")
            return

        # Generar el ID automático contando cuántos miembros hay.

        nuevo_id = f"miembro_{len(gimnasio) + 1}"

        # Guardar el nuevo miembro en el diccionario
        gimnasio[nuevo_id] = {
            "nombre": nombre,
            "tipo_suscripcion": tipo
        }

        console.print(f"[bold ]✅ Miembro '{nombre}' creado con ID {nuevo_id}[/bold]\n")

    except ValueError:
        console.print("[red]⚠ Error: Ingresa solo números donde se piden.[/red]")

#-------------------------CREAR CLASE-----------------------
# Qué necesita una clase? -> id, nombre, instructor, horario, cupo maximo
def crear_clase(clases):
    console.print("\n[bold magenta]➕ CREAR NUEVA CLASE[/bold magenta]")

    nombre_clase = input("Nombre de la clase: ").strip()
    instructor = input("Instructor: ").strip()
    horario = input("Horario (ej: Lunes 7:00 AM a 9:00 AM): ").strip()

    try:
        cupo_maximo = int(input("Cupo máximo: "))

        if cupo_maximo <= 0:
            console.print("[red]⚠ El cupo debe ser mayor a 0.[/red]")
            return

        # Generar ID automático sumando 1 al número de clases existentes
        nuevo_id = f"clase_{len(clases) + 1}"

        # Guardar la clase en el diccionario
        clases[nuevo_id] = {
            "nombre_clase": nombre_clase,
            "instructor": instructor,
            "horario": horario,
            "cupo_maximo": cupo_maximo
        }

        console.print(f"[bold green]✅ Clase '{nombre_clase}' creada con ID {nuevo_id}[/bold green]\n")

    except ValueError:
        console.print("[red]⚠ Error: El cupo debe ser un número entero.[/red]")