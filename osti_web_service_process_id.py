#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Script for adding OSTI IDs to INSPIRE records after using OSTI Web Service.
"""

import os
import re
import xml.etree.ElementTree as ET
#import urllib2
from urllib2 import Request, urlopen
import PyPDF2
from PyPDF2 import PdfFileReader
#, PdfFileWriter
from StringIO import StringIO

from invenio.search_engine import perform_request_search
from invenio.bibrecord import print_rec, record_add_field
from invenio.bibformat_engine import BibFormatObject
from osti_web_service import get_url

TEST = False
#TEST = True
DOCUMENT = 'tmp_osti.out'
DIRECTORY = '/afs/cern.ch/project/inspire/TEST/hoc/osti/'

if TEST:
    DOCUMENT = 'tmp_osti_test.out'

RECIDS = []

def create_osti_id_pdf(recid, osti_id):
    """
    Places a PDF named after the OSTI id in a location that
    can be pushed to OSTI.
    If the pdf is not of an excepted paper it skips this.
    """

    try:
        [url, accepted] = get_url(recid)
        if accepted == False:
            return None
    except IndexError:
        print "No url on", recid
        return None
    except TypeError:
        print "No url on", recid
        return None
    remote_file = urlopen(Request(url)).read()
    memory_file = StringIO(remote_file)
    try:
        PdfFileReader(memory_file)
    except PyPDF2.utils.PdfReadError:
        print "PDF invalid for", recid
        return None
    except TypeError:
        print "Problem with", url
        return None
    final_pdf = DIRECTORY + str(osti_id) + ".pdf"
    final_txt = DIRECTORY + str(osti_id) + ".txt"
    if os.path.exists(final_pdf) or os.path.exists(final_txt):
        print "Already have PDF for recid=", recid, "osti_id=", osti_id
        return None
    output = open(final_pdf, 'wb')
    output.write(remote_file)
    output.close()

def find_recid(mystery_id):
    """
    Takes an ID, could be a recid or an irn, and returns a recid
    """

    if not mystery_id.isdigit():
        print "Invalid ID: " , mystery_id
        return False
    search = "001:" + mystery_id + \
             " or 970__a:SPIRES-" + mystery_id + " 037:FERMILAB*"
    result = perform_request_search(p = search, cc = 'HEP')
    if len(result) == 1:
        recid = result[0]
        if recid in RECIDS:
            return False
        else:
            RECIDS.append(recid)
            return recid
    else:
        return False

def create_xml(osti_id, inspire_id):
    """
    The function checks if the OSTI ID should be added to INSPIRE.
    If so, it builds up that information.
    """

    osti_id = str(osti_id)
    recid = str(inspire_id)
    search = "001:" + recid
    result = perform_request_search(p = search, cc = 'HEP')
    if len(result) != 1:
        print 'No such INSPIRE record', recid
        return None
    search = "001:" + recid + " 035__a:" + osti_id
    result = perform_request_search(p = search, cc = 'HEP')
    if len(result) == 1:
        return None
    search = "035__9:osti 035__a:" + str(osti_id)
    result = perform_request_search(p = search, cc = 'HEP')
    if len(result) == 1:
        for item in BibFormatObject(int(recid)).fields('035__'):
            if item.has_key('9') and item.has_key('a'):
                if item['9'] == 'OSTI' and item['a'] == osti_id:
                    print 'OSTI ID', osti_id, 'already on', result[0]
        return None
    search = "001:" + recid + " -035__9:OSTI"
    if TEST:
        print search
    result = perform_request_search(p = search, cc = 'HEP')
    if not len(result) == 1:
        print search, result
        print 'Problem with', recid, osti_id
        return False
    if TEST:
        print result
    record = {}
    record_add_field(record, '001', controlfield_value=str(recid))
    new_id  = [('a', osti_id), ('9', 'OSTI')]
    record_add_field(record, '035', '', '', subfields=new_id)
    create_osti_id_pdf(recid, osti_id)
    return print_rec(record)

    #try:
    #    create_osti_id_pdf(recid, osti_id)
    #    return print_rec(record)
    #except:
    #    print "Something wrong: " + search
    #    return False


def main():
    """
    Takes the output from an OSTI web push and appends the
    OSTI IDs to the INSPIRE records.
    """

    filename = 'tmp_' + __file__
    filename = re.sub('.py', '_append.out', filename)
    output = open(filename,'w')
    output.write('<collection>')
    tree = ET.parse(DOCUMENT)
    root = tree.getroot()
    for record in root.findall('record'):
        print record.tag
        osti_id = record.find('osti_id').text
        inspire_id = record.find('other_identifying_nos').text
        record_update = create_xml(osti_id, inspire_id)
        if record_update:
            try:
                if TEST:
                    print record_update
                else:
                    output.write(record_update)
            except:
                print 'CANNOT print record', record.attrib
    output.write('</collection>')
    output.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Exiting'

