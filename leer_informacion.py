from rich.console import Console
from rich.table import Table

console = Console()

def listar_miembros(gimnasio: dict, filtro_nombre: str = ""):
    """Muestra y filtra los miembros del gimnasio leyendo las llaves 'miembro_X'."""
    
    # Quitamos los espacios de los lados y pasamos a minúsculas lo que el usuario quiere buscar
    buscar = filtro_nombre.strip().lower()
    
    # Creamos una lista vacía para ir guardando a los miembros que compaginen con la búsqueda
    miembros_filtrados = []
    
    # .items() nos sirve para revisar el cajón del "gimnasio" dándonos el código y el contenido de cada registro a la vez
    for clave, info in gimnasio.items():
        
        # .startswith("miembro_") revisa si el código de la tarjeta empieza con la palabra "miembro_"
        if clave.startswith("miembro_"):
            
            # .get("nombre", "") busca el nombre de la persona sin que el programa se apague si de casualidad no lo encuentra
            nombre_miembro = info.get("nombre", "")
            
            # Revisamos si las letras que busca el usuario están metidas dentro del nombre del miembro
            if buscar in nombre_miembro.lower():
                
                # .append() agarra los datos de este miembro y los guarda en nuestra lista de seleccionados
                miembros_filtrados.append({
                    "id": clave,
                    "nombre": nombre_miembro,
                    "tipo": info.get("tipo_suscripcion", "")
                })

    # Si la lista quedó vacía y no encontramos a nadie, mostramos un aviso amarillo y paramos la función con un "return"
    if not miembros_filtrados:
        return console.print("\n[yellow]⚠️ No se encontraron miembros registrados con esos criterios.[/yellow]\n")

    # Diseñamos el aspecto de la tabla con títulos y colores usando la herramienta Table de Rich
    tabla = Table(title="👥 MIEMBROS DEL GIMNASIO", header_style="bold cyan", expand=True)
    
    # Este ciclo acomoda los nombres de las 3 columnas principales de la tabla con sus estilos
    for col, style in [("ID Miembro", "bold"), ("Nombre Completo", None), ("Tipo de Suscripción", "green")]:
        
        # .add_column() es la orden que dibuja una columna nueva en la tabla (las divisiones que van de arriba a abajo)
        tabla.add_column(col, style=style, justify="center" if col != "Nombre Completo" else "left")

    # Revisamos uno por uno los miembros que guardamos en nuestra lista filtrada
    for m in miembros_filtrados:
        
        # .add_row() es la orden que acomoda una fila de datos (un renglón de izquierda a derecha) en la tabla
        tabla.add_row(m["id"], m["nombre"], m["tipo"])

    console.print(tabla)