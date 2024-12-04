MAIN_URL = "https://www.ilovepdf.com/ru"
MERGE_URL = "https://www.ilovepdf.com/ru/merge_pdf"


TIMEOUT = 10
MAX_RETRIES = 5

# AUTH
LOGIN_URL = "https://www.ilovepdf.com/ru"
AUTH_EMAIL_CORRECT = "sizovivan.05@gmail.com"
AUTH_PASSWORD_OLD = "3&OF;%^G}X{o"
AUTH_PASSWORD_CORRECT = "'~7G.mqWoH*&"
AUTH_PASSWORD_INVALID = "123123"



def update_config(old_password, new_password):
    with open("config.py", "r") as file:
        lines = file.readlines()

    with open("config.py", "w") as file:
        for line in lines:
            if line.startswith("AUTH_PASSWORD_OLD"):
                file.write(f'AUTH_PASSWORD_OLD = "{old_password}"\n')
            elif line.startswith("AUTH_PASSWORD_CORRECT"):
                file.write(f'AUTH_PASSWORD_CORRECT = "{new_password}"\n')
            else:
                file.write(line)
