import re
import sys

help='''
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e --eg start-up example = nothing
 -d --dump on test failure, exit with stack dump = false
 -f --file file with csv data = ../data/auto93.csv
 -h --help show help = false
 -n --nums number of nums to keep = 512
 -s --seed random number seed = 10019
 -S --seperator feild seperator = ,'''

class config:
    def __init__(self, help):
        self.the = {}
        for k, x in re.findall('\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
            self.the[k] = self.coerce(x)
#use command in help message to set key and value for the variable
    def coerce(self, s):
  #Processing string into boolean, otherwise just return s1
        def fun(s1):
            if s1.lower()=='true':
                return True
            if s1.lower()=='false':
                return False
            return s1
        #if s is int
        if s.isdigit():
            return int(s)
        #if s is float
        try:
            float(s)
            return float(s)
         #if s is string
        except ValueError:
            return fun(re.match("^\s*(.*?)\s*$", s).groups()[0])

    def cli(self, args):
        for slot in self.the.keys():
            v = str(self.the[slot])
        #for loop every args, and override value of the key variable with matched args input
            for x in args:
          #slot[0] is shortcut for slot, both are acceptable
                if (x=="-" + slot[0]) or (x=="--" + slot):
                    if v == 'false':
                        v = True
                    elif v == 'true':
                        v = False
                    else:
                        v = args[-1]
            #override value of the[slot] from args, but doesn't seem can handle multiple args
            self.the[slot] = self.coerce(v)
        if self.the['help']:
            print("\n" + help + "\n")
        return self.the
