<div align="center">
  <img src="https://img.shields.io/badge/Nexu-Vision_Language-0f172a?style=for-the-badge&logo=huggingface" alt="NexuCaption Banner">
  <h1>Nexu Vision-Language Engine (NexuCaption) ✦</h1>
  <p><b>Enterprise Image Captioning using ViT & GPT-2 Modalities</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black)]()
  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![Status](https://img.shields.io/badge/Status-Production_Ready-success.svg)]()
</div>

---

## 🚀 The Vision

Tagging and describing massive libraries of image data is a severe operational bottleneck for media companies, digital asset management (DAM) platforms, and accessibility (A11Y) teams. Relying on human labor is unscalable, slow, and expensive. 

**NexuCaption** represents the pinnacle of multi-modal AI integration. By bridging Vision Transformers (ViT) with generative Language Models (GPT-2), it acts as an automated, high-precision image captioning service that delivers contextual semantic descriptions of visual data in milliseconds.

---

## 🏆 Unmatched Performance: Competitive Analysis

NexuCaption outclasses older CNN-RNN combinations and avoids the heavy API costs of enterprise cloud solutions.

| Feature | NexuCaption (Ours) | Cloud Vision API | Traditional CNN-RNN | AWS Rekognition |
|---------|-----------------|------------------|---------------------|-----------------|
| **Modality Architecture** | **ViT + GPT-2 Encoder/Decoder** | Proprietary Blackbox | CNN + LSTM | Proprietary Blackbox |
| **Generative Fluency** | **Extremely High (GPT-2)** | Moderate | Low (Formulaic) | Moderate |
| **Data Privacy** | **100% Local Processing** | Sent to Cloud | Local | Sent to Cloud |
| **Operating Cost**| **Zero (Open Source)**| High | Zero | High |
| **Custom Fine-Tuning**| **Yes (HuggingFace Integration)**| No | Yes | No |

By leveraging HuggingFace's `VisionEncoderDecoderModel`, NexuCaption achieves cloud-level accuracy while guaranteeing 100% data sovereignty (on-premise execution). 

---

## 🧠 Core Architecture & System Flow

```mermaid
graph TD
    A["Client UI - Image Upload"] -->|"POST Base64/Form"| B("FastAPI Gateway")
    B --> C{"Image Preprocessor"}
    C -->|"RGB Normalization"| D["Vision Transformer (ViT)"]
    D -->|"Latent Image Embeddings"| E["GPT-2 Autoregressive Decoder"]
    E -->|"Beam Search"| F["Semantic Text Sequence"]
    F --> G["JSON Response"]
    G -->|"Rendered UI"| A
```

### 1. The Encoder-Decoder Multi-Modal Pipeline
We utilize HuggingFace to seamlessly connect `vit-base-patch16-224-in21k` as the encoder and `gpt2` as the decoder. This means the visual features extracted by the ViT (the patches) are passed as cross-attention keys and values to the GPT-2 decoder. The language model then generates a highly descriptive caption, token by token, resulting in fluent, human-like descriptions.

### 2. Zero-Config VisionOS Frontend
The API is surfaced through a stunning, glassmorphism-inspired drag-and-drop interface. It leverages native browser APIs (like `FileReader`) to display image previews instantly, before transmitting the payload to the local FastAPI server for processing.

---

## 📂 Project Structure & Files

- `main.py`: The FastAPI server that handles image uploads and API routing.
- `caption_engine.py`: The heavy-lifting HuggingFace pipeline integrating ViT and GPT-2 models.
- `static/index.html`: The premium, Apple-inspired drag-and-drop web interface.
- `static/styles.css`: The CSS that powers the animations, glassmorphism, and responsive layout.
- `static/script.js`: Handles asynchronous file uploads, loading states, and DOM updates.

---

## ⚙️ Installation & Usage

### Prerequisites
- Python 3.10+
- PyTorch, Transformers, Pillow, FastAPI

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/lakshanmuruganandam/Nexu-Vision-Language.git
cd Nexu-Vision-Language

# 2. Install dependencies
pip install torch transformers pillow fastapi uvicorn python-multipart

# 3. Boot the API Server
python main.py
```
*Note: The first run will download the ViT-GPT2 model weights (~900MB) automatically from HuggingFace.*

---

## 🤝 Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📜 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---
<div align="center">
  <b>Seeing the world through silicon. Built by Lakshan Muruganandam.</b>
</div>
