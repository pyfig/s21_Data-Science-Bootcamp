import os

def check_venv():
    try:
        virtual_env = os.environ["VIRTUAL_ENV"]
        print(f"Your current virtual env is {virtual_env}")
    except KeyError:
        print("No virtual environment is currently active.")

if __name__ == "__main__":
    check_venv()
