from pyfiglet import Figlet
from plumbum import cli

def print_banner(text):
    print(Figlet(font="slant").renderText(text))


def get_files():
    return []   # incomplete function
class FancyGitAdd(cli.Application):
    VERSION = "1.1"
    def main(self):
        print("Welcome to Fancy Git Add!")

if __name__ == "__main__":
    FancyGitAdd()
