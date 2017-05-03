import glob
import unittest
from ScriptValidate import validateFile
from ElementTree import ParseError

class TestScriptValidate(unittest.TestCase):

  def testValidateBasicFile(self):
    file = glob.glob('./test/base.xml')
    validateFile(file[0])

  def testMisspelledLineTagRaisesError(self):
    with self.assertRaises(ParseError) as cm:
      file = glob.glob('./test/misspelledLineTag.xml')
      validateFile(file[0])
      
  def testMisspelledSymbolRaisesError(self):
    with self.assertRaises(ParseError) as cm:
      file = glob.glob('./test/misspelledSymbol.xml')
      validateFile(file[0])

  def testAsciiWithoutEndlineRaisesError(self):
    with self.assertRaises(ParseError) as cm:
      file = glob.glob('./test/asciiWithoutEndline.xml')
      validateFile(file[0])

if __name__ == '__main__':
    unittest.main()