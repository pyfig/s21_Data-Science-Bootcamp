# python3 -m venv user
# source /Users/user/user/bin/activate 
#!/usr/bin/env python3
import os
import sys
import subprocess

class Librarian:
    def __init__(self):
        self.lib = []
    def check_venv(self):
        try:
            virtual_env = os.environ["VIRTUAL_ENV"]
            print(f"Your current virtual env is {virtual_env}")
        except KeyError:
            print("No virtual environment is currently active.")

    def install_lib(self):
        print("Установка библиотек...")
        requirements_file = "requirements.txt"        
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("Библиотеки установлены успешно!")

    def display_lib(self):
        installed_libraries = subprocess.check_output(["pip", "freeze"], text=True)
        print("Установленные библиотеки:")
        print(installed_libraries)

    def archive_lib(self):
        print("Архивация виртуального окружения...")
        env_path = sys.prefix
        archive_name = "venv_archive"
        subprocess.check_call(["tar", "-czf", f"{archive_name}.tar.gz", env_path])
        print(f"Виртуальное окружение успешно заархивировано!")

if __name__ == "__main__":
    try:
        librarian = Librarian()
        if not os.environ.get("VIRTUAL_ENV"):
            raise Exception("Этот скрипт должен быть запущен в виртуальном окружении")
            
        librarian.check_venv()
        librarian.install_lib()
        librarian.display_lib()
        librarian.archive_lib()
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
