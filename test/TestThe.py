import sys

sys.path.append('code')

from cli import *
from contextlib import redirect_stdout

# Test without flags
def test_cli1():
	with redirect_stdout(None):
		return Config().cli([]) == {'eg': 'nothing', 'dump': False, 'file': 'data/auto93.csv', 'help': False, 'nums': 512, 'seed': 10019, 'seperator': ','}

# Test with all flags
def test_cli2():
	with redirect_stdout(None):
		return Config().cli(['-h', '-n', '100', '-s', '100', '-f', 'data/fake.txt', '-d', '-e', 'test', '-S', ':']) == {'eg': 'test', 'dump': True, 'file': 'data/fake.txt', 'help': True, 'nums': 100, 'seed': 100, 'seperator': ':'}

# Test with long flags
def test_cli3():
	with redirect_stdout(None):
		return Config().cli(['--help', '--nums', '100', '--seed', '100', '--file', 'data/fake.txt', '--dump', '--eg', 'test', '--seperator', ':']) == {'eg': 'test', 'dump': True, 'file': 'data/fake.txt', 'help': True, 'nums': 100, 'seed': 100, 'seperator': ':'}

# Test with mixed flags
def test_cli4():
	with redirect_stdout(None):
		return Config().cli(['-h', '--nums', '100', '-s', '100', '--file', 'data/fake.txt', '-d', '--eg', 'test', '-S', ':']) == {'eg': 'test', 'dump': True, 'file': 'data/fake.txt', 'help': True, 'nums': 100, 'seed': 100, 'seperator': ':'}

# Test with invalid flags (-x and --notreal do not exist). They should be ignored
def test_cli5():
	with redirect_stdout(None):
		return Config().cli(['-x', '--notreal', '--nums', '100', '-s', '100', '--file', 'data/fake.txt', '-d', '--eg', 'test', '-S', ':']) == {'eg': 'test', 'dump': True, 'file': 'data/fake.txt', 'help': False, 'nums': 100, 'seed': 100, 'seperator': ':'}

tests = [test_cli1, test_cli2, test_cli3, test_cli4, test_cli5]
