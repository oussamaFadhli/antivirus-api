# services/antivirus_service.py
import clamd
from fastapi import UploadFile

class AntivirusService:
    def __init__(self, clamd_client: clamd.ClamdNetworkSocket):
        self.clamd_client = clamd_client

    def scan_file(self, file: UploadFile) -> dict:
        # Read file content in chunks
        file_content = file.file.read()
        
        # Perform the scan
        result = self.clamd_client.instream(file_content)
        file.file.seek(0)  # Reset file position for future reads
        
        # Process the result
        if result['stream'][0] == 'OK':
            return {"status": "clean"}
        else:
            return {
                "status": "infected",
                "malware": result['stream'][1]
            }
