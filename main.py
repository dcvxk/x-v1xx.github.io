import os
import time 
import requests
import tkinter as tk
from tkinter import filedialog
import platform
import subprocess

os.system("color 9")
os.system("title X-V1XX BETA V1.0.0")
os.system("cls")

memoria = """

╔═══════════════════════════════════════════════════╗
║       OPCIONES DE MEMORIA RAM - X-V1XX            ║
╠═══════════════════════════════════════════════════╣
║  [1] 4GB RAM                                      ║
║  [2] 6GB RAM                                      ║
║  [3] 8GB RAM                                      ║
║  [4] 12GB RAM                                     ║
║  [5] 16GB RAM                                     ║
║  [6] 24GB RAM                                     ║
║  [7] 32GB RAM                                     ║
║  [8] 64GB RAM                                     ║        
║  [9] Restablecer valores predeterminados          ║
╚═══════════════════════════════════════════════════╝

"""

winpriority = """

╔════════════════════════════════════════════════════╗
║            🚀 X-V1XX WINPRIORITY 🚀                ║
╠════════════════════════════════════════════════════╣
║  [1] PRIORITY 26 (MENOS DELAY)                     ║
║  [2] PRIORITY 27 (-DELAY / +FPS)                   ║
║  [3] PRIORITY 28 (+FPS / +DELAY)                   ║
║  [4] PRIORITY fff55555 (GAMING)                    ║
╚════════════════════════════════════════════════════╝ 

L MI RECOMENDACION ES IR PROBANDO CADA UNO.
"""

prg = """

╔════════════════════════════════════════════════════╗
║         🚀 PROGRAMAS TOP PING & FPS 🚀            ║
╠════════════════════════════════════════════════════╣
║  [1] Razer Cortex (Boost FPS & limpiar RAM)        ║
║  [2] WTFast (Reducir ping y latencia)              ║
║  [3] MSI Afterburner (Optimizar GPU para FPS)      ║
║  [4] Latency Optimizer (Mejorar ping en juegos)    ║
║  [5] GeForce Experience (Optimización y drivers)   ║
║  [6] TCP Optimizer (Mejorar conexión internet)     ║
║  [7] Game Fire (Optimiza recursos para juegos)     ║
║  [0] Volver al menú principal                      ║
╚════════════════════════════════════════════════════╝

"""

menu = """

╔══════════════════════════════════════════════════════════════╗
║                      ▓▓▓ MENU DE TWEAKS ▓▓▓                  ║
╠══════════════════════════════════════════════════════════════╣
║ [1] TWEAKS +FPS               ║ [8]  WINPRIORITY +FPS        ║
║ [2] TWEAKS -PING              ║ [9]  DNS_JUMPER - X-V1XX     ║
║ [3] TWEAKS -LATENCIA          ║ [10] INTEL                   ║
║ [4] PROGRAMAS +FPS            ║ [11] AMD                     ║
║ [5] CLEAN PC                  ║ [12] NVIDIA                  ║
║ [6] SUPPORT X-V1XX            ║ [13] OVERCLOCKING            ║
║ [7] PUNTO DE RESTAURACIÓN     ║ [14] TWEAKS MEMORY           ║
║ [0] SALIR                     ║ [15] TWEAKS CPU              ║
╚══════════════════════════════════════════════════════════════╝


"""

banner = """


██╗  ██╗     ██╗   ██╗ ██╗██╗  ██╗██╗  ██╗              ██╗   ██╗ ██╗    ██████╗     ██████╗ 
╚██╗██╔╝     ██║   ██║███║╚██╗██╔╝╚██╗██╔╝              ██║   ██║███║   ██╔═████╗   ██╔═████╗
 ╚███╔╝█████╗██║   ██║╚██║ ╚███╔╝  ╚███╔╝     █████╗    ██║   ██║╚██║   ██║██╔██║   ██║██╔██║
 ██╔██╗╚════╝╚██╗ ██╔╝ ██║ ██╔██╗  ██╔██╗     ╚════╝    ╚██╗ ██╔╝ ██║   ████╔╝██║   ████╔╝██║
██╔╝ ██╗      ╚████╔╝  ██║██╔╝ ██╗██╔╝ ██╗               ╚████╔╝  ██║██╗╚██████╔╝██╗╚██████╔╝
╚═╝  ╚═╝       ╚═══╝   ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                ╚═══╝   ╚═╝╚═╝ ╚═════╝ ╚═╝ ╚═════╝ 
                                                                                             
                                      ⌊ X-V1XX BETA V1.0.0 ⌋               

"""

