# use this to run the stuff. comment it out for now as we are still testing. later we'll run it against the actual folders n shit.

import sys
import glob
import argparse
from ElementTree import ParseError
from ScriptValidate import validateFile

parser = argparse.ArgumentParser(description='Validate a SNSC3 script files.')
parser.add_argument('folders', type=str, nargs='+', help='Name of double-quote enclosed folder(s) containing XML files to validate.')
args=parser.parse_args()


num_files = 0
for folder in args.folders:
  for file in glob.glob('./{}/*.xml'.format(folder)):
    try:
      validateFile(file)
    except:
      continue