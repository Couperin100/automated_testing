"""Common paths file.

A single location to store path constants related to the project so that
anywhere you need to get a path to a particular directory in the project you
can import it from here."""

from os import environ, path

ROOT = environ['VIRTUAL_ENV']
CONFIG_DIR = path.join(ROOT, 'config')
ENVS = path.join(CONFIG_DIR, 'envs.yaml')
RESULTS_DIR = path.join(ROOT, 'results')
EXPECTED = path.join(CONFIG_DIR, 'expected-text')

FULL_REPORT = path.join(RESULTS_DIR, 'report.html')

