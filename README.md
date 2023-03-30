# Next Project Bootstrapper

Small python script that automates the setup of a new personal NextJS project. 

# Setup

This project requires Python3. In your `.bashrc` or the appropriate shell profile, add the following at the end of the file:

```
alias nextboot="python path/to/bootstrap.py"
```

You are now ready to go and execute the file!

# Arguments

```
positional arguments:
  name        Name of the project. Initializes directory and project name to parameter. Aborts if directory/project already exists.

options:
  -h, --help  show this help message and exit
```

`name` is a required argument.