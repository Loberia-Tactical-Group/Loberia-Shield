import platform
import os
import sys

# Esto obliga a que el programa busque librerías en su propia carpeta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import watchdog
except ImportError:
    print("Error crítico: Watchdog no encontrado")
from core.scanner import cloud_scan 
from core.quarantine import isolate_file
from engines.watcher import start_watcher 

# --- CONFIGURACIÓN GLOBAL DE LOBERIA ---
VT_API_KEY = "94279753f4b98eba82791d0761854a758631d5778f9d58fe7c9366484061ce39"

def process_threat(file_path):
    """Analiza y procesa una amenaza específica."""
    print(f"[*] Analizando objetivo: {file_path}")
    
    # Consultamos a la nube de Loberia
    result = cloud_scan(file_path, VT_API_KEY)
    print(f"[*] Resultado: {result}")
    
    if "DANGER" in result or "❌" in result:
        print("[!] Procediendo a neutralización inmediata...")
        success, path = isolate_file(file_path)
        if success:
            print(f"[✔] Objetivo aislado en: {path}")
        else:
            print(f"[✘] Error en la extracción: {path}")

def main():
    """Punto de entrada principal del Sistema Shield."""
    system = platform.system()
    
    print("="*50)
    print("      LOBERIA SHIELD XDR - ACTIVE DEFENSE")
    print(f"      Status: ACTIVE | OS: {system}")
    print("="*50)
    
    # --- AJUSTE TÁCTICO DE RUTA ---
    # Esto asegura que el programa siempre encuentre una carpeta válida para vigilar
    path_to_watch = os.path.expanduser("~\\Downloads") 
    
    print(f"[+] Iniciando centinela de archivos en: {path_to_watch}")
    
    # Pasamos la ruta a la función para que no de error
    start_watcher(path_to_watch)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Loberia Shield desactivado por el usuario.")
