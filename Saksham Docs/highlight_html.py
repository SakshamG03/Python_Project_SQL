from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

with open("D:\Dell\Desktop\CS Project\Python_Project_SQL\shopping management.py", 'r') as file:
    code = file.read()

# Generate HTML with syntax highlighting
formatter = HtmlFormatter(full=True, style="default")  # Use 'default' style for IDLE-like colors
with open('output.html', 'w') as output_file:
    output_file.write(highlight(code, PythonLexer(), formatter))

print("HTML file created as 'output.html'.")
