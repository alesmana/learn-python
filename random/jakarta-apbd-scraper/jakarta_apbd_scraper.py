import urllib2
import sys
import csv
import re

import os


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

class RekeningPendapatan(object):
    
    def __init__(self):
        self.year = -1
        self.name = 'NA'
        self.SKPD = 'NA'
        self.dpa  = -1

    def test_string(self):
        print '%d, %s, %s, %d' % (
          self.year, 
          self.name, 
          self.SKPD, 
          self.dpa)
          
    def return_list_header(self):
        return ['year', 'skpd', 'name', 'dpa']
          
    def return_as_list(self):
        return [self.year, self.SKPD, self.name, self.dpa]
        
class RekeningBelanjaTidakLangsung(object):
    
    def __init__(self):
        self.year = -1
        self.name = 'NA'
        self.SKPD = 'NA'
        self.dpa  = -1

    def test_string(self):
        print '%d, %s, %s, %d' % (
          self.year, 
          self.name, 
          self.SKPD, 
          self.dpa)
          
    def return_list_header(self):
        return ['year', 'skpd', 'name', 'dpa']
          
    def return_as_list(self):
        return [self.year, self.SKPD, self.name, self.dpa]

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
        print '%d, %s, %s, %s, %s, %s, %d' % (
          self.year, 
          self.kodeUrusan, 
          self.urusan,
          self.skpdUkpd,
          self.program,
          self.kegiatan,
          self.dpa)

    def return_list_header(self):
        return ['year', 'kode urusan', 'urusan', 'skpd/ukpd', 'program', 'kegiatan', 'dpa']
          
    def return_as_list(self):
        return [self.year, self.kodeUrusan, self.urusan, self.skpdUkpd, self.program, self.kegiatan, self.dpa]
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
          
def get_seed_url(apbd_year, belanjaLangsung=True):
  """returns url that points to the start of the information tree"""
  # only check one year 
  # apbd is divided into belanja langsung and belanja tidak langsung
  if (belanjaLangsung):
    seed = ''.join(['http://www.jakarta.go.id/web/apbd/browse/', str(apbd_year)])  
  else: 
    seed = "http://www.jakarta.go.id/web/apbd_tl"
  return seed
    
def clean_input(input):
  """return a cleaned input without all the extra stupid thing"""
  # remove nnumber and dot from sentence (e.g. '8. Program peningkatan sarana prasarana Kebudayaan'
  output = re.sub('([\d.]+)', '',input)
  
  # trim the output
  output = output.strip()
  
  if output:
    return output
  else: 
    return input
      
def dump_to_csv(filename, dictionary):
  """write dictionary into specified csv file (i.e. filename)
      check if csv is already exist
      if file not exist
        create new file
        add header
      else
        append to existing file
      close file
        
      note: assume user know that number of column should be the same (no checking here) 
  """
  is_file_exist = False
  
  # check if csv already exist
  try:
    with open(filename) as f:
      is_file_exist = True
  except IOError as e:
    is_file_exist = False
    
  # if not exist create a new one with proper header
  if not is_file_exist:
    f = open(filename, "wb")
    c = csv.writer(f)
    c.writerow(dictionary[dictionary.keys()[0]].return_list_header())  # not sure if there is better way
    is_file_exist = True 
    f.close()
    
  # since the file should be exist by now, just append

  f = open(filename, "ab")
  c = csv.writer(f)

  
  # just whack
  for key, value in dictionary.items():
    c.writerow(value.return_as_list())
  
  # close file
  f.close()
  
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
        urusan_name       = raw_info[start_urusan_name+1:end_urusan_name]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_urusan_name+1) #lazy
        
    return urusan_kode, urusan_name, end_of_row
        
