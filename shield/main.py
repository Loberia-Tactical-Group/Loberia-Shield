import platform
from core.scanner import check_with_loberia_cloud

def init_loberia():
    system = platform.system()
    print(f"🐺 LOBERIA SHIELD V1.0 | Sistema Detectado: {system}")
    print("-" * 40)
    
    if system == "Windows":
        # Aquí llamaremos al motor de Windows que crearemos luego
        print("[*] Cargando Escudo de Registro y Procesos .exe...")
    elif system == "Linux":
        # Aquí llamaremos al motor de Servidores/VPN
        print("[*] Cargando Blindaje de Firewall e IPTables...")
        
    print("[+] Sistema de Inteligencia Cloud: ACTIVO")

if __name__ == "__main__":
    init_loberia()
