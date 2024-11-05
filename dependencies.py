# dependencies.py
import clamd
from services.antivirus_service import AntivirusService

def get_clamd_client() -> clamd.ClamdNetworkSocket:
    return clamd.ClamdNetworkSocket(host="localhost", port=3310)

def get_antivirus_service() -> AntivirusService:
    clamd_client = get_clamd_client()
    return AntivirusService(clamd_client=clamd_client)
