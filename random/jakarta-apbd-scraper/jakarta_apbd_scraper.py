import urllib2
import sys

# Class of both 'Rekening Belanja Tidak langsung' and 'Program Belanja Langsung' since I am so lazy

class RekeningBelanjaTidakLangsung(object):
    
    def __init__(self):
        self.year = -1
        self.name = 'NA'
        self.SKPD = 'NA'
        self.dpa  = -1

    def test_string(self):
        print '%d %s %s %d' % (
          self.year, 
          self.name, 
          self.SKPD, 
          self.dpa)

class ProgramBelanjaLangsung(object):

    def __init__(self):
        self.year       = -1
        self.kodeUrusan = 'NA'
        self.urusan     = 'NA'
        self.skpdUkpd   = 'NA'
        self.program    = 'NA'
        self.kegiatan   = 'NA'
        self.dpa        = -1

    def test_string(self):
        print '%d %s %s %s %s %s %d' % (
          self.year, 
          self.kodeUrusan, 
          self.urusan,
          self.skpdUkpd,
          self.program,
          self.kegiatan,
          self.dpa)

def get_page(url):
    """return html string of a page given its URL. Return 'error' in case of any slip."""
    try:
        usock = urllib2.urlopen(url)
        page = usock.read()
        usock.close()
        return page
    except urllib2.HTTPError, e:
        return 'get_page() error: %s' % str(e.code)  
    except urllib2.URLError, e:
        return 'get_page() error: %s' % str(e.args) 
    except:
        return 'get_page() error'#doh!
          
def get_seed_url(belanjaLangsung=True):
    """returns url that points to the start of the information tree"""
    # only check one year for now
    
    # apbd is divided into belanja langsung and belanja tidak langsung
    if (belanjaLangsung):
        seed = "http://www.jakarta.go.id/web/apbd/browse/2013"
    else: 
        seed = "http://www.jakarta.go.id/web/apbd_tl"
    return seed


def grab_skpd_table_from_rekening_belanja_tidak_langsung_page(url):
    """given the page URL, return the portion of the page that code table containing skpd information"""

    # download all the html code from the seed page which is annual_belanja_tidak_langsung_page
    # this one uses only one year, so not so complex
    # ps: use http://www.jakarta.go.id/web/apbd_tl for url
    
    page = get_page(url)
    
    # mark the start of SKPD table
    start_skpd_table = page.find('<table border ="1"><tr bgcolor="#CCFF00"><th align="center"><strong>Nama SKPD</strong></th><th align="center"><strong>Jumlah Kode Rekening</strong></th><th align="center"><strong>Nilai (Rp)</strong></th><th align="center"><strong>Nilai (%)</strong></th></tr>')
    if start_skpd_table == -1: 
        return "error: none"
    
    start_quote = page.find('<tr><td><a', start_skpd_table)
    end_quote = page.find('<tr><th colspan="2">', start_quote+1) # hack: since we are going to omit the last row
    skpd_table = page[start_quote:end_quote]
    
    return skpd_table
    
def grab_one_row_skpd(raw_info, start_of_next_row):
    """given skpd table, return the url of the skpd, its name and start_start_row"""
    
    start_start_row     = raw_info.find('<tr', start_of_next_row) #since every row starts with <tr
    if start_start_row == -1:
        return 'NA', 'NA', start_start_row
    else:
        # all the messiness starts here 
        end_start_row       = raw_info.find('>', start_start_row+1)
        
        # get the url
        # trying to find <td><a href=
        start_skpd_url = raw_info.find('<td><a href=', end_start_row) #lazy
        start_skpd_url = raw_info.find('=', start_skpd_url) 
        end_skpd_url   = raw_info.find('>', start_skpd_url+1)
        skpd_url = raw_info[start_skpd_url+2:end_skpd_url-1] #quick hack to omit " from the url
        
        # get the name
        start_skpd_name = raw_info.find('>', end_skpd_url) #no need to +1
        end_skpd_name   = raw_info.find('</a>', start_skpd_name+1) 
        skpd_name       = raw_info[start_skpd_name+1:end_skpd_name]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_skpd_name+1) #lazy
    
    return skpd_name, skpd_url, end_of_row
    
    
