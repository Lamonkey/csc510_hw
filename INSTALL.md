Installation
============
These instructions assume that you are starting with a local copy of the source code tree, created by `git clone` or by unpacking a zipped/tarball copy. They also assume that Python 3.10 or greater is installed and accessible as `python`.

### Python venv
Create a virtualenv, probably in the source root directory:
```
python -m venv venv
```

Activate venv (linux/mac):
```bash
source venv/bin/activate
which python
# `which python` should now point to venv/bin/python 
```

Activate venv (Windows Powershell):
```powershell
.\venv\Scripts\Activate.ps1
# `where.exe python` should point to the venv's python binary
```

At this point, the package can be installed with `pip` as described under 'Install as developer' or 'Install as standard package' below.

Deactivate venv when finished:
```
deactivate
```

### Install as developer
To install as a developer, with the virtualenv active as described above, run:
```
pip install -r requirements.txt
```

Further instructions will be added when entry point is made available.

### Other notes
Wording based off of Github user joshuam1008 private project. Contact for more details.
