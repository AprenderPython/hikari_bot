class functions:
    def help():
        """ About hikari """
        help = (
            "Hi, mi nombre es hikari y aqui podras aprender a usarme :)\n\n"
            "Los comandos disponibles son:\n\n"
            "/start - Usame para saludarme y ver si estoy viva.\n"
            "/help - Si tienes alguna duda podes volver aqui :)"
            "\n\nCualquier duda o bug puedes reportarlo a @dark_zly o a la comunidad @aprenderpython"
            "\n Code: https://github.com/AprenderPython/hikari_bot")
        return help
    def config():
        """Configuracion del bot"""
        token = input("Escribe el token: ")
        return token