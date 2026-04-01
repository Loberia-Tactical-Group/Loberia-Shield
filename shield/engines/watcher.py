import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.scanner import cloud_scan
from core.quarantine import isolate_file

# --- CONFIGURACIÓN TÁCTICA ---
WATCH_PATH = "C:/Users/Carlos/Downloads" # Ajusta a tu ruta real
API_KEY = "94279753f4b98eba82791d0761854a758631d5778f9d58fe7c9366484061ce39"

class LoberiaHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            print(f"\n[!] Nuevo objetivo detectado: {file_path}")
            
            # Análisis automático
            result = cloud_scan(file_path, API_KEY)
            print(f"[*] Resultado: {result}")
            
            if "DANGER" in result:
                print("[!] Amenaza confirmada. Ejecutando protocolo de extracción...")
                success, final_path = isolate_file(file_path)
                if success:
                    print(f"[✔] Amenaza neutralizada en: {final_path}")

def start_watcher():
    event_handler = LoberiaHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    observer.start()
    print(f"🐺 LOBERIA WATCHER | Vigilando perímetro: {WATCH_PATH}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watcher()
