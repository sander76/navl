import traceback
from pathlib import Path

from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.output.vt100 import Vt100_Output

from navl.file_tree_viewer import FileTreeViewer


def main():
    """Main entry point."""
    import sys

    root_path = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    if not root_path.exists:
        print(f"Error: Path {root_path!r} does not exist")
        sys.exit(1)

    footer = (
        "Use ↑↓→← to navigate, Enter to select and exit, 'r' to refresh, 'q' to quit"
    )
    try:
        layout = Layout(
            HSplit(
                [FileTreeViewer(root_path), Window(FormattedTextControl(text=footer))]
            )
        )
        app = Application[str](
            layout=layout,
            full_screen=True,
            mouse_support=True,
            output=Vt100_Output.from_pty(sys.stderr),
        )

        res = app.run()
        if res:
            print(res)
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        sys.exit(1)
