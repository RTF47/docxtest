from docx2pdf import convert

def docx_to_pdf(docx_path, pdf_path):
    """Конвертирует DOCX в PDF"""
    convert(docx_path, pdf_path)
    print("PDF сохранён!")