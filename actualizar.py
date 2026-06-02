from rich.console import Console

console = Console()


def actulizar_miembro (gimnasio: dict):
    id_miembro = int(console.input("[green] id del miembro a editar: [/green]"))
    
    # nombre_clase = input("Nombre de la clase: ").strip()

    str_id_miembro = f"miembro_{id_miembro}"

    if str_id_miembro in gimnasio:
        info = gimnasio[str_id_miembro]
        print(f"¡Mienbro encontrado!. proporciona los datos a editar del miembro: {str_id_miembro}")
        print("\nPresiona 'ENTER' sin escribir nada para mantener el valo actual\n")

        console.print(f"[green]El Nombre actual es:[/green] {info["nombre"]}")
        nuevo_nombre = console.input("[green]Elije el nuevo nombre, de lo contrario Presiona ENTER:[/green]")

        if nuevo_nombre != "":
            info["nombre"] = nuevo_nombre

        console.print(f"[green]Tipo de suscripción Actual:[/green] {info["tipo_suscripcion"]}")
        console.print("  Las Opciones para actualizar son:")
        console.print("  [bold]1.[/bold] Mensual")
        console.print("  [bold]2.[/bold] Anual")
        nuevo_plan = int(console.input("[green]Elige (1 o 2) para actualizar, de lo contrario presiona ENTER: [/green]"))

        if nuevo_plan != "":
            if nuevo_plan == 1:
                tipo = "Mensual"
            elif nuevo_plan == 2:
                tipo = "Anual"
            else:
                console.print("[red]⚠ Opción inválida.[/red]")
                return
        info["tipo_suscripcion"] = tipo
    else:
        print(f"❌❌❌El mienbro con ese id {str_id_miembro} no exsiste❌❌❌")


def actulizar_clase (clases: dict):
    id_miembro = int(console.input("[green] id del miembro a editar: [/green]"))
    
    # nombre_clase = input("Nombre de la clase: ").strip()

    str_id_miembro = f"clase_{id_miembro}"

    if str_id_miembro in clases:
        info = clases[str_id_miembro]
       
        print(f"Infomacion: {info}" )
    else:
        print(f"❌❌❌La clase con ese id {str_id_miembro} no exsiste❌❌❌")
