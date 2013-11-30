To get started, copy this repository locally, and then follow these steps.

1.  Add the folder of original files and an empty folder to store the renamed files. If necessary, change `PATH` and `RENAMED_PATH` in `rename.py` to match your actual folder names.

2. Create a python virtualenv (optional, but recommended -- requires [virtualenv and virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)):

  `mkvirtualenv dpl`

  Or, use the virtualenv if it's already been created:

  `workon dpl`

3. Install the requirements:

  `pip install -r requirements.txt`

4. Run the script:

  `python rename.py`
