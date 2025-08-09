# navl

A terminal-based file tree navigator.

## Overview

navl is an interactive file tree viewer that allows you to navigate directory structures directly from your terminal.

## Features

- **Interactive Navigation**: Use arrow keys to move through the file tree
- **Expand/Collapse**: Toggle directories to show or hide their contents
- **Path Selection**: Select a file or directory path and have it printed to stdout. Use this for piping into other commands.

## Installation

`pip install navl`

or better use `pipx` or `uv tool` and you'll have a navl command available in your prompt.

## terminal usage

cd into a folder using navl. Put this bash function inside your `.bashrc` or `.zshrc` file.

```bash
# A function to visually change directories with navl
lcd() {
    local selected_dir
    selected_dir=$(navl)
    
    # If the user selected a path (and didn't just quit), `cd` into it.
    # Check if the selection is a directory.
    if [[ -n "$selected_dir" && -d "$selected_dir" ]]; then
        cd "$selected_dir"
    fi
}
```