def grab_skpdUkpd_table_from_informasi_belanja_langsung_page(url):
    """ given the page url, return the portion of the page that code table containing skpd / ukpd information"""
    
    page = get_page(url)
    
    # mark the start of SKPD / UKPD table
    start_skpdUkpd_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th rowspan="2" align="center">Nama SKPD / UKPD</th><th rowspan="2" align="center">Kegiatan</th><th rowspan="2" align="center">DPA (Rp)</th><th colspan="2" align="center">DPA (%)</th></tr><tr bgcolor="#CCFF00"><th align="center">per Tahun</th><th align="center">per Urusan</th></tr>') # clean this up later
    if start_skpdUkpd_table == -1:
        return "error: skpd / ukpd table is not found"
        
    start_quote     = page.find('<tr><td>', start_skpdUkpd_table)
    end_quote       = page.find('<tr><th colspan="2"><strong>', start_quote+1) # lazy hack since we are going to omit the last row anyway
    skpdUkpd_table  = page[start_quote:end_quote]
    
    return skpdUkpd_table

def parse_one_row_skpd_ukpd(raw_info, start_of_next_row):
    """ given skpd ukpd table and starting point, return the url to corresponding kegiatan of the skpd/ukpd, its name and start row for the next cycle"""
    
    start_start_row = raw_info.find('<tr', start_of_next_row) #since every row starts with <tr
    if start_start_row == -1:
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
        end_skpdUkpd_name   = raw_info.find('</a>', start_skpdUkpd_name+1)
        skpdUkpd_name       = raw_info[start_skpdUkpd_name+1:end_skpdUkpd_name]
        
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_skpdUkpd_name+1) #lazy
        
    return kegiatan_url, skpdUkpd_name, end_of_row
        
def grab_kegiatan_table_from_kegiatan_langsung_page(url):
  """ given the page url, return the portion of the page that code table containing program and kegiatan information """
  
  page = get_page(url)
  
  # mark the start of program and kegiatan table 
  start_kegiatan_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th rowspan="2" align="center">Program</th><th rowspan="2" align="center">Kegiatan</th><th rowspan="2" align="center">DPA (Rp)</th><th colspan="3" align="center">DPA (%)</th></tr><tr bgcolor="#CCFF00"><th align="center">per Tahun</th><th align="center">per Urusan</th><th align="center">per SKPD</th></tr>')
  if start_kegiatan_table == -1:
      return "error: program / kegiatan table is not found"
  
  start_quote     = page.find('<tr><td valign="top">', start_kegiatan_table)
  end_quote       = page.find('<tr><th colspan="2"><strong>', start_quote+1) # last row omitted
  kegiatan_table  = page[start_quote:end_quote]

  # check for pagination
  # super messy
  # check of there is 'next' link
  
  next_char = page.find('>&gt;</a>', end_quote+1)
 
  if next_char != -1:
    # get the next url
    # trying to find <a href=
    start_next_url = page.rfind('<a href=', end_quote, next_char-1) #lazy
    start_next_url = page.find('=', start_next_url) 
    end_next_url   = page.find('>', start_next_url+1)
    next_url = page[start_next_url+2:end_next_url-1] #quick hack to omit " from the url
   
    kegiatan_table = kegiatan_table + grab_kegiatan_table_from_kegiatan_langsung_page(next_url) #recursive galore
  else:
    print 'there is no next page'
      
  return kegiatan_table
    
def parse_one_row_kegiatan(raw_info, start_of_next_row):
    """ given kegiatan table and starting point, return the name of program and kegiatan and its dpa """
    
    start_start_row   = raw_info.find('<tr', start_of_next_row) # since every row starts with <tr
    if start_start_row == -1:
        return 'Na', 'NA', 'NA', start_start_row
    else:
        end_start_row = raw_info.find('>', start_start_row+1)
        
        # get the name of program
        start_program_name  = raw_info.find('<td valign="top">', end_start_row)
        start_program_name  = raw_info.find('>', start_program_name) #lazy
        end_program_name    = raw_info.find('</td>',start_program_name+1)
        program_name        = raw_info[start_program_name+1:end_program_name]

        # get the name of kegiatan
        start_kegiatan_name = raw_info.find('<td valign="top">', end_program_name)
        start_kegiatan_name = raw_info.find('>', start_kegiatan_name) #lazy
        end_kegiatan_name   = raw_info.find('</td>',start_kegiatan_name+1)
        kegiatan_name        = raw_info[start_kegiatan_name+1:end_kegiatan_name]
        
        # get dpa amount
        start_kegiatan_dpa  = raw_info.find('<td align="right" valign="top">',end_kegiatan_name)
        start_kegiatan_dpa  = raw_info.find('>', start_kegiatan_dpa) #lazy
        end_kegiatan_dpa    = raw_info.find('</td>', start_kegiatan_dpa+1)
        kegiatan_dpa        = raw_info[start_kegiatan_dpa+1:end_kegiatan_dpa]
        
        return program_name, kegiatan_name, kegiatan_dpa, end_kegiatan_dpa

