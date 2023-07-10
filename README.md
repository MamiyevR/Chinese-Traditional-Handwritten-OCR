# Chinese-Traditional-Handwritten-OCR

Traditional Chinese Handwritten OCR tools.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install requirements.txt
```

## Run

Web app OCR tool: (http://127.0.0.1:8000/)
```bash
python website/main.py
```

TrOCR model: download pre-trained weights from [here](https://drive.google.com/drive/folders/1xycqMmZI9Pw5URtHcE6sXNutK6bY-IG7?usp=sharing) and place it in root folder
```bash
python TrOCR.py
```

EasyOCR model: another model with full image text extraction capabilities but have less accuracy compared to Nanonets. With training and fine-tune, accuracy can be increased
