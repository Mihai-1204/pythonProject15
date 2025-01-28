import os

import reportlab
from reportlab.pdfgen import canvas


def create_pdf(name: str, images_path: str = "images", y: int = 300):
    os.makedirs(".pdfs", exist_ok=True)

    new_pdf = canvas.Canvas(f"{name}.pdf")
    new_pdf.drawString(100, 100, "New PDF")
    images_list = os.listdir(images_path)

    for image in images_list:
        new_pdf.drawImage(f"./{images_path}/{image}",x=100, y=y)
        y -= 500

    new_pdf.save()