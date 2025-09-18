from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil, uuid, os, subprocess
from pathlib import Path

app = FastAPI()
WORKDIR = Path(__file__).resolve().parents[1] / 'jobs'
WORKDIR.mkdir(exist_ok=True, parents=True)

@app.post('/remove')
async def remove(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    job_dir = WORKDIR / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    input_path = job_dir / file.filename
    with open(input_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    output_path = job_dir / ('no_watermark_' + file.filename)
    # spawn worker
    subprocess.Popen(['python', str(Path(__file__).resolve().parents[1] / 'worker' / 'remove.py'), str(input_path), str(output_path)])
    return JSONResponse({'job_id': job_id, 'output': str(output_path)})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=9000, reload=True)
