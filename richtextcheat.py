from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.progress import Progress
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel
from rich.spinner import Spinner
import time

# Create a Console instance
console = Console()

def display_basic_usage():
    code = 'console.print("Hello, [bold magenta]World[/bold magenta]!")'
    console.print(f"Code:\n{code}\n")
    console.print("Hello, [bold magenta]World[/bold magenta]!")
    
def display_text_styling():
    codes = [
        'Text("Bold Text", style="bold")',
        'Text("Italic Text", style="italic")',
        'Text("Underlined Text", style="underline")',
        'Text("Colored Text", style="red")',
        'Text("Text with Background", style="on green")',
        'Text("Bold and Italic", style="bold italic")'
    ]
    for code in codes:
        console.print(f"Code:\nconsole.print({code})\n")
        exec(f'console.print({code})')
        print(f"\n")
        
def display_table():
    code = """\
table = Table(title="Sample Table")
table.add_column("Column 1")
table.add_column("Column 2")
table.add_row("Row 1 Col 1", "Row 1 Col 2")
table.add_row("Row 2 Col 1", "Row 2 Col 2")
console.print(table)

table = Table(title="Aligned Table")
table.add_column("Left", justify="left")
table.add_column("Center", justify="center")
table.add_column("Right", justify="right")
table.add_row("Left", "Center", "Right")
console.print(table)
"""
    console.print(f"Code:\n{code}\n")
    table = Table(title="Sample Table")
    table.add_column("Column 1")
    table.add_column("Column 2")
    table.add_row("Row 1 Col 1", "Row 1 Col 2")
    table.add_row("Row 2 Col 1", "Row 2 Col 2")
    console.print(table)

    table = Table(title="Aligned Table")
    table.add_column("Left", justify="left")
    table.add_column("Center", justify="center")
    table.add_column("Right", justify="right")
    table.add_row("Left", "Center", "Right")
    console.print(table)
    print(f"\n")
def display_progress_bar():
    code = """\
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.05)
"""
    console.print(f"Code:\n{code}\n")
    with Progress() as progress:
        task = progress.add_task("Processing...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.05)
    print(f"\n")
def display_markdown():
    code = """\
markdown = Markdown("# Hello World\\nThis is **bold** text.")
console.print(markdown)
"""
    console.print(f"Code:\n{code}\n")
    markdown = Markdown("# Hello World\nThis is **bold** text.")
    console.print(markdown)
    print(f"\n")
def display_code_block():
    code = """\
code = '''def hello_world():
    print("Hello, World!")'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
"""
    console.print(f"Code:\n{code}\n")
    code = """def hello_world():
    print("Hello, World!")"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    print(f"\n")
def display_panel():
    codes = [
        'Panel("This is a panel", title="Panel Title")',
        'Panel("This is another panel", title="Panel Title", border_style="bright_blue")'
    ]
    for code in codes:
        console.print(f"Code:\nconsole.print({code})\n")
        panel = eval(f'Panel({code})')
        console.print(panel)
    print(f"\n")
def display_spinner():
    code = """\
with console.status("Processing...", spinner="dots"):
    time.sleep(10)  # Simulating some processing time
"""
    console.print(f"Code:\n{code}\n")
    with console.status("Processing...", spinner="dots"):
        time.sleep(10)  # Simulating some processing time

if __name__ == "__main__":
    display_basic_usage()
    time.sleep(1)
    print(f"\n")
    display_text_styling()
    time.sleep(1)
    print(f"\n")
    display_table()
    time.sleep(1)
    print(f"\n")
    display_progress_bar()
    time.sleep(1)
    print(f"\n")
    display_markdown()
    time.sleep(1)
    print(f"\n")
    display_code_block()
    time.sleep(1)
    print(f"\n")
    display_panel()
    time.sleep(1)
    print(f"\n")
    display_spinner()
    time.sleep(1)
    print(f"\n")
    pause = input("Press Enter to exit..")
