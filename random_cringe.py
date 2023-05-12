PREFIX = "https://vid.kinja.com/prod/"
POSTFIX = "_1080p.mp4"
MIN_N = 190001
MAX_N = 194680

from random import randint
import webbrowser


def get_random_cringe():
    n = randint(MIN_N, MAX_N)
    url = f"{PREFIX}{n}/{n}{POSTFIX}"
    webbrowser.open(url)


if __name__ == "__main__":
    get_random_cringe()
