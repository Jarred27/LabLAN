from fabric.api import run

"""
env.hosts = ['host1','host2']


def taskA():
    run('ls')


def taskB():
    run('whoami')


"""


def hello(who = "world"):
    print("Hello {who}!".format(who=who))

run("mkdir /tmp/trunk/")
run("uptime")
run("hostname")
result = run("ls -l /var/www")
result.failed


def host_type():
    run('uname -s')


def local_git():
    print("HI Local Git")
