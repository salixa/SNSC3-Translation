# Parser script run
# encoding: utf-8


import os
import sys
import constants

from ElementTree import ElementTree
from ElementTree import ParseError


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


def elementContentToStringList(ascii, end_els):
  """
  Converts the content of an ascii element into a list of strings.

  :raises SyntaxError: error for incorrectly formed <ascii> content.
  """

  lines = []
  lines.append(ascii.text.strip())
  for end_el in end_els:
    texts = end_el.tail.strip().split('\n')
    for text in texts:
      if len(text) > 0:
        lines.append(text)
  return lines


def validateAsciiElements(tree):
  """
  Performs validation of content between <ascii> elements.
  
  :raises SyntaxError: error for incorrectly formed <ascii> content.
  """

  for ascii in tree.iter('ascii'):
    end_els = ascii.findall('end_line')
    inner_text = ''.join(ascii.itertext())
    lines = elementContentToStringList(ascii, end_els)

    if len(end_els) != len(lines):
      raise SyntaxError(inner_text + '\nNumber of <end_line> elements is incorrect!')

    # TODO: add support for symbol elements (width of 2) (need to find all of these first)
    for line in lines:
      if len(line.strip()) > 30:
        raise SyntaxError(inner_text + '\nIs longer than 30 characters!')

  return


def validateFile(filename):
  """
  Checks if a given file follows SNSC3 pseudo-XML.
  
  :param filename: name of the file to read from
  :raises ParseError: bubbled up from ElementTree
  """

  with open(filename, 'rb') as xml_file:
    bytes = readXml(xml_file)
    try:
      tree = ElementTree().parseBytes(bytes)
      validateAsciiElements(tree)
      print(filename + ' passed')
    finally:
      xml_file.close()
