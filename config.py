'Environment variables'

import os

PATH_CURRENT = os.getcwd()

# configuration
config = {
    # paths folder
    "path_folder_results": PATH_CURRENT + "\\report",
    "path_folder_txts": PATH_CURRENT + "\\files",

    # paths files
    "path_result_txt": PATH_CURRENT + "\\report\\result.txt",
    "path_result_pdf": PATH_CURRENT + "\\report\\result.pdf",

    # email
    "email": "robot.test.beta@gmail.com",
    "password": "ekefiwxwbmtvilkm", # app password
    "port": 465,
    "smtp_server": "smtp.gmail.com",
}

# print(config)
