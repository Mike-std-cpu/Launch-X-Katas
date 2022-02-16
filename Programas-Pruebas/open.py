#Conjunto de kata X de  traceback

def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()

    """
    Se trata de una sola función main() que abre el archivo inexistente, como antes. Al final, esta función usa
    un asistente de Python que indica al intérprete que ejecute la función main() cuando se le llama en el terminal.
    Ejecútala con Python y podrás comprobar el siguiente mensaje de error:
    """