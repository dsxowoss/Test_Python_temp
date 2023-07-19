'Convert file txt to pdf'

import fitz
from config import config


def convert_txt_to_pdf():
    """Generate file pdf"""

    try:
        # path of file txt
        path_txt = config["path_result_txt"]

        # path of file pdf
        path_pdf = config["path_result_pdf"]
        # print(path_pdf)

        # read file txt
        with open(path_txt, 'r', encoding="utf-8") as file:
            content = file.read()
            # print(content)

        # create new file pdf
        doc_pdf = fitz.open()

        # create new page pdf
        page_pdf = doc_pdf.new_page()

        # Set the font and font size
        font = "Times-Roman"
        font_size = 8

        # insert text in page pdf
        page_pdf.insert_text(fitz.Point(50, 50), content, fontsize=font_size, fontname=font)

        # save file pdf
        doc_pdf.save(path_pdf)
        doc_pdf.close()

        print("3. Convert file txt to pdf successfully")

    except Exception as error:
        # catching error
        raise Exception(f"Error generate file pdf: {error}")


# if __name__ == "__main__":
#     convert_txt_to_pdf()
