from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def game(ctx):
    ctx.run("python3 src/ponggame.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)