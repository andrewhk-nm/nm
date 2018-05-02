""" This may just need to be a text file not a py file.
The purpose is to collect the NetX360 Client Onboarding (COB)
Fields that need review. The Excel output is terrible, so this would
translate it. Probably in a dictionary structure.
"""
# TODO: read in the list of required field.
#       look up answers I already know (cache)
#       ask for the ones I don't, and save the answers to the cache
#       json sounds right for that.
#       the xls file that gets spit out of NetX actually looks like an html/xml file.
#           I'm going to try the xml package instead of xlrd
#       etree complains that the file isn't well formed. It indicates line 1column 198, which ends with 'x:str'
# TODO: 2018-04-20 1p
#       Parsing works.
#       Replacement works.
#       Requesting new verbiage works.
#       TODO: Save the new verbiage.
#       TODO: Make sure the format makes sense. I have two classes right now, is that the right amount?
#               Or should there be just one? Or more?
# TODO: 2018-04-27 9.57a
#       Run on a file from the command line/right click > Send To
#       Clean up the interface.
#		Don't try to save Account Numbers
#		Perhaps some sort of way to put the person's name in the text? I don't want to start there though.
# Started using "Issues" on GitHub.


import json
##import xlrd
##import xml.etree.ElementTree as etree
from html.parser import HTMLParser
import sys

COB_DEFINITIONS_PATHFILENAME = 'cob_definitions/cob_definitions.txt'

class MyHTMLParser(HTMLParser):
    """ This class handles the parsing of the HTML COB contents
    """
    fields = dict()
    pretty_print = list()
    
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        """ As the HTML parser encounters data, handle it appropriately
        """
        #print("Encountered some data  :", data)

        # Handle exceptional data
        # "COB Field Review - #########" contains the account number. I don't think I want this, even obscured...
        if data[0:16] == 'COB Field Review':
            # Just exit and add nothing to the list.
            return
        # Skip blanks
        if data.strip() == '':
            # Just exit and add nothing to the list.
            return

        # Try getting the replacement field from the list.
        # If it doesn't exist, prompt for new replacement text.
        try:
            replacement_data = self.fields[data]
        except(KeyError):
            replacement_data = input('\n"{}" does not have a replacement set.\n\nHow would you like this field to read instead? '.format(data))
            self.fields[data] = replacement_data
        
        #print("With Replacement       :", replacement_data)
        # add the replacement data to a list for later printing
        self.pretty_print.append(replacement_data)
        #print(replacement_data)

class Cob2Human():
    """ Builds a dictionary to replace the gross COB text with human readable requests.
    """

    fields = dict()

    def _decodejson(self, filename=COB_DEFINITIONS_PATHFILENAME):
        """ Read from the external replacement definitions file, and
            bring it into the local variable.
        """
        #print(filename)
        try:
            # I don't think the rest of the code should be in the try block...
            with open(filename, encoding='utf-8', mode='r') as a_file:
                a_json = json.loads(a_file.readline())
            return a_json
        except(FileNotFoundError):
            print('"{}" not found. Skipping import.'.format(filename))
            # Return an empty dictionary if no definition file is found.
            return dict()
    
    def __init__(self):
        # Import the current json list of replacements, if it exists
        self.fields = self._decodejson()
        #print(self.fields)
        
  
def read_cob_file(filename=None):
    """ Open filename (or prompt for one) and return a string of the file contents.
    """
    if not filename:
        filename = input('Please enter the full path and filename for the Client Onboarding Field Review xls/xml/html sheet.\n')
    with open(filename, encoding='utf-8') as a_file:
        whole_file = ''
        for a_line in a_file:
            whole_file += a_line
        return whole_file


def writejson(fields, filename=COB_DEFINITIONS_PATHFILENAME):
    """ Write the replacement text to file for reuse next time.
    """
    with open(filename, encoding='utf-8', mode='w') as a_file:
        a_file.write(json.dumps(fields))

if __name__ == '__main__':
    # Get the args, if any were passed
    # args = sys.argv[1]
    filename = sys.argv[1]
    
    #print('args={}'.format(args))
    #input('<enter> to continue')
    
    # Create the cob2human object. this reads the fields from the replacement definition file into a dictionary.
    cob2human = Cob2Human()
    parser = MyHTMLParser()
    parser.fields = cob2human.fields
    #parser.feed(read_cob_file(r'C:\Users\perm7158\Documents\Repos\Python\nm\COB.xls.html'))
    # Parse the list into Pretty Print format
    parser.feed(read_cob_file(filename))
    # Write the updated list to file
    writejson(parser.fields)
    # Print the list
    input('Parsing and conversions complete. Press <ENTER> to print the list.')
    for item in parser.pretty_print:
        print(item)
    # Pause before quitting
    input('\nDone Pretty Printing. <ENTER> to exit.')
