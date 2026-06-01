def eliminar_miembro(lista_miembros):
    eliminar_por_id = input("Ingrese el ID del miembro que deseas eliminar: ").lower()
    
    if eliminar_por_id in lista_miembros:
        lista_miembros.pop(eliminar_por_id)
        print(f"El ID {eliminar_por_id} fue eliminado exitosamente")
        
    else:
        print(f"El ID {eliminar_por_id} no se encuentra en la base de datos")
        

def eliminar_clase(lista_clases):
    eliminar_clase_por_id = input("Ingrese la clase que desea eliminar por ID: ").lower()
    
    if eliminar_clase_por_id in lista_clases:
        lista_clases.pop(eliminar_clase_por_id)
        print(f"El ID {eliminar_clase_por_id} fue eliminado exitosamente")


