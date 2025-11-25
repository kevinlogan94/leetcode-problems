# Design Document: In-Memory File System

This document outlines the design and implementation details for the `FileSystem` class, which simulates an in-memory file system.

## 1. Core Design Philosophy

The primary goal was to create a simple, intuitive, and robust in-memory representation of a file system hierarchy. The design leverages standard Python data structures to model the relationship between directories and files in a way that is both memory-efficient and easy to understand.

The chosen approach is a **Trie-like structure using nested dictionaries**.

## 2. Data Structure

The entire file system is represented by a single root dictionary, `self.root`. This structure was chosen for its natural mapping to a file system's hierarchical nature.

*   **Directories are represented by Dictionaries (`dict`)**: A directory is a container. A Python dictionary serves this purpose perfectly, where its keys are the names of the files and subdirectories it contains.
*   **Files are represented by Strings (`str`)**: A file is a leaf node in our hierarchy that contains content. A Python string is used to store this content directly.

### Example Structure:

A file system with a directory `/a` containing a file `b.txt` would look like this in memory:

```python
{
    "a": {
        "b.txt": "content of file"
    }
}
```

To differentiate between files and directories, we rely on Python's `isinstance()` type checking, which is wrapped in the helper methods `_is_file()` and `_is_dir()`.

## 3. Path Traversal

A common utility needed by all methods is the ability to navigate a given path (e.g., `/a/b/c.txt`). This is handled consistently:

1.  The path string is split by the `/` delimiter using `path.split('/')`.
2.  This results in a list of path components (e.g., `['', 'a', 'b', 'c.txt']`). The initial empty string is always ignored by starting loops or slices at index `1`.
3.  The code then iterates through these components, descending into the nested dictionary structure from the `self.root`.

## 4. Method-by-Method Design Decisions

### `ls(path)`

*   **Goal**: List contents of a directory or return a file's name.
*   **Logic**:
    1.  Navigate to the target node specified by `path`.
    2.  Use `_is_file()` to check the type of the node.
    3.  If it's a file (`str`), return its name (the last component of the path).
    4.  If it's a directory (`dict`), return a **lexicographically sorted** list of its keys using `sorted(node.keys())`.

### `mkdir(path)`

*   **Goal**: Create a directory, including any necessary parent directories.
*   **Logic**: The key to this method's elegance is `dict.setdefault(key, {})`.
    1.  As we traverse the path components, `node.setdefault(component, {})` attempts to get the next directory.
    2.  If the directory doesn't exist, `setdefault` creates it as an empty dictionary (`{}`) and returns it.
    3.  If it already exists, `setdefault` simply returns the existing directory.
    4.  This allows us to create the entire path in a single, clean loop.

### `addContentToFile(filePath, content)`

*   **Goal**: Create or append content to a file.
*   **Logic**:
    1.  **Navigate to Parent**: The loop traverses `components[1:-1]`, which includes all path components *except* the filename itself. This correctly positions `node` at the parent directory.
    2.  **Create/Append**: The line `node[filename] = node.get(filename, "") + content` is the core of the operation.
        *   `node.get(filename, "")` retrieves the existing file content. If the file is new, it returns a default empty string `""`.
        *   The new `content` is then appended, and the result is stored. This handles both creation and appending in one step.
    3.  **Defensive Check**: A check `if filename in node and self._is_dir(node[filename]):` is included to prevent accidentally overwriting an existing directory with file content.

### `readContentFromFile(filePath)`

*   **Goal**: Return the full content of a file.
*   **Logic**: This is the most straightforward method.
    1.  Navigate the full path to the target node.
    2.  The final `node` in this case is the file's content string itself.
    3.  Return the `node`.

## 5. Complexity Analysis

Let `L` be the length of the input path string and `K` be the number of items in a directory being listed.

*   **`ls`**: `O(L + K log K)`. `O(L)` for path traversal and `O(K log K)` for sorting the directory contents.
*   **`mkdir`**: `O(L)`. Traverses the path once.
*   **`addContentToFile`**: `O(L + M)`, where `M` is the length of the content being added. `O(L)` for traversal and `O(M)` for string concatenation.
*   **`readContentFromFile`**: `O(L)`. Traverses the path once.
*   **Space Complexity**: `O(Total size of all paths and file contents stored)`.

This design is considered optimal for the problem constraints, providing efficient and readable implementations for all required file system operations.