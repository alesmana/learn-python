import urllib2
import sys

"""
simple crawler to get data about Jakarta APBD from public website 

how to use
    tba
    
some definition
   'grab' -> just get the string
   'parse'-> magically put relevant values into correct variables / objects

"""

#
# Class of both 'Rekening Belanja Tidak langsung' and 'Program Belanja Langsung' since I am so lazy
#
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
#
# common functions
#
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

#  
# functions required for informasi belanja langsung
#
def grab_urusan_table_from_informasi_belanja_langsung_page(url):
    """given the page URL, return the portion of the page that code table containing urusan information"""
    
    page = get_page(url)
    
    # mark the start of urusan table
    start_urusan_table = page.find('<table border ="1"><tr bgcolor="#CCFF00"><th align="center"><strong>Kode</strong></th><th align="center"><strong>Nama Urusan</strong></th><th align="center"><strong>Jumlah SKPD / UKPD</strong></th><th align="center"><strong>DPA (Rp)</strong></th><th align="center"><strong>DPA (%)</strong></th></tr>') # obviously this is too long. fix later
    if start_urusan_table == -1:
        return "error: urusan table is not found"
    
    start_quote   = page.find('<tr><td', start_urusan_table)
    end_quote     = page.find('<tr><th colspan="3">', start_quote+1) # hack: since we are going to omit the last row
    urusan_table  = page[start_quote:end_quote]
    
    return urusan_table
    
def parse_one_row_urusan(raw_info, start_of_next_row):
    """given urusan table and starting point, return urusan name and code"""
    
    start_start_row = raw_info.find('<tr', start_of_next_row) # since every row starts with <tr
    if start_start_row == -1:
        return 'NA', 'NA', start_start_row
    else:
        # brace yourself
        end_start_row = raw_info.find('>', start_start_row+1)
        
        # get the kode
        start_urusan_kode = raw_info.find('<td valign="top">', end_start_row) # lazy
        start_urusan_kode = raw_info.find('>', start_urusan_kode) # lazy
        end_urusan_kode   = raw_info.find('</td>', start_urusan_kode+1)
        urusan_kode       = raw_info[start_urusan_kode+1:end_urusan_kode]

        # get the name
        start_urusan_name = raw_info.find('<td valign="top">', end_urusan_kode)
        start_urusan_name = raw_info.find('>', start_urusan_name) # lazy
        end_urusan_name   = raw_info.find('</td>', start_urusan_name+1)
        urusan_name       = raw_info.[start_urusan_name+1:end_urusan_name]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_urusan_name+1) #lazy
        
    return urusan_code, urusan_name, end_of_row
        
def grab_skpdUkpd_table_from_informasi_belanja_langsung_page(url):
    """giventhe page url, return the portion of the page that code table containing skpd / ukpd information"""
    
    page = get_page(url)
    
    # mark the start of SKPD / UKPD table
    start_skpdUkpd_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th rowspan="2" align="center">Nama SKPD / UKPD</th><th rowspan="2" align="center">Kegiatan</th><th rowspan="2" align="center">DPA (Rp)</th><th colspan="2" align="center">DPA (%)</th></tr><tr bgcolor="#CCFF00"><th align="center">per Tahun</th><th align="center">per Urusan</th></tr>') # clean this up later
    if start_skpdUkpd_table = -1
        return "error: skpd / ukpd table is not found"
        
    start_quote     = page.find('<tr><td>', start_skpdUkpd_table)
    end_quote       = page.find('<tr><th colspan="2"><strong>', start_quote+1) # lazy hack since we are going to omit the last row anyway
    skpdUkpd_table = page[start_quote:end_quote]
    
    return skpdUkpd_table

def parse_one_row_skpd_ukpd(raw_info, start_of_next_row):
    """ given skpd ukpd table and starting point, return the url to corresponding kegiatan of the skpd/ukpd, its name and start row for the next cycle"""
    
    start_start_row = raw._info.find('<tr', start_of_next_row) #since every row starts with <tr
    if start_start_row == -1
        return 'NA', 'NA', start_start_row
    else:
        end_start_row = raw_info.find('>', start_start_row+1)
        
        # get kegiatan url
        # try to spot <td><a href=
        start_kegiatan_url  = raw_info.find('<td><a href=', end_start_row) 
        start_kegiatan_url  = raw_info.find('=', start_kegiatan_url)
        end_kegiatan_url    = raw_info.find('>', start_kegiatan_url+1)
        kegiatan_url        = raw_info[start_kegiatan_url+2:end_kegiatan_url-1] # quick hack to omit " from the url
        
        # get the name of SKPD / UKPD
        start_skpdUkpd_name = raw_info.find('>', end_kegiatan_url) # no need to +1
        end_skpdUkpd_name   = raw_info.find('</a>, start_skpdUkpd_name+1)
        skpdUkpd_name       = raw_info[start_skpdUkpd_name+1:end_skpdUkpd_name]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_skpdUkpd_name+1) #lazy
        
    return kegiatan_url, skpdUkpd_name, end_of_row
        
