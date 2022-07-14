from os import system, path


class App:
    @staticmethod
    def start():
        App.__install_dependencies()
        App.__run_server()

    @staticmethod
    def __install_dependencies():
        try:
            import django
        except ModuleNotFoundError:
            if path.isfile('requirements.txt'):
                system('pip install -r requirements.txt')
            else:
                print("There are not enough dependencies to run the module.\n"
                      "Please download the requirements.txt file from:\n"
                      "https://github.com/Allen-Avanheim/softformance_6/blob/master/requirements.txt")
                exit()

    @staticmethod
    def __run_server():
        system('python manage.py runserver')


if __name__ == "__main__":
    app = App()
    app.start()
