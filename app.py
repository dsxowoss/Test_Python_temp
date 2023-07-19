'App'

from modules.functions import validate_folder, validate_input_email
from modules.files_txt import merge_files_txt
from modules.files_pdf import convert_txt_to_pdf
from modules.send_mail import send_mail


def app():
    """Main function"""

    try:
        validate_folder()
        merge_files_txt()
        convert_txt_to_pdf()

        # get input email
        input_email = validate_input_email()
        send_mail(input_email)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    app()
