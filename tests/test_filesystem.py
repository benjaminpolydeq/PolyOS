"""Tests for VirtualDirectory and VirtualFile classes."""
import pytest
from exemple.filesystem import VirtualFile, VirtualDirectory


class TestVirtualFile:
    """Test VirtualFile class."""

    def test_file_init_with_name_only(self):
        """Test VirtualFile initialization with name only."""
        file = VirtualFile("test.txt")
        assert file.name == "test.txt"
        assert file.content == ""

    def test_file_init_with_name_and_content(self):
        """Test VirtualFile initialization with name and content."""
        file = VirtualFile("readme.txt", "Hello, World!")
        assert file.name == "readme.txt"
        assert file.content == "Hello, World!"

    def test_file_content_empty_string(self):
        """Test file content defaults to empty string."""
        file = VirtualFile("empty.txt")
        assert isinstance(file.content, str)
        assert file.content == ""

    def test_file_content_multiline(self):
        """Test file can contain multiline content."""
        content = "Line 1\nLine 2\nLine 3"
        file = VirtualFile("multiline.txt", content)
        assert file.content == content
        assert "\n" in file.content

    def test_file_content_special_characters(self):
        """Test file content with special characters."""
        content = "Special chars: !@#$%^&*()"
        file = VirtualFile("special.txt", content)
        assert file.content == content

    def test_file_name_with_extension(self):
        """Test file names with various extensions."""
        file_txt = VirtualFile("doc.txt")
        file_py = VirtualFile("script.py")
        file_no_ext = VirtualFile("README")

        assert file_txt.name == "doc.txt"
        assert file_py.name == "script.py"
        assert file_no_ext.name == "README"


class TestVirtualDirectory:
    """Test VirtualDirectory class."""

    def test_directory_init(self):
        """Test VirtualDirectory initialization."""
        dir = VirtualDirectory("root")
        assert dir.name == "root"
        assert dir.children == {}

    def test_directory_init_empty_children(self):
        """Test directory children starts as empty dict."""
        dir = VirtualDirectory("test_dir")
        assert isinstance(dir.children, dict)
        assert len(dir.children) == 0

    def test_add_file_single(self):
        """Test adding a single file to directory."""
        dir = VirtualDirectory("root")
        dir.add_file("file.txt", "content")
        assert "file.txt" in dir.children
        assert isinstance(dir.children["file.txt"], VirtualFile)
        assert dir.children["file.txt"].content == "content"

    def test_add_file_multiple(self):
        """Test adding multiple files to directory."""
        dir = VirtualDirectory("root")
        dir.add_file("file1.txt", "content1")
        dir.add_file("file2.txt", "content2")
        dir.add_file("file3.txt", "content3")
        assert len(dir.children) == 3
        assert "file1.txt" in dir.children
        assert "file2.txt" in dir.children
        assert "file3.txt" in dir.children

    def test_add_file_without_content(self):
        """Test adding file without explicit content."""
        dir = VirtualDirectory("root")
        dir.add_file("empty.txt")
        assert "empty.txt" in dir.children
        assert dir.children["empty.txt"].content == ""

    def test_add_file_overwrites_existing(self):
        """Test adding file with same name overwrites previous."""
        dir = VirtualDirectory("root")
        dir.add_file("file.txt", "original")
        dir.add_file("file.txt", "updated")
        assert dir.children["file.txt"].content == "updated"

    def test_add_dir_single(self):
        """Test adding a single subdirectory."""
        dir = VirtualDirectory("root")
        dir.add_dir("subdir")
        assert "subdir" in dir.children
        assert isinstance(dir.children["subdir"], VirtualDirectory)
        assert dir.children["subdir"].name == "subdir"

    def test_add_dir_multiple(self):
        """Test adding multiple subdirectories."""
        dir = VirtualDirectory("root")
        dir.add_dir("docs")
        dir.add_dir("src")
        dir.add_dir("tests")
        assert len(dir.children) == 3
        assert "docs" in dir.children
        assert "src" in dir.children
        assert "tests" in dir.children

    def test_add_dir_creates_empty_directory(self):
        """Test added subdirectory starts empty."""
        dir = VirtualDirectory("root")
        dir.add_dir("subdir")
        subdir = dir.children["subdir"]
        assert subdir.children == {}

    def test_list_contents_empty(self):
        """Test listing contents of empty directory."""
        dir = VirtualDirectory("root")
        contents = dir.list_contents()
        assert contents == []
        assert isinstance(contents, list)

    def test_list_contents_files_only(self):
        """Test listing contents with only files."""
        dir = VirtualDirectory("root")
        dir.add_file("file1.txt")
        dir.add_file("file2.txt")
        contents = dir.list_contents()
        assert sorted(contents) == ["file1.txt", "file2.txt"]

    def test_list_contents_dirs_only(self):
        """Test listing contents with only directories."""
        dir = VirtualDirectory("root")
        dir.add_dir("docs")
        dir.add_dir("src")
        contents = dir.list_contents()
        assert sorted(contents) == ["docs", "src"]

    def test_list_contents_mixed(self):
        """Test listing contents with mixed files and directories."""
        dir = VirtualDirectory("root")
        dir.add_file("readme.txt")
        dir.add_dir("docs")
        dir.add_file("license.txt")
        dir.add_dir("src")
        contents = dir.list_contents()
        assert len(contents) == 4
        assert sorted(contents) == ["docs", "license.txt", "readme.txt", "src"]

    def test_list_contents_returns_list(self):
        """Test list_contents always returns a list."""
        dir = VirtualDirectory("root")
        dir.add_file("file.txt")
        contents = dir.list_contents()
        assert isinstance(contents, list)

    def test_nested_directory_structure(self):
        """Test creating nested directory structures."""
        root = VirtualDirectory("root")
        root.add_dir("docs")
        docs_dir = root.children["docs"]
        docs_dir.add_file("guide.txt", "User guide")
        docs_dir.add_dir("examples")
        
        assert "docs" in root.children
        assert "guide.txt" in docs_dir.children
        assert "examples" in docs_dir.children

    def test_deep_nesting(self):
        """Test deeply nested directory structure."""
        root = VirtualDirectory("root")
        root.add_dir("level1")
        level1 = root.children["level1"]
        level1.add_dir("level2")
        level2 = level1.children["level2"]
        level2.add_dir("level3")
        level3 = level2.children["level3"]
        level3.add_file("deep.txt", "Deeply nested file")
        
        assert level3.children["deep.txt"].content == "Deeply nested file"


