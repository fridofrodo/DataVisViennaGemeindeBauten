import folium
from IPython.display import IFrame

# Path to the HTML file
file_path = 'path/to/your/gemeindebauten_wien_interactive_buffered_constrained.html'

# Display the HTML file in an IFrame
IFrame(src=file_path, width='100%', height='600px')
