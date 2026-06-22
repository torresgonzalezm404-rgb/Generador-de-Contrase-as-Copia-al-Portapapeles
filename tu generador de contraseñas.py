import random
import string
import subprocess
import sys

LONGITUD = 16

# Caracteres para la contraseña
caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"

def generar_password():
    password = ''.join(random.choice(caracteres) for _ in range(LONGITUD))
    return password

def copiar_al_portapapeles(texto):
    try:
        if sys.platform == "darwin":  # macOS
            subprocess.run(["pbcopy"], input=texto.encode('utf-8'), check=True)
        elif sys.platform == "win32":  # Windows
            subprocess.run(["clip"], input=texto.encode('utf-8'), check=True)
        elif sys.platform.startswith("linux"):  # Linux
            subprocess.run(["xclip", "-selection", "clipboard"], input=texto.encode('utf-8'), check=True)
        else:
            print("⚠️ No sé copiar al portapapeles en este sistema.")
            return False
        return True
    except:
        return False

if __name__ == "__main__":
    nueva_pass = generar_password()
    print(f"🔐 Tu nueva contraseña es: {nueva_pass}")
    
    if copiar_al_portapapeles(nueva_pass):
        print("📋 ¡Copiada al portapapeles! Solo pega (Ctrl+V)")
    else:
        print("❌ No se pudo copiar, cópiala manualmente.")