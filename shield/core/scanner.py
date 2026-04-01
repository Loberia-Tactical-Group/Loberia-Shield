import hashlib
import requests

# Esta es la llave que conecta a Loberia con la base de datos mundial
VT_API_KEY = "TU_API_KEY_AQUI" # Luego te explico cómo sacarla gratis
VT_URL = "https://www.virustotal.com/api/v3/files/"

def get_file_hash(file_path):
    """Genera la huella digital del archivo (SHA-256)."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_with_loberia_cloud(file_path):
    """Consulta si el archivo es peligroso en la nube."""
    file_hash = get_file_hash(file_path)
    headers = {"x-apikey": VT_API_KEY}
    
    response = requests.get(f"{VT_URL}{file_hash}", headers=headers)
    
    if response.status_code == 200:
        stats = response.json()['data']['attributes']['last_analysis_stats']
        malicious = stats['malicious']
        if malicious > 0:
            return f"[❌] AMENAZA: Detectada por {malicious} antivirus."
        return "[✅] LIMPIO: El archivo es seguro."
    elif response.status_code == 404:
        return "[?] DESCONOCIDO: Archivo nuevo, procediendo con cautela."
    else:
        return "[!] ERROR: No hay conexión con la central Loberia."
