# Parser script run
# encoding: utf-8

"""
Current progress:

Validate tags


TODO:
Validate line length
Validate <end_line> exists for lines between <ascii> tags
more to come...
"""

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
  # if contains(bytes, constants.INFO_OPEN):
  if any(tag in bytes for tag in constants.LINE_TAGS):
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


def validateTree(tree):
  """
  TODO: implement
  this method will find all ASCII tags and ensure the contents of them have <end_line> tags.
  """
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
      validateTree(tree)
      print(filename + ' passed')
    finally:
      xml_file.close()
