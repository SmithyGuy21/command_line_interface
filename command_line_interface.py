from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls

def print_banner(text):
    print(Figlet(font="slant").renderText(text))


def get_files():
    ls_output = ls().strip()
    files = ls_output.split("\n")
    return files   


def test_get_files():
    files = get_files()
    assert len(files) == 5, "There should be 5 files"


class FancyGitAdd(cli.Application):
    VERSION = "1.1"
    def main(self):
        print_banner("Welcome to Fancy Git Add!")

if __name__ == "__main__":
    FancyGitAdd()
    get_files()

