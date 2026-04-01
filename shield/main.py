import platform
import os
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
    
    # OPCIÓN 1: Iniciar Vigilancia en Tiempo Real (Por defecto)
    print("[+] Iniciando centinela de archivos...")
    start_watcher()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Loberia Shield desactivado por el usuario.")
