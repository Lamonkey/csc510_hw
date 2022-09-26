import re
import sys

help='''
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e --eg start-up example = nothing
 -d --dump on test failure, exit with stack dump = false
 -f --file file with csv data = data/auto93.csv
 -h --help show help = false
 -n --nums number of nums to keep = 512
 -s --seed random number seed = 10019
 -S --seperator feild seperator = ,'''

class Config:
    """Generates and stores mappings parsed from command line."""
    def __init__(self):
        """Initialize mapping structure, parsing help structure."""
        self.the = {}  # Initialize 'the' to map command line arguments to their associated value
        # For each line in the given help statement, build a new mapping in 'the'
        for k, x in re.findall('\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
            self.the[k] = self.coerce(x)

    def coerce(self, s):
        '''
        This function processes a string that needs to be converted to either a boolean, int, float, or remain a string

         - s: This parameter is the string that must be processed and refers to the output mapping in 'the'

        returns: The converted string
        '''
        def fun(s1):
            # If the lowercase value of the given string is 'true' or 'false', return the associated boolean value
            if s1.lower()=='true':
                return True
            if s1.lower()=='false':
                return False
            # Otherwise return the original string
            return s1
        if s.isdigit(): # If s can be converted to an int, return the int of the string
            return int(s)
        try: # Try to convert the string to a float and return the float value
            float(s)
            return float(s)
        except ValueError: # If the string cannot be converted to a float then run regex to return string
            return fun(re.match("^\s*(.*?)\s*$", s).groups()[0])

    def cli(self, args):

        '''
        This function processes the command line arguments and updates the mappings in 'the'

         - args: The list of arguments normally in the example format "-h -n 100"

        returns: The updated 'the' dictionary
        '''
        for slot in self.the.keys(): # For each mapping in fun
            v = str(self.the[slot]) # Convert the output mapping to a string
            for i, x in enumerate(args): # For each argument given
                # If the argument contains '-' and is followed by the first letter of one of 'the' keys,
                # or if it contains '--' and is followed by the full key name
                if (x=="-" + ('S' if slot == 'seperator' else slot[0])) or (x=="--" + slot): 
                    # Flip string version of booleans
                    if v.lower() == 'false':
                        v = 'true'
                    elif v.lower() == 'true':
                        v = 'false'
                    # If not a boolean then just grab string
                    elif i+1 < len(args):
                        v = args[i+1]
            # Pass the argument to the coerce function to be processed
            self.the[slot] = self.coerce(v)
        # If the help mapping is true then print the help statement
        if self.the['help']:
            print("\n" + help + "\n")
        # Return the updated 'the'

        return self.the

    def the(self):
        return self.the