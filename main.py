# main.py
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from services.antivirus_service import AntivirusService
from dependencies import get_antivirus_service

app = FastAPI()

@app.post("/scan-file/")
async def scan_file(
    file: UploadFile = File(...),
    antivirus_service: AntivirusService = Depends(get_antivirus_service)
):
    # Check file type
    if not file.content_type.startswith("application/") and not file.content_type.startswith("text/"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # Scan the file
    scan_result = antivirus_service.scan_file(file)
    
    return scan_result
