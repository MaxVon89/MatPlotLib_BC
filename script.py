import json
import os
import glob
from pathlib import Path

def load_notebook(file_path):
    """Load .ipynb file and return its JSON structure."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(nb_data, file_path):
    """Save notebook JSON structure to file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb_data, f, indent=1, ensure_ascii=False)

def merge_notebooks(parent_path, subdir_path):
    """Merge all .ipynb files from subdir into parent."""
    
    # Load parent notebook
    parent_nb = load_notebook(parent_path)
    parent_cells = parent_nb['cells']
    
    merged_cells = parent_cells.copy()
    
    # Find all .ipynb files recursively in subdir
    nb_pattern = os.path.join(subdir_path, "**/*.ipynb")
    notebook_files = glob.glob(nb_pattern, recursive=True)
    
    print(f"Found {len(notebook_files)} notebooks to merge")
    
    for nb_file in sorted(notebook_files):  # Alphabetical order
        print(f"Merging: {nb_file}")
        
        # Load child notebook
        child_nb = load_notebook(nb_file)
        
        # Add separator cell (optional - shows source file)
        separator = {
            "cell_type": "markdown",
            "source": [f"---\n**Source:** `{nb_file}`\n---"],
            "metadata": {}
        }
        merged_cells.append(separator)
        
        # Append all cells from child notebook
        merged_cells.extend(child_nb['cells'])
    
    # Update parent notebook cells
    parent_nb['cells'] = merged_cells
    

    # Save merged notebook
    save_notebook(parent_nb, parent_path)
    print(f"\n✅ Merged! Saved to {"D:\Documents\Programming\Languages\Python\Python Tutorials\Python-Libraries\MatPlotLib\MatPlotLib_BC"}")
    print(f"Total cells: {len(merged_cells)}")

if __name__ == "__main__":
    # Current directory setup:
    # parentDir/
    # |_ parent.ipynb  ← this gets updated
    # |_ subDir/       ← scan here
    
    parent_file = "MPL_TypesOfPlots.ipynb"
    subdir = "plot_types_jupyter"
    
    if os.path.exists(parent_file) and os.path.exists(subdir):
        merge_notebooks(parent_file, subdir)
    else:
        print(f"❌ Need '{parent_file}' and '{subdir}' in current directory")