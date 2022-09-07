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

    def coerce(self, s):
        def fun(s1):
            if s1.lower()=='true':
                return True
            if s1.lower()=='false':
                return False
            return s1
        if s.isdigit():
            return int(s)
        try:
            float(s)
            return float(s)
        except ValueError:
            return fun(re.match("^\s*(.*?)\s*$", s).groups()[0])

    def cli(self, args):
        for slot in self.the.keys():
            v = str(self.the[slot])
            for x in args:
                if (x=="-" + slot[0]) or (x=="--" + slot):
                    if v == 'false':
                        v = True
                    elif v == 'true':
                        v = False
                    else:
                        v = args[-1]
            self.the[slot] = self.coerce(v)
        if self.the['help']:
            print("\n" + help + "\n")
        return self.the
