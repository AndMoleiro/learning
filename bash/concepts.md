## Executing the script

### Set the interperter
At the begining of the file, add  
`!#/bin/bash`  
This will make sure the script uses bash as its interperter and is commonly called "Shebang"


### Set permissions
After creating the file, run:  
- `$chmod {permissions} {script.sh}`  

to grant the script the required permissions to execute. For example:  
- `$chmod 755 script.sh`  

## Script Components

### Variables
Storage locations that have a name-value pair.
- Syntax: `VARIABLE_NAME="value"`
- To use a variable, preceed it by `$`.
    - Eg: `echo "I like the $MY_SHELL shell."`
    - Eg 2: `echo "I am ${MY_SHELL}ing on my Keyboard."`
- Assign command output to a variable. Eg:

    ```
    #!/bib/bash

    SERVER_NAME=$(hostname)
    echo "You are running this script on ${SERVER_NAME}."
    
    --

    Output -> You are running this script on linuxsvr.
    ```
 
- Variable names can contain letters, digits and underscores.
    - Valid:
        - `FIRST3LETTERS="ABC"`
        - `FIRST_THREE_LETTERS="ABC"`
        - `firstThreeLetters="ABC"`
    - Invalid:
        - `3LETTERS="ABC`
        - `first-three-letters="ABC`
        - `first@Three@Letters="ABC"`

### TESTS

- Syntax: `[ condition-to-test-for ]`
    - Eg: `[ -e /etc/passwd ]`
        - if the password exists, returns True -> Command exits with the status of 1
        - if the password doesn't exists, returns False -> Command exits with the status of 0

- Some tests that can be used in the bash shell:
    - File Operators:
        - `-d FILE` - True if file is a directory
        - `-e FILE` - True if file exists
        - `-f FILE` - True if file is a regular file
        - `-r FILE` - True if file is readable by you
        - `-s FILE` - True if file exists and is not empty
        - `-w FILE` - True if file is writable by you
        - `-x FILE` - True if file is executable by you
    - String Operators:
        - `-z STRING` - True if string is empy
        - `-n STRING` - True if string is empy
        - `STRING1 = STRING2` - True if the strings are equal
        - `STRING1 != STRING2` - True if the strings are not equal
    - Arithmetic operators:
        - `arg1 -eq arg2` - True if arg1 is equal to arg 2
        - `arg1 -ne arg2` - True if arg1 is not equal to arg 2
        - `arg1 -lt arg2` - True if arg1 is less than to arg 2
        - `arg1 -le arg2` - True if arg1 is less than or equal to arg 2
        - `arg1 -gt arg2` - True if arg1 is greather than to arg 2
        - `arg1 -ge arg2` - True if arg1 is greather than or equal to arg 2

### If statement

- Syntax:  
```
if [ condition-is-true ]
then
    command 1
    command 2
    command N
elif [ condition-is-true ]
then 
    command 3
else
    command 4
fi
```

### For loop


