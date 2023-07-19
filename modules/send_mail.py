'Send mail using smtplib and gmail'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import config


def send_mail(to_email):
    """Send report PDF by email"""

    try:
        # create the message
        message = MIMEMultipart()
        message['Subject'] = "Report PDF"
        message['From'] = config["email"]
        message['To'] = to_email

        # add body to message
        message.attach(MIMEText("Report PDF", 'plain'))

        # open pdf file in binary mode
        with open(config["path_result_pdf"], 'rb') as pdf_file:

            # Create a mimebase object
            part = MIMEBase('application', 'octet-stream')

            # set content pdf in object mimebase
            part.set_payload(pdf_file.read())

            # use encode base64
            encoders.encode_base64(part)

            # add name file
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {"result.pdf"}'
            )

            # attach file pdf to message
            message.attach(part)

        # establish connection using SSL
        with smtplib.SMTP_SSL(config["smtp_server"], config["port"]) as smtp_server:

            # login in account gmail
            smtp_server.login(config["email"], config["password"])

            # send email
            smtp_server.sendmail(config["email"], to_email, message.as_string())
            print(f"4. Email sent successfully to {to_email}")

    except Exception as error:
        # catching error
        raise Exception(f"Error send mail: {error}")


# if __name__ == "__main__":
#     send_mail("munguiahuaman@gmail.com")
