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

import json
import xlrd
import xml.etree.ElementTree as etree

def read_cob_xml(filename=None):
    """ Open filename (or prompt for one) and convert the NetX text into emailable text.
    """
    if not filename:
        filename = input('Please enter the full path and filename for the Client Onboarding Field Review xls/xml sheet.\n')

    tree = etree.parse(filename)
    root = tree.getroot()
    print(root)
    

def read_cob_xl(filename=None):
    """ Open filename (or prompt for one) and convert the NetX text into emailable text.
    """
    if not filename:
        filename = input('Please enter the full path and filename for the Client Onboarding Field Review xls sheet.\n')

    workbook = xlrd.open_workbook(filename=filename)
    worksheet = workbook.sheets()
    print('worksheet={}'.format(worksheet))

        

def decodejson(filename='nm_netx_cob_data/nm_netx_cob.txt'):
    with open(filename, encoding='utf-8', mode='r') as a_file:
        a_json = json.loads(a_file.readline())
    return a_json


def encodejson():
    some_fields = {
        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - BUSINESS TYPE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - ADDRESS LINE 1 IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - CITY IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - STATE / PROVINCE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - EMPLOYMENT INFO - ADDITIONAL EMPLOYMENT INFO - EMPLOYER ADDRESS - ZIP / POSTAL CODE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - GENERAL INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - INVESTMENT KNOWLEDGE AND EXPERIENCE - INVESTMENT KNOWLEDGE - INVESTMENT KNOWLEDGE IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - RELATED TO AN EMPLOYEE OF THIS BROKER-DEALER? IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - RELATED TO AN EMPLOYEE OF ANOTHER BROKER-DEALER? IS MANDATORY': '',
        'PRIMARY ACCOUNT HOLDER - BROKER-DEALER AFFILIATIONS - MAINTAINING OTHER BROKERAGE ACCOUNTS IS MANDATORY': '',
        'PRIMARY BENEFICIARY 1 - NAME DETAILS - RELATIONSHIP IS MANDATORY': '',
        'PRIMARY BENEFICIARY 1 - NAME DETAILS - FIRST NAME IS MANDATORY': '',
        'PRIMARY BENEFICIARY 1 - NAME DETAILS - LAST NAME IS MANDATORY': '',
        'PRIMARY BENEFICIARY 1 - DATE OF BIRTH IS MANDATORY': '',
        'PRIMARY BENEFICIARY 1 - GENDER IS MANDATORY': '',
        }
    writejson(some_fields)

def writejson(fields, filename='nm_netx_cob_data/nm_netx_cob.txt'):
    with open(filename, encoding='utf-8', mode='w') as a_file:
        a_file.write(json.dumps(fields))

if __name__ == '__main__':
    #encodejson()
    #decoded_json = decodejson()
    #print(decoded_json)
    #read_cob_xl(r'C:\Users\perm7158\Documents\GitHub\nm\COBFieldReview-NS1394810 (not a real account, Roth IRA).xls')
    read_cob_xml(r'C:\Users\perm7158\Documents\GitHub\nm\COB.xls.html')