def grab_kegiatan_table_from_kegiatan_langsung_page(url):
    return "function not yet developed"
    
def parse_one_row_kegiatan(raw_info, start_of_next_row):
    return "function not yet developed"
    
#
# functions required for informasi belanja tidak langsung
#
def grab_skpd_table_from_informasi_belanja_tidak_langsung_page(url):
    """given the page URL, return the portion of the page that code table containing skpd information"""

    # download all the html code from the seed page which is annual_belanja_tidak_langsung_page
    # this one uses only one year, so not so complex
    # ps: use http://www.jakarta.go.id/web/apbd_tl for url
    
    page = get_page(url)
    
    # mark the start of SKPD table
    start_skpd_table = page.find('<table border ="1"><tr bgcolor="#CCFF00"><th align="center"><strong>Nama SKPD</strong></th><th align="center"><strong>Jumlah Kode Rekening</strong></th><th align="center"><strong>Nilai (Rp)</strong></th><th align="center"><strong>Nilai (%)</strong></th></tr>') 
    if start_skpd_table == -1: 
        return "error: skpd table is not found"
    
    start_quote = page.find('<tr><td><a', start_skpd_table)
    end_quote   = page.find('<tr><th colspan="2">', start_quote+1) # hack: since we are going to omit the last row
    skpd_table  = page[start_quote:end_quote]
    
    return skpd_table
    
def parse_one_row_skpd(raw_info, start_of_next_row):
    """given skpd table and starting point, return the url of the skpd, its name and start_start_row"""
    
    start_start_row     = raw_info.find('<tr', start_of_next_row) # since every row starts with <tr
    if start_start_row == -1:
        return 'NA', 'NA', start_start_row
    else:
        end_start_row       = raw_info.find('>', start_start_row+1)
        
        # get the skpd url
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
        return "error: rekening table is not found"
    
    start_quote     = page.find('<tr><td valign="top">', start_rekening_table)
    end_quote       = page.find('<tr><th><strong>', start_quote+1) # hack: since we are going to omit the last row
    rekening_table  = page[start_quote:end_quote]
    
    return rekening_table
    
def parse_one_row_rekening(raw_info, start_of_next_row):
    """given rekening table, return the name of rekening, dpa and start_start_row"""
    
    start_start_row     = raw_info.find('<tr', start_of_next_row) #since every row starts with <tr
    if start_start_row == -1:
        return 'NA', 'NA', start_start_row
    else:
        # all the messiness starts here 
        end_start_row       = raw_info.find('>', start_start_row+1)
        
        # get the name
        start_rekening_name = raw_info.find('<td valign="top">', end_start_row) #lazy
        start_rekening_name = raw_info.find('>', start_rekening_name) #lazy
        end_rekening_name   = raw_info.find('</td>', start_rekening_name+1)
        rekening_name       = raw_info[start_rekening_name+1:end_rekening_name]
        
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
    
    # i think some part of this can be refractored 

    # list container
    rbtls = {} 
    
    start_start_row     = 0
    
    while start_start_row != -1:
        # get name and url from one row of skpd table
        skpd_name, skpd_url, start_start_row = parse_one_row_skpd(raw_info, start_start_row)   
        print 'SKPD: %s %s (%d)' % (skpd_name, skpd_url, start_start_row) #testing
        
        # use the url to go to RekeningBelanjaTidakLangsung page
        # grab the table that contains rekening
        skpd_rekening_raw_info = grab_rekening_table_from_rekening_belanja_tidak_langsung_page(skpd_url)
        
        # grab the nama rekening and dpa rekening
        rekening_start_start_row = 0
        while rekening_start_start_row != -1:
          rekening_name, rekening_dpa, rekening_start_start_row = parse_one_row_rekening(skpd_rekening_raw_info, rekening_start_start_row)
          print '---- REKENING: %s %s (%d)' % (rekening_name, rekening_dpa, rekening_start_start_row) #testing
          
          # save into list of RekeningBelanjaTidakLangsung
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

# skpd_btl_main_page_raw_info = grab_skpd_table_from_informasi_belanja_tidak_langsung_page(get_seed(false))
# result_list = parse_apbd_belanja_tidak_langsung(skpd_btl_main_page_raw_info)

# from pprint import pprint
# pprint(result_list)