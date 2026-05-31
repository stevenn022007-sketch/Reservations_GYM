#-----------STEFYY- CREAR MIEMBRO----------------
from rich.console import Console
# Qué necesita un miembro? -> id, nombre, tipo de suscripción

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