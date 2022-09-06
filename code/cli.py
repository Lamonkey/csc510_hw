import re

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

def coerce(s):
    def fun(s1):
        if s1=='true':
            return True
        if s1=='false':
            return False
        return s1
    if s.isdigit():
        return int(s)
    try:
        float(s)
        return float(s)
    except ValueError:
        return fun(re.match("^\s*(.*?)\s*$", s).groups()[0])

the = {}
for k, x in re.findall('\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
    the[k] = coerce(x)
print(the)
for i in the.keys():
    print(i)
    print(the[i])

def cli(t, args):
    for slot in t.keys():
        v = str(t[slot])
        for x in args:
            if (x=="-" + slot[0]) or (x=="--" + slot):
                if v == 'false':
                    v = True
                elif v == 'true':
                    v = False
                else:
                    v = args[-1]
        t[slot] = coerce(v)
    if t['help']:
        print("\n" + help + "\n")
    return t