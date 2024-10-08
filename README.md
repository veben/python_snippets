# Python Snippets
Welcome to Python Snippets, my collection of Python patterns and snippets

## Manage Virtual Environment & Debugger

### Installation
1. Install venv manager:
```sh
apt install python3.10-venv
```
2. Create the venv:
```sh
python3 -m venv venv_3.10.12
```

### Configuration for the Terminal
- Activate the Virtual Environment:
```sh
source venv_3.10.12/bin/activate
```
- Ensure that Python is recognized within the virtual environment:
```sh
❯ which python
/mnt/c/Users/benoit.veyriere/My Drive/docs/snippets/personal/python_snippets/venv_3.10.12/bin/python
```
- Navigate to a Project Sub-folder

#### Run the tests with **unitest**
Execute your tests using Python's unittest module:
```sh
python -m unittest
```

#### Run the tests with **pytest**
> pytest can run tests written with unittest

- Install `pytest`:
```sh
python -m pip install pytest
```
- Run the tests:
```sh
pytest
```

### Configuration for VSCode
- Open `python_snippets` in VSCode (not parent folder)
```sh
code python_snippets
```
- Configure VSCode to use the venv creating a `.vscode/settings.json` configuration file:
```plaintext
{
  "python.pythonPath": "${workspaceFolder}/venv_3.10.22/bin/python"
}
```
- Set Up the Python Debugger creating a `.vscode/launch.json` configuration file:
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
    }
  ]
}
```
- Open a test file in the editor
- Access the Debugger view by pressing `CTRL+SHIFT+d`
- Run the tests with the configured debugger by pressing `F5`

#### Troubleshooting VSCode Python Package Recognition
> Issue: VSCode Not Recognizing Newly Installed Packages

If you've installed a package via terminal, but VSCode doesn't recognize it, follow these steps to refresh your environment.

##### Option 1: Restart the Python Language Server
This method updates VSCode's Python environment:
1. Open the Command Palette: `Ctrl+Shift+P`
2. Type "Python: Restart Language Server"

##### Option 2: Reload the VSCode Window
This method refreshes the entire VSCode environment:
1. Open the Command Palette: `Ctrl+Shift+P`
2. Type and select "Developer: Reload Window"

## Snippets
1. [Sliding Windows](sliding_windows/README.md)
2. [Two Pointers](two_pointers/README.md)
3. [Hare and Tortoise](hare_and_tortoise/README.md)
4. [Merge Intervals](merge_intervals/README.md)
5. [Cyclic Sort](cyclic_sort/README.md)
6. [In-place reversal of linked list](in-place-reversal-of-linked-list/README.md)
7. [Tree BFS](tree_bfs/README.md)
8. [Tree DFS](tree_dfs/README.md)
9. [Subsets](subsets/README.md)
10. [Two Heaps](two_heaps/README.md)