def parse_apbd_belanja_langsung(apbd_year, raw_info, filename):
    """parse the raw information of apbd belanja langsung for one year"""
   
    # definitely need to be refractored
    
    # list container
    pbls = {}
    
    start_start_row = 0
    
    while start_start_row != -1:
        
        # get the code and name of urusan
        urusan_kode, urusan_name, start_start_row = parse_one_row_urusan(raw_info, start_start_row)
        print 'URUSAN: %s - %s (%d)' % (urusan_name, urusan_kode, start_start_row)
        
        # construct url to go to each urusan
        urusan_url = ''.join(['http://www.jakarta.go.id/web/apbd/category/', urusan_kode, '/', str(apbd_year)])
        
        # use the url to go to urusan belanja langsung page
        urusan_skpdUkpd_raw_info = grab_skpdUkpd_table_from_informasi_belanja_langsung_page(urusan_url)
        
        urusan_start_start_row = 0
        while urusan_start_start_row != -1:
            kegiatan_url, skpdUkpd_name, urusan_start_start_row = parse_one_row_skpd_ukpd(urusan_skpdUkpd_raw_info, urusan_start_start_row)
            print '--SKPD/UKPD: %s - %s (%d)' % (skpdUkpd_name, kegiatan_url, urusan_start_start_row)
            
            # use the url to go to kegiatan belanja langsung page
            kegiatan_raw_info = grab_kegiatan_table_from_kegiatan_langsung_page(kegiatan_url)
            
            kegiatan_start_start_row = 0
            while kegiatan_start_start_row != -1:
                program_name, kegiatan_name, kegiatan_dpa, kegiatan_start_start_row = parse_one_row_kegiatan(kegiatan_raw_info, kegiatan_start_start_row)
                print '----PROGRAM KEGIATAN DPA: %s - %s - %s (%d)' % (program_name, kegiatan_name, kegiatan_dpa, kegiatan_start_start_row)

                # save into list of RekeningBelanjaTidakLangsung
                if (kegiatan_start_start_row != -1):
                    temp_kegiatan             = ProgramBelanjaLangsung()
                    temp_kegiatan.year        = apbd_year
                    temp_kegiatan.kodeUrusan  = urusan_kode
                    temp_kegiatan.urusan      = urusan_name
                    temp_kegiatan.skpdUkpd    = skpdUkpd_name
                    temp_kegiatan.program     = clean_input(program_name)
                    temp_kegiatan.kegiatan    = clean_input(kegiatan_name)
                    temp_kegiatan.dpa         = kegiatan_dpa
                    
                    # use year-kode_urusan-skpd-program-kegiatan as 'key' # dammit so inefficient #use hash ???
                    temp_key = ''.join([str(temp_kegiatan.year), temp_kegiatan.kodeUrusan, temp_kegiatan.skpdUkpd.replace(" ",""), temp_kegiatan.program.replace(" ",""), temp_kegiatan.kegiatan.replace(" ","")])
                    pbls[temp_key] = temp_kegiatan
            # dump into CSV
            dump_to_csv(filename, pbls)
            # clear array container      
            pbls.clear() 
  
    
    
    
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
    start_rekening_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th align="center">Nama Kode Rekening</th><th align="center">DPA (Rp)</th></tr>')
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
      