def grab_rekening_table_from_rekening_belanja_tidak_langsung_page(url):
    """given the page URL, return the portion of the page that code table containing rekening information """
    
    page = get_page(url)
    
    # mark the start of rekening table
    start_rekening_table = page.find('<table border')
    if start_rekening_table == -1: 
        return "error: none"
    
    start_quote = page.find('<tr><td valign="top">', start_rekening_table)
    end_quote = page.find('<tr><th><strong>', start_quote+1) # hack: since we are going to omit the last row
    rekening_table = page[start_quote:end_quote]
    
    return rekening_table
    
def grab_one_row_rekening(raw_info, start_of_next_row):
    """given rekening table, return the name of rekening, dpa and start_start_row"""
    
    start_start_row     = raw_info.find('<tr', start_of_next_row) #since every row starts with <tr
    if start_start_row == -1:
        return 'NA', 'NA', start_start_row
    else:
        # all the messiness starts here 
        end_start_row       = raw_info.find('>', start_start_row+1)
        
        # get the name
        start_rekening_name = raw_info.find('<td valign="top">', end_start_row) #lazy
        start_rekening_name = raw_info.find('>', start_rekening_name) 
        end_rekening_name   = raw_info.find('</td>', start_rekening_name+1)
        rekening_name = raw_info[start_rekening_name+1:end_rekening_name]
        
        # get the dpa
        start_rekening_dpa = raw_info.find('<td align="right"', end_rekening_name) #lazy
        start_rekening_dpa = raw_info.find('>', start_rekening_dpa) #lazy
        end_rekening_dpa   = raw_info.find('</td>', start_rekening_dpa+1) 
        rekening_dpa       = raw_info[start_rekening_dpa+1:end_rekening_dpa]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_rekening_dpa+1) #lazy
    
    return rekening_name, rekening_dpa, end_of_row
    
    
def parse_apbd_belanja_tidak_langsung(raw_info): 
    """parse the raw skpd table into something that can be processed easily"""

    rbtls = {} 
    
    start_start_row     = 0
    
    while start_start_row != -1:
        # get name and url from one row of skpd table
        skpd_name, skpd_url, start_start_row = grab_one_row_skpd(raw_info, start_start_row)   
        print 'SKPD %s %s (%d)' % (skpd_name, skpd_url, start_start_row) #testing
        
        # use the url to go to RekeningBelanjaTidakLangsung page
        # grab the table that contains rekening
        skpd_rekening_raw_info = grab_rekening_table_from_rekening_belanja_tidak_langsung_page(skpd_url)
        
        # grab the nama rekening and dpa rekening
        rekening_start_start_row = 0
        while rekening_start_start_row != -1:
          rekening_name, rekening_dpa, rekening_start_start_row = grab_one_row_rekening(skpd_rekening_raw_info, rekening_start_start_row)
          print '---- REKENING %s %s (%d)' % (rekening_name, rekening_dpa, rekening_start_start_row) #testing
          
          # save into array of RekeningBelanjaTidakLangsung
          if (start_start_row != -1 and rekening_start_start_row != -1):
              temp_rekening       = RekeningBelanjaTidakLangsung()
              temp_rekening.year  = 2013 #hardcoded for now
              temp_rekening.name  = rekening_name
              temp_rekening.SKPD  = skpd_name
              temp_rekening.dpa   = rekening_dpa
              
              # use year-skpd_name-rekening_name as 'key' # dammit so inefficient
              temp_key = str(temp_rekening.year) + '-' + temp_rekening.SKPD.replace(" ","") + '-' + temp_rekening.name.replace(" ","")
              rbtls[temp_key] = temp_rekening
          else:
              break
    
    # return an array of RekeningBelanjaTidakLangsung
    return rbtls
    
skpd_btl_main_page_raw_info = grab_skpd_table_from_rekening_belanja_tidak_langsung_page('http://www.jakarta.go.id/web/apbd_tl')

result_list = parse_apbd_belanja_tidak_langsung(skpd_btl_main_page_raw_info)

from pprint import pprint
pprint(result_list)