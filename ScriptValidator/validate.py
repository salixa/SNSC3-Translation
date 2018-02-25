import argparse
import glob
import os

from parseXml import validateFile
from ElementTree import ParseError

parser = argparse.ArgumentParser(description='Validate SNSC3 script files.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('days', type=int, nargs='*', help='Index of day(s) to validate.', default=[])
group.add_argument('--all', action='store_true')
args = parser.parse_args()
days = args.days

if args.all:
  days = list(range(0, 12))
for day in days:
  for file in glob.glob('../Day {:02d}/*.xml'.format(day)):
    validateFile(file)
