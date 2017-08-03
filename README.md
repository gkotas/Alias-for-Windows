# Alias for Windows
This is my implementation to mimic bash's built-in [alias](https://ss64.com/bash/alias.html) command.
The syntax is meant to be as similar to the built-in command as possible. Additional arguments will work as intended.
See the Known Issues section for more details.

### Installation
1. Clone this repo to a directory, i.e C:\Aliases
2. Add that directory to the PATH
3. That's it!

### Examples
Adding `ls` instead of `dir`:
```
alias ls=dir
```

Opening Notepad++ with `npp`:
```
alias npp=start \"\" /B \"C:\Program Files (x86)\Notepad++\notepad++.exe\"
```
Adding `start "" /B` before the executable detaches it from the command prompt.
*Note the use of backslashes to escape the quotes*

### Known Issues
1. Quotes need to be escaped, like in the Notepad++ example.
2. Aliases with the same name as Internal Commands (`cd`, `mkdir`, etc.) have to be called like `cd.cmd`.