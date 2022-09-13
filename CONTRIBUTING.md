# Contributing to Data Summary

### How To Contribute
This project uses a git-flow style for contributing. If you want to add a feature, feel free to create a new branch off of development and work on your changes there. When your feature is complete, submit a pull request to development where it can be integrated and tested. If the build is successful, it will eventually be merged into main.

### How To Raise Issues and Bugs
Use GitHub Issues to report bugs and other issues, using appropriate tags. Be sure that bug reports are clear and reproducible, so other developers can replicate the bugs and try to work on solutions. Just like adding features, if you want to fix a bug yourself, just pull off a branch then submit a pull request back into development. Once the issue is resolved in main, the issue will be closed.

### Development Standards
We are working in python in a command-line application. Best practices should be used whenever appropriate, and ensure to stay within the style guidelines already in place. These include capitalization for classes, snake case for variable naming, and capitalized files that typically contain one class.

### Review Standards
When you approve a pull request, it's important that you thoroughly vet the code for issues and errors. Be sure to check all changes and provide meaningful comments if something doesn't pass your inspection. By approving a pull request, you are equally responsible as the author for its quality, so make sure you're only letting in quality code!

### How To Get Started
Follow the steps outlined in INSTALL.md and make sure to also look at README.md and CITATION.md. This will guide you on how to set up your environment and get started!

### How To Run and Add Tests
py -m code.main -e ALL

will run all the test cases. If you run 

py -m code.main -e LIST

you can see every current test case. To add a test case, go to the test_csv.py file and add a function that returns true on success and false on failure. Then, immediately after declaring the function, add an entry to the tests dictionary with a name that can be used to call your specific function from the command line. 