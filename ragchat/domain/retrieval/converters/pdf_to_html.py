import fitz  # PyMuPDF


class PdfToHtmlConverter:

    def convert(self, buffer):
        doc = fitz.open("pdf", buffer)
        html = ""
        for page in doc:
            html += page.get_text("html")
        doc.close()
        return html
