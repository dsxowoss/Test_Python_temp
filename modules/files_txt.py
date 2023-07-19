'Merge contents of txt files into a single file'

import os
from config import config


def merge_files_txt():
    """Generate result file txt"""

    try:
        # path of folder with txt files
        path_folder = config["path_folder_txts"]

        # path of result file txt
        path_result = config["path_result_txt"]

        # clean result file txt
        with open(path_result, "w", encoding="utf-8") as file_result:
            file_result.write("")

        # iterate and extract txt files
        for name_file in os.listdir(path_folder):

            path_file = os.path.join(path_folder, name_file)
            # print(path_file)

            # read files txt
            with open(path_file, "r", encoding="utf-8") as file:

                # write in result file txt
                with open(path_result, "a", encoding="utf-8") as file_result:
                    file_result.write(file.read() + "\n")

        print("2. Merge files txt successfully")

    except Exception as error:
        # catching error
        raise Exception(f"Error merge files txt: {error}")


# if __name__ == "__main__":
#     merge_files_txt()
