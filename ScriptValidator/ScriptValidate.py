# Parser script run
# encoding: utf-8


import logging
import warnings

import constants
from ElementTree import ElementTree


def replacePseudoXml(bytes):
  """
  Replaces all SNSC3 specific pseudo-XML with valid xml for parser to process.

  :param bytes: bytearray read directly from file
  :returns: bytearray with pseudo-XML elements removed/replaced
  """
  if any(el in bytes for el in constants.LINE_ELS):
    return constants.NEWLINE

  bytes = bytes.replace(constants.END_LINE_OPEN, constants.END_LINE_CLOSED)
  bytes = bytes.replace(constants.THREE_DOTS_OPEN, constants.THREE_DOTS_CLOSED)
  bytes = bytes.replace(constants.PLAYER_NAME_OPEN, constants.PLAYER_NAME_CLOSED)
  bytes = bytes.replace(constants.PLAYER_NICKNAME_OPEN, constants.PLAYER_NICKNAME_CLOSED)
  bytes = bytes.replace(constants.HEARTH_OPEN, constants.HEARTH_CLOSED)
  bytes = bytes.replace(constants.PAW_OPEN, constants.PAW_CLOSED)

  return bytes


def readXml(file):
  """
  Reads from a file and processes it to remove SNSC3 specific pseudo-XML.

  :param file: file to read from
  :returns: bytearray representation of the file
  """
  ascii = False
  bytes = bytearray()
  bytes += constants.ROOT_OPEN
  for line in file.readlines():
    line = replacePseudoXml(line)
    bytes += line
  bytes += constants.ROOT_CLOSE
  return bytes


def elementContentToString(ascii, end_els):
  """
  Converts the content of an ascii element into a list of strings.

  :raises SyntaxError: error for incorrectly formed <ascii> content.
  """
  lines = ''
  lines += (ascii.text.strip())
  for el in end_els:
    if el.tail is not None and len(el.tail) > 0:
      lines += (el.tail)
  return lines


def validateEndlines(ascii, warn_array):
  """
  Checks <end_line> elements exist, match the number of lines, 
  and are placed at the end of each line.
  
  :param ascii: 
  :return: 
  """
  end_els = ascii.findall('end_line')
  inner_text = ''.join(ascii.itertext())
  if len(end_els) != inner_text.count('\n') - 1:
    warn_array.append('Number of <end_line> elements is incorrect!')
  for el in end_els:
    if el.tail is None or el.tail[0] != '\n':
      warn_array.append('<end_line> element not placed at end of line!')


# THIS IS WRONG
def determineSymbolLength(ascii):
  len_array = []
  len = 0
  for el in ascii:
    if el.tag in constants.SYMBOLS:
      len += constants.SYMBOL_LEN
    elif el.tag in constants.NAME_ELS:
      len += constants.NAME_EL_LEN
    else:
      len_array.append(len)
      len = 0
  return len_array


# THIS IS WRONG.
def validateLineLength(ascii, warn_array):
  end_els = ascii.findall('end_line')
  lines = elementContentToString(ascii, end_els).split('\n')
  line_symbols = determineSymbolLength(ascii)

  index = 0
  for line, symbol_len in zip(lines, line_symbols):
    if len(line.strip()) + symbol_len > constants.MAX_LINE_LENGTH:
      warn_array.append('Line is longer than ' + str(constants.MAX_LINE_LENGTH) + ' characters!')


def validateAsciiElements(tree):
  """
  Performs validation of content between <ascii> elements.
  
  :raises SyntaxError: error for incorrectly formed <ascii> content.
  """
  valid = True
  for ascii in tree.iter('ascii'):
    warn_array = []
    validateEndlines(ascii, warn_array)
    validateLineLength(ascii, warn_array)
    if len(warn_array) > 0:
      valid = False
      print(''.join(ascii.itertext()))
      for str in warn_array:
        logging.warning(str)
  return valid


def validateFile(filename):
  """
  Checks if a given file follows SNSC3 pseudo-XML.
  
  :param filename: name of the file to read from
  :raises ParseError: bubbled up from ElementTree
  """
  with open(filename, 'rb') as xml_file:
    bytes = readXml(xml_file)
    try:
      print('Validating ' + filename + '...')
      tree = ElementTree().parseBytes(bytes)
      if not validateAsciiElements(tree):
        warnings.warn(filename + ' is invalid!')
    finally:
      xml_file.close()
