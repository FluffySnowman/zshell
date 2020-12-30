# zShell

A simple shell built in python

### Installation

```bash
git clone https://github.com/FluffySnowman/zshell.git

cd zshell
```

### Executing

Run zShell.py file with python 3 like so:-

```bash
python3 zShell.py
```

### How to use

To run a command using zShell, you need to use the text box provided at the top left of the application window.

Type in the command you want to execute and then either click the execute button or press the return/enter key on your keyboard.

The output of the respective command will be displayed in a text box below the input box.

# Complications

- Some commands that require an interrupt to stop (such as 'ping') may not work correctly. The window and the execute button may hang or be disfunctional when this happens.
- Each command is redireced back to the zshell directory. using 'cd ..' or 'cd' to any path will not work. BYPASS:- To bypass this you will have to run 'cd /your/path && command'. Make sure to add '&&'. Use it as many times as you want to stack commands.