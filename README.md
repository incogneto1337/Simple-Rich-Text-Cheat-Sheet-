---

# Rich Text Cheat Sheet

This script demonstrates various features of the `rich` library in Python, which is used for rich text formatting in the terminal. Each function in the script displays a different aspect of what `rich` can do, including text styling, tables, progress bars, and more.

## Features

1. **Basic Usage**: Shows how to print text with basic styling.
2. **Text Styling**: Demonstrates different text styles such as bold, italic, underlined, and colored text.
3. **Table**: Displays tables with columns and rows, including alignment options.
4. **Progress Bar**: Shows how to use progress bars to indicate ongoing tasks.
5. **Markdown**: Renders markdown text in the terminal.
6. **Code Block**: Displays code with syntax highlighting.
7. **Panel**: Creates panels with titles and optional border styles.
8. **Spinner**: Demonstrates a spinner that indicates processing or loading.

## Installation

To use this script, you need to have Python and the `rich` library installed. You can install `rich` using pip:

```bash
pip install rich
```

## Usage

1. **Save the Script**: Save the provided Python code to a file, for example, `rich_cheatsheet.py`.

2. **Run the Script**: Execute the script from the terminal:

    ```bash
    python rich_cheatsheet.py
    ```

3. **View Output**: The script will display each feature with a code preview and its output. Press Enter when prompted to exit the script.

## Code Overview

- **`display_basic_usage()`**: Prints basic text with styling.
- **`display_text_styling()`**: Demonstrates various text styles.
- **`display_table()`**: Shows how to create and print tables.
- **`display_progress_bar()`**: Illustrates the use of progress bars.
- **`display_markdown()`**: Renders markdown text.
- **`display_code_block()`**: Displays code with syntax highlighting.
- **`display_panel()`**: Creates and prints panels.
- **`display_spinner()`**: Displays an indefinite spinner.

## Example Output

### Basic Usage

**Code:**
```python
console.print("Hello, [bold magenta]World[/bold magenta]!")
```
**Output:**
Hello, [bold magenta]World[/bold magenta]!

### Text Styling

**Code:**
```python
Text("Bold Text", style="bold")
```
**Output:**
Text("Bold Text", style="bold")

### Table

**Code:**
```python
table = Table(title="Sample Table")
table.add_column("Column 1")
table.add_column("Column 2")
table.add_row("Row 1 Col 1", "Row 1 Col 2")
table.add_row("Row 2 Col 1", "Row 2 Col 2")
console.print(table)
```
**Output:**
(Displays a sample table with columns and rows)

### Progress Bar

**Code:**
```python
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.05)
```
**Output:**
(Displays a progress bar updating over time)

### Markdown

**Code:**
```python
markdown = Markdown("# Hello World\nThis is **bold** text.")
console.print(markdown)
```
**Output:**
(Displays rendered markdown text)

### Code Block

**Code:**
```python
code = '''def hello_world():
    print("Hello, World!")'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```
**Output:**
(Displays highlighted Python code)

### Panel

**Code:**
```python
Panel("This is a panel", title="Panel Title")
```
**Output:**
(Displays a panel with a title)

### Spinner

**Code:**
```python
with console.status("Processing...", spinner="dots"):
    time.sleep(10)
```
**Output:**
(Displays a spinner spinning indefinitely)

## License

This script is provided under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
