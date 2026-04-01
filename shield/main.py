import platform
from core.scanner import cloud_scan
from core.quarantine import isolate_file

# TU LLAVE TÁCTICA
VT_API_KEY = "94279753f4b98eba82791d0761854a758631d5778f9d58fe7c9366484061ce39"

def process_threat(file_path):
    print(f"[*] Analizando objetivo: {file_path}")
    
    # Consultamos a la nube de Loberia
    result = cloud_scan(file_path, VT_API_KEY)
    print(result)
    
    if "DANGER" in result:
        print("[!] Procediendo a neutralización inmediata...")
        success, path = isolate_file(file_path)
        if success:
            print(f"[✔] Objetivo aislado en: {path}")
        else:
            print(f"[✘] Error en la extracción: {path}")

if __name__ == "__main__":
    print("="*50)
    print("      LOBERIA SHIELD XDR - ACTIVE DEFENSE")
    print("="*50)
    
    # Prueba táctica (puedes cambiar esto por una ruta real de un archivo sospechoso)
    # process_threat("C:/Descargas/archivo_raro.exe")
