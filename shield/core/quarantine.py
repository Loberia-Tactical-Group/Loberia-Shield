import os
import shutil
from datetime import datetime

# Directorio seguro de Loberia
QUARANTINE_DIR = "C:/Loberia_Shield/Quarantine"

def init_quarantine():
    """Crea la zona de aislamiento si no existe."""
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
        # En una versión avanzada, aquí quitaríamos permisos de ejecución
        print(f"[*] Zona de Cuarentena establecida en: {QUARANTINE_DIR}")

def isolate_file(file_path):
    """Mueve el archivo a la zona de aislamiento y lo neutraliza."""
    try:
        init_quarantine()
        file_name = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Cambiamos el nombre para que no sea ejecutable (.exe -> .loberia)
        new_name = f"INFECTED_{timestamp}_{file_name}.loberia"
        dest_path = os.path.join(QUARANTINE_DIR, new_name)
        
        shutil.move(file_path, dest_path)
        
        # Creamos un log táctico del arresto
        with open(os.path.join(QUARANTINE_DIR, "incident_log.txt"), "a") as log:
            log.write(f"[{datetime.now()}] NEUTRALIZADO: {file_name} -> {new_name}\n")
            
        return True, dest_path
    except Exception as e:
        return False, str(e)
