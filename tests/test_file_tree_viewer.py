from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from navl.file_tree_viewer import FileTreeViewer, TreeNode


@pytest.fixture
def test_path(tmp_path: Path):
    (tmp_path / "src" / "my_lib").mkdir(exist_ok=True, parents=True)
    (tmp_path / "src" / "main.py").touch()
    (tmp_path / "src" / "docs").mkdir(exist_ok=True, parents=True)
    return tmp_path


def test_collect_expanded_paths(test_path: Path):
    """Test the _collect_expanded_paths method."""
    root_node = TreeNode(test_path / "src")
    root_node.load_children()
    root_node.children[1].expanded = True  # expanding one path here.

    expanded = tuple(FileTreeViewer._collect_expanded_paths(root_node))

    assert expanded == (test_path / "src" / "my_lib",)


def test_collect_expanded_paths_no_expanded_nodes(test_path: Path):
    """Test _collect_expanded_paths when no nodes are expanded."""
    root_node = TreeNode(test_path / "src")
    root_node.load_children()

    expanded = tuple(FileTreeViewer._collect_expanded_paths(root_node))

    assert len(expanded) == 0


def test_collect_visible_nodes(test_path: Path):
    """Test the _collect_visible_nodes method."""
    viewer = FileTreeViewer(test_path)
    viewer._update_display()

    assert [node.path for node in viewer.visible_nodes] == [
        test_path,
        test_path / "src",
    ]


def test_collect_visibile_nodes_expanded(test_path: Path):
    viewer = FileTreeViewer(test_path)

    viewer._update_display()

    viewer.visible_nodes[1].toggle_expanded()  # expanding the src folder
    viewer._update_display()

    assert [node.path for node in viewer.visible_nodes] == [
        test_path,
        test_path / "src",
        test_path / "src" / "docs",
        test_path / "src" / "main.py",
        test_path / "src" / "my_lib",
    ]
