from fabric.api import run


def hello(who = "world"):
    print("Hello {who}!".format(who=who))


