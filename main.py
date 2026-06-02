from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import eliminar  # Tu módulo para eliminar
import crear  # Tu módulo para crear
import leer_informacion # Tu módulo para leer información
import actualizar # modulo para actualizar informacion

gimnasio = {
    "miembro_1": {"nombre": "Steven", "tipo_suscripcion": "mensual"},
    "miembro_2": {"nombre": "Andres", "tipo_suscripcion": "mensual"}
}
#diccionario para clases
clases = {
    "clase_1": {"nombre_clase": "Yoga", "instructor": "Eliana", "horario": "Lunes 7:00 AM a 9:00 AM", "cupo_maximo": 20},
    "clase_2": {"nombre_clase": "Zumba", "instructor": "Gabriel", "horario": "Martes 6:00 PM a 8:00 PM", "cupo_maximo": 25},
    "clase_3": {"nombre_clase": "Crossfit", "instructor": "Lina", "horario": "Miércoles 5:00 PM a 7:00 PM", "cupo_maximo": 15},
    "clase_4": {"nombre_clase": "Calistenia", "instructor": "Leonardo", "horario": "Jueves 8:00 AM a 10:00 AM", "cupo_maximo": 18},
}

# 1. Inicializamos la consola de Rich
console = Console()
# 2. Creamos un título estilizado dentro de un Panel centrado
bienvenida = Panel(
    Align.center("[bold italic reverse cyan] 🏋️‍♂️ BIENVENIDO AL MEJOR GYM 🏋️‍♂️ [/bold italic reverse cyan]"),
    border_style="bold steel_blue1",
    expand= False
)
console.print(bienvenida)

while True:
    # 3. Diseñamos el menú visual con texto enriquecido
    menu_texto = (
        "[bold cyan]     ── MIEMBROS ──[/bold cyan]\n"
        "[bold green]1.[/bold green] 👀 Ver Miembros\n"
        "[bold green]2.[/bold green] ➕ Crear Miembro\n"
        "[bold green]3.[/bold green] ❌ Eliminar Miembro\n"
        "[bold green]4.[/bold green] 📝 Editar Miembro\n"
        "[bold cyan]     ── CLASES ──[/bold cyan]\n"
        "[bold green]5.[/bold green] 👀 Ver Clases\n"
        "[bold green]6.[/bold green] ➕ Crear Clase\n"
        "[bold green]7.[/bold green] ❌ Eliminar Clase\n"
        "[bold red]8.[/bold red] 🚪 Salir del Sistema"
    )
    
    # Metemos el menú dentro de un cuadro (Panel)
    menu_panel = Panel(
        menu_texto, 
        title="[bold yellow]Opciones Disponibles[/bold yellow]", 
        border_style="bright_magenta",
        expand = False
    )
    console.print(menu_panel)
    
    # 4. Entrada de datos estilizada con Console
    # Usamos try-except por si el usuario presiona letras en lugar de números
    try:
        opcion_usuario = int(console.input("\n[bold orange1]👉 Ingrese la opción (1 a 8): [/bold orange1]"))
    except ValueError:
        console.print("\n[bold red]⚠ Error: Por favor, introduce solo números.[/bold red]")
        continue

    match opcion_usuario:
        case 1:
            leer_informacion.listar_miembros(gimnasio)
        case 2:
            crear.crear_miembro(gimnasio)
        case 3:
            eliminar.eliminar_miembro(gimnasio)
        case 4:
            actualizar.actulizar_miembro(gimnasio)
        case 5:
            pass
        case 6:
            crear.crear_clase(clases)
        case 7:
            eliminar.eliminar_clase(clases)
        case 8:
            console.print("\n[bold italic white on red] 👋 ¡Gracias por usar el sistema! Saliendo... [/bold italic white on red]\n")
            break
        case _:
            console.print("\n[bold red]❌ Opción inválida. Intenta de nuevo.[/bold red]")
    
        