import io
import time
import asyncio
import threading
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = FastAPI(title="Vision-Language Neural Engine")

processor = None
model = None
is_loading = False

def load_model_in_background():
    global processor, model, is_loading
    if model is not None or is_loading:
        return
    is_loading = True
    print("-> [BACKGROUND] Allocating memory to CPU (Stability Mode)...")
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        model.to("cpu")
        print("-> [BACKGROUND] Warming up shaders...")
        dummy_image = Image.new('RGB', (224, 224), color='black')
        inputs = processor(dummy_image, return_tensors="pt").to("cpu")
        model.generate(**inputs, max_new_tokens=20, num_beams=1)
        print("✅ [BACKGROUND] NEURAL ENGINE ONLINE AND READY!")
    except Exception as e:
        print(f"❌ [BACKGROUND] ERROR LOADING MODEL: {e}")
    finally:
        is_loading = False

@app.on_event("startup")
async def startup_event():
    threading.Thread(target=load_model_in_background, daemon=True).start()

@app.post("/api/caption")
async def generate_caption(file: UploadFile = File(...)):
    global processor, model, is_loading
    
    if model is None:
        if is_loading:
            return {"caption": "The AI is currently booting into RAM. Please wait a few seconds and try again!", "status": "loading"}
        else:
            return {"caption": "AI failed to boot.", "status": "error"}
    
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        
        start_time = time.time()
        
        inputs = processor(image, return_tensors="pt").to("cpu")
        out = model.generate(**inputs, max_new_tokens=30, num_beams=1)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        exec_ms = (time.time() - start_time) * 1000

        return {
            "caption": caption, 
            "status": "success",
            "telemetry": {
                "model": "Salesforce/blip-image-captioning-base",
                "execution_ms": f"{exec_ms:.1f}ms",
                "framework": "PyTorch (Native)"
            }
        }
    except Exception as e:
        return {"caption": str(e), "status": "error"}

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