def parse_apbd_belanja_tidak_langsung(raw_info, filename): 
    """ parse the entire information of apbd belanja tidak langsung for one year"""
    
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
      
      # dump into CSV
      dump_to_csv(filename, rbtls)
      # clear array container      
      rbtls.clear() # better than rbtls = {} true story
  
  
#
# functions required for informasi pendapatan pemrov dki
#
def grab_skpd_table_from_informasi_pendapatan_daerah_page(url):
  """given the page URL, return the portion of the page that code table containing skpd information of pendapatan daerah"""
  
  # actually this is the same as grab_skpd_table_from_informasi_belanja_tidak_langsung_page(url)

  # this one uses only one year, so not so complex
  # ps: use http://www.jakarta.go.id/web/apbdpt
  
  page = get_page(url)
  
  # mark the start of SKPD table
  start_skpd_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th align="center"><strong>Nama SKPD</strong></th><th align="center"><strong>Jumlah Kode Rekening</strong></th><th align="center"><strong>Nilai (Rp)</strong></th></tr>') 
  if start_skpd_table == -1: 
      return "error: skpd table is not found"
  
  start_quote = page.find('<tr><td><a', start_skpd_table)
  end_quote   = page.find('<tr><th colspan="2">', start_quote+1) # hack: since we are going to omit the last row
  skpd_table  = page[start_quote:end_quote]
  
  return skpd_table
  
def grab_rekening_table_from_informasi_pendapatan_daerah_page(url):
  """given the page URL, return the portion of the page that code table containing rekening information """
  
  # similar with grab_rekening_table_from_rekening_belanja_tidak_langsung_page(url) but with added pagination
  
  page = get_page(url)
  
  # mark the start of rekening table
  start_rekening_table = page.find('<table border ="1" width="100%"><tr bgcolor="#CCFF00"><th align="center">Nama Kode Rekening</th><th align="center">DPA (Rp)</th></tr>')
  if start_rekening_table == -1: 
      return "error: rekening table is not found"
  
  start_quote     = page.find('<tr><td valign="top">', start_rekening_table)
  end_quote       = page.find('<tr><th><strong>', start_quote+1) # hack: since we are going to omit the last row
  rekening_table  = page[start_quote:end_quote]
  
  return rekening_table
  
def parse_apbd_pendapatan_daerah(raw_info, filename):
  pass
  

 
# skpd_btl_main_page_raw_info = grab_skpd_table_from_informasi_belanja_tidak_langsung_page(get_seed_url(2013, False))
# parse_apbd_belanja_tidak_langsung(skpd_btl_main_page_raw_info, 'apbd_tidak_langsung_2013_2.csv')
#apbd_tl_result_list = parse_apbd_belanja_tidak_langsung(skpd_btl_main_page_raw_info)

#dump_to_csv('apbd_tidak_langsung_2013_2.csv', apbd_tl_result_list)

#urusan_bl_main_page_raw_info = grab_urusan_table_from_informasi_belanja_langsung_page(get_seed_url(2009, True))
#apbd_l_result_list = parse_apbd_belanja_langsung(2009, urusan_bl_main_page_raw_info)
#
#dump_to_csv('apbd_langsung_2009.csv', apbd_l_result_list)


# urusan_bl_main_page_raw_info = grab_urusan_table_from_informasi_belanja_langsung_page(get_seed_url(2009, True))
# parse_apbd_belanja_langsung(2009, urusan_bl_main_page_raw_info, 'apbd_langsung_2009_2.csv')

urusan_bl_main_page_raw_info = grab_urusan_table_from_informasi_belanja_langsung_page(get_seed_url(2010, True))
parse_apbd_belanja_langsung(2010, urusan_bl_main_page_raw_info, 'apbd_langsung_2010_2.csv')

urusan_bl_main_page_raw_info = grab_urusan_table_from_informasi_belanja_langsung_page(get_seed_url(2011, True))
parse_apbd_belanja_langsung(2010, urusan_bl_main_page_raw_info, 'apbd_langsung_2011_2.csv')