# INICIO DEL PROGRAMA
print(banner)
time.sleep(1)
print(" WELCOME TO X-V1XX - V1.0.0 BETA")
time.sleep(0.1)
os.system("cls")
print(" INICIANDO...")
print("| ════════...................| 40%")
time.sleep(0.1)
os.system("cls")
print(" INICIANDO...")
print("| ════════════════...........| 68%")
time.sleep(0.1)
os.system("cls")
print(" INICIANDO...")
print("| ════════════════════════...| 85%")
time.sleep(0.1)
os.system("cls")
print(" INICIANDO...")
print("| ═══════════════════════════| 100%")
time.sleep(0.1)
os.system("cls")
    
while True:

    print(banner)
    print(menu)
    opciones = input("└───> ")

    if opciones == "1":

        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/tweaks_fps")
        os.system('regedit /s X-V1XX.reg"')
        os.system('regedit /s "Services By V1XX.reg"')
        os.system('regedit /s "2 Tweaks del registro.reg"')
        os.system('regedit /s "1 Windows Reguistro.reg"')
        print("TWEAKS +FPS APLICADOS ✓")
        os.system("cls")

    if opciones == "2":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/tweaks_ping")
        os.system("regedit /s lantencia.reg")
        os.system("regedit /s ping.reg")
        os.system("regedit /s ping1.reg")
        print("TWEAKS +PING APLICADOS ✓")
        os.system("cls")

    if opciones == "3":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/tweaks_latencia")
        os.system("start latencia.reg")
        print("TWEAKS -LATENCIA APLICADOS ✓")
        os.system("cls")

    if opciones == "4":
        os.system("cls")
        time.sleep(0.5)
        print("BRO EL OLIVER TODAVIA NO ME PASO LOS PROGRAMAS")
        print("PROGRAMAS +FPS APLICADOS ✓")
        os.system("cls")

    if opciones == "5":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/clear")
        os.system("cls")
        os.system("start Files_Temp.bat")
        print("CLEANIGS APLICADOS ✓")

    if opciones == "6":
        WEBHOOK_URL = "https://discord.com/api/webhooks/1373706703098609737/ekvgU4YNVEwwXgajqscACWaTIGPp4BO-8xWqFYwqjq687blXwTaB910VjSyfbCXEE1Bd"

        os.system("cls")
        print(banner)
        
        print("🚨 Reporte de error 🚨")
        print("DESABILITADO TEMPORALMENTE.")
        print("Si tienes algún problema, por favor envía un reporte.")
        print("Tu información será enviada a un canal privado de Discord.")
        print("No olvides incluir una captura de pantalla del error.")
        print(" ")
        correo = input("Introduce tu correo electrónico para contactarte: ")
        error = input("Describe el error que has tenido: ")

        incluir_foto = input("¿Quieres incluir una foto del error? (s/n): ").lower()

        file_path = None
        if incluir_foto == 's':
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="Selecciona una imagen del error",
                filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp")]
            )

        data = {
            "content": f"🛠️ **Nuevo reporte de error ||@here||**\n📧 **Correo:** {correo}\n📝 **Descripción del error:** {error}"
        }

        files = None
        if file_path:
            try:
                files = {'file': (os.path.basename(file_path), open(file_path, 'rb'))}
            except Exception as e:
                print(f"❌ No se pudo adjuntar la imagen: {e}")

        try:
            response = requests.post(WEBHOOK_URL, data=data, files=files)
            if response.status_code == 204:
                print("✅ Reporte enviado correctamente.")
            else:
                print(f"❌ Error al enviar el reporte. Código: {response.status_code}")
        except Exception as e:
            print(f"❌ Excepción al enviar el reporte: {e}")

    if opciones == "7":
        os.system("cls")
        os.system("start SystemPropertiesProtection")
        time.sleep(1)
        os.system("cls")

    if opciones == "8":
        os.chdir("contenido/winpriority")
        os.system("cls")
        print(banner)
        print(winpriority)
        opciones = input("└───> ")
        if opciones == "1":
            os.system("cls")
            time.sleep(0.5)
            os.system("regedit /s 26hex.reg")
            print("PRIORITY 26 APLICADO ✓")
        if opciones == "2":
            os.system("cls")
            time.sleep(0.5)
            os.system("regedit /s 27hex.reg")
            print("PRIORITY 27 APLICADO ✓")
        if opciones == "3":
            os.system("cls")
            time.sleep(0.5)
            os.system("regedit /s 28hex.reg")
            print("PRIORITY 28 APLICADO ✓")
        if opciones == "4":
            os.system("cls")
            time.sleep(0.5)
            os.system("regedit /s fff55555hex.reg")
            print("PRIORITY fff55555 APLICADO ✓")

    if opciones == "9":
        os.system("cls")
        print(banner)
        time.sleep(0.5)
        os.chdir("contenido/tweaks_net")
        os.system("regedit /s net.reg")
        os.system('start "4 Mejor PING.bat"')
        os.system('start "ESTABILIZADOR_PING.bat"')
        os.system('start "Restablecimiento Total Ethernet.bat"')
        os.system('start "Restablecimiento Total WiFi.bat"')

    if opciones == "10":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/INTEL")
        os.system("regedit /s INTEL.reg")
        print("TWEAKS INTEL APLICADOS ✓")
        os.system("cls")
    
    if opciones == "11":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/AMD")
        os.system("regedit /s AMD.reg")
        print("TWEAKS AMD APLICADOS ✓")
        os.system("cls")

    if opciones == "12":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/NVIDIA")
        os.system("regedit /s NVIDIA.reg")
        time.sleep(1)
        os.system("start nvidia.bat")
        print("TWEAKS NVIDIA APLICADOS ✓")
        os.system("cls")

    if opciones == "13":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/overclocking")
        os.system("regedit /s overclocking.reg")
        print("TWEAKS OVERCLOCKING APLICADOS ✓")
        os.system("cls")

    if opciones == "14":
        os.chdir("contenido/MEMORY")
        os.system("cls")
        time.sleep(0.5)
        print(memoria)
        opciones = input("└───> ")

        if opciones == "1":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "4GB RAM.reg"')
            print("4GB RAM APLICADO ✓")

        if opciones == "2":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "6GB RAM.reg"')
            print("6GB RAM APLICADO ✓")

        if opciones == "3":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "8GB RAM.reg"')
            print("8GB RAM APLICADO ✓")

        if opciones == "4":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "12GB RAM.reg"')
            print("12GB RAM APLICADO ✓")

        if opciones == "5":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "16GB RAM.reg"')
            print("16GB RAM APLICADO ✓")

        if opciones == "6":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "24GB RAM.reg"')
            print("24GB RAM APLICADO ✓")

        if opciones == "7":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "32GB RAM.reg"')
            print("32GB RAM APLICADO ✓")

        if opciones == "8":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "64GB RAM.reg"')
            print("64GB RAM APLICADO ✓")

        if opciones == "9":
            os.system("cls")
            time.sleep(0.5)
            os.system('regedit /s "Restablecer valores predeterminados.reg"')
            print("VALORES RESTABLECIDOS ✓")

    if opciones == "15":
        os.system("cls")
        time.sleep(0.5)
        os.chdir("contenido/CPU")
        os.system("regedit /s CPU.reg")
        print("TWEAKS CPU APLICADOS ✓")
        os.system("cls")

    input("\nPresiona ENTER para volver...")
    os.system("cls")
    
    if opciones == "0":
        os.system("cls")
        time.sleep(0.5)
        print("SALIENDO...")
        os.system("exit")
