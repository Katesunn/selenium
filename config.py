MAIN_URL = "https://www.ilovepdf.com/ru"
MERGE_URL = "https://www.ilovepdf.com/ru/merge_pdf"


TIMEOUT = 10
MAX_RETRIES = 5

# AUTH
LOGIN_URL = "https://www.ilovepdf.com/ru"
AUTH_EMAIL_CORRECT = "solntsevakate6@gmail.com"
AUTH_PASSWORD_OLD = "123123"
AUTH_PASSWORD_CORRECT = "LJh$1NU~]1[W"
AUTH_PASSWORD_INVALID = "111111"



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
