from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn
from rich.live import Live
from rich.logging import RichHandler
from rich.traceback import install
from rich.pretty import Pretty
import logging
import time
import random

install()
console = Console()


def demo_table():
    table = Table(title="Fruits and Prices", box=box.ROUNDED, show_lines=True)
    table.add_column("Fruit", justify="left", style="bold cyan")
    table.add_column("Quantity", justify="right", style="magenta")
    table.add_column("Price", justify="right", style="green")

    table.add_row("Apple", "10", "$0.50")
    table.add_row("Banana", "5", "$0.30")
    table.add_row("Cherry", "20", "$1.50")

    console.print(table)


def demo_syntax():
    code = """
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(10))
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title="Python Syntax"))


def demo_markdown():
    md = Markdown("""
# Rich Markdown

* Rich can render **markdown** natively.
* It's great for documentation and READMEs.

- item 1
- item 2

> Quote example
""")
    console.print(md)


def demo_tree():
    tree = Tree("📁 Project")
    src = tree.add("src")
    src.add("main.py")
    src.add("utils.py")
    tree.add("README.md")
    tree.add("requirements.txt")
    console.print(tree)


def demo_panels():
    p1 = Panel("This is an info panel", title="Info", style="bold white on blue")
    p2 = Panel("This is a warning", title="Warning", style="bold white on red")
    console.print(p1)
    console.print(p2)


def demo_progress():
    console.print("Progress examples:")
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(),
        "{task.completed}/{task.total}",
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("Processing", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)


def demo_live():
    console.print("Live updating table:")
    items = [(f"task{i}", 0) for i in range(5)]
    with Live(refresh_per_second=4) as live:
        for _ in range(30):
            table = Table(box=box.MINIMAL)
            table.add_column("Task")
            table.add_column("Progress")
            for i, (name, val) in enumerate(items):
                val = min(100, val + random.randint(1, 10))
                items[i] = (name, val)
                table.add_row(name, f"{val}%")
            live.update(table)
            time.sleep(0.15)


def demo_logging():
    logging.basicConfig(level="NOTSET", handlers=[RichHandler()])
    log = logging.getLogger("rich_demo")
    log.info("This is an info message")
    log.warning("This is a warning")
    log.error("This is an error with a {value}", extra={"value": 42})


def demo_pretty():
    data = {
        "users": [
            {"id": i, "name": f"user{i}", "tags": ["tester", "admin"]} for i in range(3)
        ]
    }
    console.print(Pretty(data))


def demo_traceback():
    console.print("Demonstrating a formatted traceback (intentional error):")

    def raise_error():
        x = 1 / 0

    try:
        raise_error()
    except Exception:
        console.print_exception()


if __name__ == "__main__":
    console.rule("Rich showcase")
    demo_table()
    console.rule()
    demo_syntax()
    console.rule()
    demo_markdown()
    console.rule()
    demo_tree()
    console.rule()
    demo_panels()
    console.rule()
    demo_progress()
    console.rule()
    demo_live()
    console.rule()
    demo_logging()
    console.rule()
    demo_pretty()
    console.rule()
    demo_traceback()
    console.rule("End showcase")
