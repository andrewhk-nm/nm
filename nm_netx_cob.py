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



import json
##import xlrd
##import xml.etree.ElementTree as etree
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    fields = dict()
    
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        print("Encountered some data  :", data)
        try:
            replacement_data = self.fields[data]
        except(KeyError):
            replacement_data = input('"{}" does not have a replacement set.\n\nHow would you like this field to read instead? '.format(data))
            self.fields[data] = replacement_data
        
        print("With Replacement       :", replacement_data)

class Cob2Human():
    """ Builds a dictionary to replace the gross COB text with human readable requests.
    """

    fields = dict()

    def decodejson(self, filename='nm_netx_cob_data/nm_netx_cob.txt'):
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
        self.fields = self.decodejson()
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

    




        
##def encodejson():
##    some_fields = {
##        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - BUSINESS TYPE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - ADDRESS LINE 1 IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - CITY IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - STATE / PROVINCE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - ZIP / POSTAL CODE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - GENERAL INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - RELATED TO AN EMPLOYEE OF THIS BROKER-DEALER? IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - RELATED TO AN EMPLOYEE OF ANOTHER BROKER-DEALER? IS MANDATORY': '',
##        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - MAINTAINING OTHER BROKERAGE ACCOUNTS IS MANDATORY': '',
##        'PRIMARY BENEFICIARY 1 - NAME DETAILS - RELATIONSHIP IS MANDATORY': '',
##        'PRIMARY BENEFICIARY 1 - NAME DETAILS - FIRST NAME IS MANDATORY': '',
##        'PRIMARY BENEFICIARY 1 - NAME DETAILS - LAST NAME IS MANDATORY': '',
##        'PRIMARY BENEFICIARY 1 - DATE OF BIRTH IS MANDATORY': '',
##        'PRIMARY BENEFICIARY 1 - GENDER IS MANDATORY': '',
##        }
##    writejson(some_fields)

def writejson(fields, filename='nm_netx_cob_data/nm_netx_cob.txt'):
    with open(filename, encoding='utf-8', mode='w') as a_file:
        a_file.write(json.dumps(fields))

if __name__ == '__main__':
    cob2human = Cob2Human()
    print(cob2human.fields)
    parser = MyHTMLParser()
    parser.fields = cob2human.fields
    parser.feed(read_cob_file(r'C:\Users\perm7158\Documents\Repos\Python\nm\COB.xls.html'))
    # Write the updated list to file
    writejson(parser.fields)
    
