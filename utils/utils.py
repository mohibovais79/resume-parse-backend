from PIL import Image
from rapidocr_onnxruntime import RapidOCR


def allowed_file(filename: str) -> bool:
    allowed_extensions = {".docx", ".png", ".jpg", ".jpeg", ".pdf"}
    return any(filename.lower().endswith(ext) for ext in allowed_extensions)


def ocr_extraction(image: Image.Image) -> str:
    engine = RapidOCR()
    result, elapse = engine(image)
    extracted_texts = [
        "".join(c for c in item[1] if c.isprintable()).replace("\n", "").replace("/n", "").strip() for item in result
    ]
    return " ".join(extracted_texts)