class TestVirtualFileSystemIntegration:
    """Integration tests for VirtualDirectory and VirtualFile."""

    def test_realistic_filesystem_structure(self):
        """Test creating a realistic filesystem structure."""
        root = VirtualDirectory("root")
        
        # Create docs directory with files
        root.add_dir("docs")
        docs = root.children["docs"]
        docs.add_file("readme.md", "# Documentation")
        docs.add_file("guide.md", "## User Guide")
        
        # Create src directory
        root.add_dir("src")
        src = root.children["src"]
        src.add_file("main.py", "print('Hello')")
        
        # Add root level files
        root.add_file("README.txt", "PolyOS Documentation")
        root.add_file("LICENSE.txt", "MIT License")
        
        # Verify structure
        assert "docs" in root.children
        assert "src" in root.children
        assert len(root.list_contents()) == 4
        assert len(docs.list_contents()) == 2
        assert len(src.list_contents()) == 1

    def test_filesystem_as_described_in_main(self):
        """Test filesystem matching the example from __main__."""
        root = VirtualDirectory("root")
        root.add_dir("docs")
        root.add_file("readme.txt", "This is PolyOS virtual fs")
        
        contents = root.list_contents()
        assert len(contents) == 2
        assert "docs" in contents
        assert "readme.txt" in contents

    def test_directory_independence(self):
        """Test that multiple directories don't share state."""
        dir1 = VirtualDirectory("dir1")
        dir2 = VirtualDirectory("dir2")
        
        dir1.add_file("file.txt", "content1")
        dir2.add_file("file.txt", "content2")
        
        assert dir1.children["file.txt"].content == "content1"
        assert dir2.children["file.txt"].content == "content2"
