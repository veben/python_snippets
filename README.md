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
- Navigate to a Project Sub-folder:
- Execute your tests using Python's unittest module:
```sh
python -m unittest
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

## Snippets
- [ ] [Sliding Windows](sliding_windows/README.md)
- [ ] [Two Pointers](two_pointers/README.md)
- [ ] [Hare and Tortoise](hare_and_tortoise/README.md)