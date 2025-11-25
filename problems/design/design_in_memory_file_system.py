# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.

# List<String> ls(String path)

# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.

# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. 
# If the middle directories in the path do not exist, you should create them as well.

# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.

# String readContentFromFile(String filePath) Returns the content in the file at filePath.

# -----------------------------


# { file: "content", directory: { file: "content" } }

from typing import List

class FileSystem:
    def __init__(self):
        """
        Initializes the file system.
        
        Pseudocode:
        1. Create a root dictionary to represent the '/' directory.
        """
        self.root = {}

    def _is_dir(self, node) -> bool:
        """
        Checks if a node is a directory.
        
        Pseudocode:
        1. Return true if the node is a dictionary, false otherwise.
        """
        return isinstance(node, dict)
    
    def _is_file(self, node) -> bool:
        """
        Checks if a node is a file.
        
        Pseudocode:
        1. Return true if the node is a string, false otherwise.
        """
        return isinstance(node, str)
    
    def ls(self, path: str) -> List[str]:
        """
        Lists the contents of a path.
        
        Pseudocode:
        1. Start at the root node.
        2. Split the path into components.
        3. If path is root ('/'), return sorted keys of the root.
        4. Otherwise, navigate through components to the target node.
        5. If the target node is a file, return its name in a list.
        6. If the target node is a directory, return a sorted list of its contents.
        """
        node = self.root
        components = path.split('/')

        # Handle root path separately
        if path == '/':
            return sorted(node.keys())

        # Navigate to the target node
        # components[1:] skips the initial empty string from the split
        for component in components[1:]:
            node = node[component]
        
        # Check if the final node is a file or directory
        if self._is_file(node):
            # If it's a file, return its name (the last component of the path)
            return [components[-1]]
        else: # It's a directory
            return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        """
        Creates a directory at the given path, including intermediate directories.
        
        Pseudocode:
        1. Start at the root node.
        2. Split the path into components.
        3. For each component in the path:
           a. Get the directory. If it doesn't exist, create it as an empty dict.
           b. Move to the next directory in the path.
        """
        node = self.root
        components = path.split('/')

        # Navigate and create directories as needed
        # components[1:] skips the initial empty string from the split
        for component in components[1:]:
            node = node.setdefault(component, {})
    
    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        Adds content to a file, creating it if it doesn't exist.
        
        Pseudocode:
        1. Start at the root node.
        2. Split the file path into components.
        3. Navigate to the parent directory, creating intermediate dirs if needed.
        4. Get the filename from the last component.
        5. Check if a directory already exists at the file's location; if so, stop.
        6. Get the file's existing content (or an empty string if new).
        7. Append the new content and update the file.
        """
        node = self.root
        components = filePath.split('/')

        # Navigate to the parent directory, creating dirs as needed
        # components[1:-1] goes up to the parent directory
        for component in components[1:-1]:
            node = node.setdefault(component, {})
        
        filename = components[-1]

        # Defensive check: do not allow overwriting a directory with a file.
        if filename in node and self._is_dir(node[filename]):
            return
        
        # Get existing content or an empty string if the file is new, then append.
        node[filename] = node.get(filename, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        """
        Reads the content from a file.
        
        Pseudocode:
        1. Start at the root node.
        2. Split the file path into components.
        3. Navigate through the components to the target node.
        4. If the target node is a file (a string), return its content.
        5. Otherwise, return an empty string.
        """
        node = self.root
        components = filePath.split('/')

        # Navigate to the target file node
        for component in components[1:]:
            node = node[component]
        
        if self._is_file(node):
            return node
        return "" # Should not be reached with valid inputs
    