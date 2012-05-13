import urllib2

def get_seed(dummy=True):
    """returns html that contains all the school links"""
    # this seed is copy pasted from search performed using http://app.sis.moe.gov.sg/schinfo/SIS_AdvSearch.asp
    # result is generated randomly and does not show PSLE score from Normal(A) and Normal(T)
    
    if (dummy): # smaller seed set, faster to test
        seed = """
        <tbody><tr datagrid-row-index="0" style="height: 15px; " class="datagrid-row-over"><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3072&snm=ADMIRALTY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ADMIRALTY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="1" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3201&snm=AHMAD+IBRAHIM+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">AHMAD IBRAHIM SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="2" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3001&snm=ANDERSON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANDERSON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="3" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3026&snm=ANG+MO+KIO+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANG MO KIO SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="4" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7101&snm=ANGLICAN+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANGLICAN HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="5" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7032&snm=ANGLO%2DCHINESE+SCHOOL+%28BARKER+ROAD%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANGLO-CHINESE SCHOOL (BARKER ROAD) *</a></div></td></tr>
        """
    else: # real seed. 153 Schools
        seed = """
        <tbody><tr datagrid-row-index="0" style="height: 15px; " class="datagrid-row-over"><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3072&snm=ADMIRALTY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ADMIRALTY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="1" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3201&snm=AHMAD+IBRAHIM+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">AHMAD IBRAHIM SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="2" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3001&snm=ANDERSON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANDERSON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="3" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3026&snm=ANG+MO+KIO+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANG MO KIO SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="4" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7101&snm=ANGLICAN+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANGLICAN HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="5" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7032&snm=ANGLO%2DCHINESE+SCHOOL+%28BARKER+ROAD%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ANGLO-CHINESE SCHOOL (BARKER ROAD) *</a></div></td></tr><tr datagrid-row-index="6" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7002&snm=ASSUMPTION+ENGLISH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ASSUMPTION ENGLISH SCHOOL</a></div></td></tr><tr datagrid-row-index="7" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3501&snm=BALESTIER+HILL+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BALESTIER HILL SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="8" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3002&snm=BARTLEY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BARTLEY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="9" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3003&snm=BEATTY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEATTY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="10" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3069&snm=BEDOK+GREEN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEDOK GREEN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="11" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3033&snm=BEDOK+NORTH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEDOK NORTH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="12" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3027&snm=BEDOK+SOUTH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEDOK SOUTH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="13" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3229&snm=BEDOK+TOWN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEDOK TOWN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="14" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3225&snm=BEDOK+VIEW+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BEDOK VIEW SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="15" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3021&snm=BENDEMEER+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BENDEMEER SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="16" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3054&snm=BISHAN+PARK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BISHAN PARK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="17" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3224&snm=BOON+LAY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BOON LAY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="18" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3043&snm=BOWEN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BOWEN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="19" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3202&snm=BROADRICK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BROADRICK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="20" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3044&snm=BUKIT+BATOK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BUKIT BATOK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="21" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3203&snm=BUKIT+MERAH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BUKIT MERAH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="22" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3204&snm=BUKIT+PANJANG+GOVT%2E+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BUKIT PANJANG GOVT. HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="23" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3040&snm=BUKIT+VIEW+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">BUKIT VIEW SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="24" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3621&snm=CANBERRA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CANBERRA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="25" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3004&snm=CEDAR+GIRLS%C4+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CEDAR GIRLS' SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="26" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3402&snm=CHANGKAT+CHANGI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHANGKAT CHANGI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="27" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3206&snm=CHESTNUT+DRIVE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHESTNUT DRIVE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="28" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7008&snm=CHIJ+KATONG+CONVENT', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHIJ KATONG CONVENT *</a></div></td></tr><tr datagrid-row-index="29" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7004&snm=CHIJ+SECONDARY+%28TOA+PAYOH%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHIJ SECONDARY (TOA PAYOH) *</a></div></td></tr><tr datagrid-row-index="30" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7019&snm=CHIJ+ST%2E+JOSEPH%C4S+CONVENT', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHIJ ST. JOSEPH'S CONVENT *</a></div></td></tr><tr datagrid-row-index="31" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7023&snm=CHIJ+ST%2E+THERESA%C4S+CONVENT', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHIJ ST. THERESA'S CONVENT *</a></div></td></tr><tr datagrid-row-index="32" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3057&snm=CHONG+BOON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHONG BOON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="33" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7025&snm=CHRIST+CHURCH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHRIST CHURCH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="34" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3055&snm=CHUA+CHU+KANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHUA CHU KANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="35" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7104&snm=CHUNG+CHENG+HIGH+SCHOOL+%28MAIN%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHUNG CHENG HIGH SCHOOL (MAIN)</a></div></td></tr><tr datagrid-row-index="36" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7105&snm=CHUNG+CHENG+HIGH+SCHOOL+%28YISHUN%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CHUNG CHENG HIGH SCHOOL (YISHUN)</a></div></td></tr><tr datagrid-row-index="37" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3029&snm=CLEMENTI+TOWN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CLEMENTI TOWN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="38" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3404&snm=CLEMENTI+WOODS+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CLEMENTI WOODS SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="39" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3012&snm=COMMONWEALTH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">COMMONWEALTH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="40" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3622&snm=COMPASSVALE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">COMPASSVALE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="41" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3610&snm=CORAL+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CORAL SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="42" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3005&snm=CRESCENT+GIRLS%C4+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">CRESCENT GIRLS' SCHOOL</a></div></td></tr><tr datagrid-row-index="43" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3056&snm=DAMAI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">DAMAI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="44" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3228&snm=DEYI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">DEYI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="45" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3503&snm=DUNEARN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">DUNEARN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="46" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3207&snm=DUNMAN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">DUNMAN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="47" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3609&snm=EAST+SPRING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">EAST SPRING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="48" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3237&snm=EAST+VIEW+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">EAST VIEW SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="49" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3075&snm=EDGEFIELD+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">EDGEFIELD SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="50" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3623&snm=EVERGREEN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">EVERGREEN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="51" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7309&snm=FAIRFIELD+METHODIST+SCHOOL+%28SECONDARY%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">FAIRFIELD METHODIST SCHOOL (SECONDARY) *</a></div></td></tr><tr datagrid-row-index="52" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3064&snm=FAJAR+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">FAJAR SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="53" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3208&snm=FIRST+TOA+PAYOH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">FIRST TOA PAYOH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="54" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3024&snm=FUCHUN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">FUCHUN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="55" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3614&snm=FUHUA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">FUHUA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="56" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3006&snm=GAN+ENG+SENG+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GAN ENG SENG SCHOOL</a></div></td></tr><tr datagrid-row-index="57" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7005&snm=GEYLANG+METHODIST+SCHOOL+%28SECONDARY%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GEYLANG METHODIST SCHOOL (SECONDARY) *</a></div></td></tr><tr datagrid-row-index="58" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3074&snm=GREENDALE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GREENDALE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="59" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3051&snm=GREENRIDGE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GREENRIDGE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="60" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3059&snm=GREENVIEW+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GREENVIEW SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="61" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3238&snm=GUANGYANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">GUANGYANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="62" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7031&snm=HAI+SING+CATHOLIC+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HAI SING CATHOLIC SCHOOL</a></div></td></tr><tr datagrid-row-index="63" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3016&snm=HENDERSON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HENDERSON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="64" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3048&snm=HILLGROVE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HILLGROVE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="65" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7108&snm=HOLY+INNOCENTS%C4+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HOLY INNOCENTS' HIGH SCHOOL *</a></div></td></tr><tr datagrid-row-index="66" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3060&snm=HONG+KAH+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HONG KAH SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="67" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3046&snm=HOUGANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HOUGANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="68" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3226&snm=HUA+YI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">HUA YI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="69" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3608&snm=JUNYUAN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">JUNYUAN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="70" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3211&snm=JURONG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">JURONG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="71" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3068&snm=JURONG+WEST+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">JURONG WEST SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="72" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3063&snm=JURONGVILLE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">JURONGVILLE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="73" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3066&snm=JUYING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">JUYING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="74" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3619&snm=KENT+RIDGE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">KENT RIDGE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="75" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3065&snm=KRANJI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">KRANJI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="76" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7028&snm=KUO+CHUAN+PRESBYTERIAN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">KUO CHUAN PRESBYTERIAN SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="77" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3049&snm=LOYANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">LOYANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="78" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3212&snm=MACPHERSON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">MACPHERSON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="79" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7307&snm=MANJUSRI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">MANJUSRI SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="80" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3615&snm=MARSILING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">MARSILING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="81" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3031&snm=MAYFLOWER+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">MAYFLOWER SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="82" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7011&snm=MONTFORT+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">MONTFORT SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="83" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7112&snm=NAN+CHIAU+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NAN CHIAU HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="84" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3047&snm=NAN+HUA+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NAN HUA HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="85" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7114&snm=NANYANG+GIRLS%C4+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NANYANG GIRLS' HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="86" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3214&snm=NAVAL+BASE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NAVAL BASE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="87" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3507&snm=NEW+TOWN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NEW TOWN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="88" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7310&snm=NGEE+ANN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NGEE ANN SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="89" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3602&snm=NORTH+VIEW+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NORTH VIEW SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="90" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3071&snm=NORTH+VISTA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NORTH VISTA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="91" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3612&snm=NORTHBROOKS+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NORTHBROOKS SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="92" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3058&snm=NORTHLAND+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NORTHLAND SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="93" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7803&snm=NORTHLIGHT+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">NORTHLIGHT SCHOOL</a></div></td></tr><tr datagrid-row-index="94" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3605&snm=ORCHID+PARK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ORCHID PARK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="95" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3215&snm=OUTRAM+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">OUTRAM SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="96" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3613&snm=PASIR+RIS+CREST+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PASIR RIS CREST SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="97" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3235&snm=PASIR+RIS+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PASIR RIS SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="98" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7026&snm=PAYA+LEBAR+METHODIST+GIRLS%C4+SCHOOL+%28SECONDARY%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PAYA LEBAR METHODIST GIRLS' SCHOOL (SECONDARY) *</a></div></td></tr><tr datagrid-row-index="99" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3073&snm=PEI+HWA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PEI HWA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="100" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3232&snm=PEICAI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PEICAI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="101" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3061&snm=PEIRCE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PEIRCE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="102" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3231&snm=PING+YI+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PING YI SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="103" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3062&snm=PIONEER+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PIONEER SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="104" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7308&snm=PRESBYTERIAN+HIGH+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PRESBYTERIAN HIGH SCHOOL</a></div></td></tr><tr datagrid-row-index="105" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3070&snm=PUNGGOL+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">PUNGGOL SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="106" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3508&snm=QUEENSTOWN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">QUEENSTOWN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="107" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3007&snm=QUEENSWAY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">QUEENSWAY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="108" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3008&snm=RAFFLES+GIRLS%C4+SCHOOL+%28SECONDARY%29', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">RAFFLES GIRLS' SCHOOL (SECONDARY)</a></div></td></tr><tr datagrid-row-index="109" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3618&snm=REGENT+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">REGENT SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="110" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3239&snm=RIVERSIDE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">RIVERSIDE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="111" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7805&snm=SCHOOL+OF+SCIENCE+AND+TECHNOLOGY%2C+SINGAPORE', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SCHOOL OF SCIENCE AND TECHNOLOGY, SINGAPORE</a></div></td></tr><tr datagrid-row-index="112" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3606&snm=SEMBAWANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SEMBAWANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="113" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3607&snm=SENG+KANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SENG KANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="114" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3509&snm=SERANGOON+GARDEN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SERANGOON GARDEN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="115" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3010&snm=SERANGOON+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SERANGOON SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="116" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3234&snm=SHUQUN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SHUQUN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="117" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3227&snm=SI+LING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SI LING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="118" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3011&snm=SIGLAP+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SIGLAP SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="119" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7800&snm=SINGAPORE+SPORTS+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SINGAPORE SPORTS SCHOOL</a></div></td></tr><tr datagrid-row-index="120" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3053&snm=SPRINGFIELD+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SPRINGFIELD SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="121" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7015&snm=ST%2E+ANDREW%C4S+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. ANDREW'S SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="122" style="height: 29px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7016&snm=ST%2E+ANTHONY%C4S+CANOSSIAN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. ANTHONY'S CANOSSIAN SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="123" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7017&snm=ST%2E+GABRIEL%C4S+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. GABRIEL'S SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="124" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7029&snm=ST%2E+HILDA%C4S+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. HILDA'S SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="125" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7020&snm=ST%2E+JOSEPH%C4S+INSTITUTION', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. JOSEPH'S INSTITUTION *</a></div></td></tr><tr datagrid-row-index="126" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7021&snm=ST%2E+MARGARET%C4S+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. MARGARET'S SECONDARY SCHOOL *</a></div></td></tr><tr datagrid-row-index="127" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7022&snm=ST%2E+PATRICK%C4S+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ST. PATRICK'S SCHOOL *</a></div></td></tr><tr datagrid-row-index="128" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3304&snm=SWISS+COTTAGE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">SWISS COTTAGE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="129" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3037&snm=TAMPINES+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TAMPINES SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="130" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3511&snm=TANGLIN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TANGLIN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="131" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3013&snm=TANJONG+KATONG+GIRLS%C4+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TANJONG KATONG GIRLS' SCHOOL</a></div></td></tr><tr datagrid-row-index="132" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3512&snm=TANJONG+KATONG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TANJONG KATONG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="133" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3403&snm=TECK+WHYE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TECK WHYE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="134" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3030&snm=TEMASEK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">TEMASEK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="135" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3611&snm=UNITY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">UNITY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="136" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3014&snm=VICTORIA+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">VICTORIA SCHOOL</a></div></td></tr><tr datagrid-row-index="137" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3067&snm=WEST+SPRING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WEST SPRING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="138" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3620&snm=WESTWOOD+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WESTWOOD SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="139" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3015&snm=WHITLEY+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WHITLEY SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="140" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3616&snm=WOODGROVE+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WOODGROVE SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="141" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3604&snm=WOODLANDS+RING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WOODLANDS RING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="142" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3041&snm=WOODLANDS+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">WOODLANDS SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="143" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3050&snm=XINMIN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">XINMIN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="144" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3222&snm=YIO+CHU+KANG+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YIO CHU KANG SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="145" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3020&snm=YISHUN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YISHUN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="146" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3045&snm=YISHUN+TOWN+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YISHUN TOWN SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="147" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3223&snm=YUAN+CHING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YUAN CHING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="148" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3019&snm=YUHUA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YUHUA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="149" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3307&snm=YUSOF+ISHAK+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YUSOF ISHAK SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="150" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=7027&snm=YUYING+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">YUYING SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="151" style="height: 15px; "><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3617&snm=ZHENGHUA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ZHENGHUA SECONDARY SCHOOL</a></div></td></tr><tr datagrid-row-index="152" style="height: 15px; " class=""><td field="itemid" class="schoolColumn"><div style="width:232px;text-align:left;" class="datagrid-cell "><a href="JavaScript:void window.open('SIS_SearchDtls.asp?strCode=3240&snm=ZHONGHUA+SECONDARY+SCHOOL', '_blank','top=0,left=0, width=800px,height=600px, scrollbars=yes,location=no,menubar=no,resizable=yes,status=yes,directories=no,toolbar=no')" class="style11">ZHONGHUA SECONDARY SCHOOL</a></div></td></tr></tbody>
        """
    return seed

def get_page(url):
    """return html string of a page given its URL. Return 'error' in case of any slip."""
    try:
        usock = urllib2.urlopen(url)
        page = usock.read()
        usock.close()
        return page
    except:
        return 'error' #doh!
        
def get_all_schools_info(page):    
    """Get all links and name of school to be stored in dictionary object which will be stored in returned schools list"""
    schools = {}
    
    # just iterate all the time until there will be no more URL
    while True:
        # get url of the school page, school name and location of the end of the latest grabbed url
        url, school_name, endpos = get_next_target(page)
        
        # store name and url accordingly 
        # if there is URL, store it in links
        if url:  
            temp_school       = School()
            temp_school.name  = school_name
            temp_school.url   = url
            
            schools[temp_school.name]    = temp_school
            page = page[endpos:]
        else:
            break
            
    # return schools array
    return schools

def get_next_target(page):
    """Get the NEXT link to individual school page. Return url, school_name and position of end_quote of the last URL"""
    # get he start of link to school based on seed
    # modify accordingly
    start_link = page.find('<a href="JavaScript:void window.open(')
    
     # cannot find any more link return None, None, 0 instead
    if start_link == -1:
        return None, None, 0
        
    # GET URL HERE 
    # go to the start of the link which is a quote
    start_quote = page.find('\'', start_link) 
    
    # go to the end of the link which is a quote
    end_quote = page.find('\'', start_quote + 1) 
    
    # grab URL and furnish URL with proper http and domain
    url = "http://app.sis.moe.gov.sg/schinfo/%s" % page[start_quote + 1:end_quote]
    
    # GET SCHOOL NAME HERE
    # go to the start of school name
    start_of_school_name = page.find('>',end_quote)
    
    # go to the end of school name
    end_of_school_name = page.find('</a>',start_of_school_name+1)
    
    # grab school name
    school_name = page[start_of_school_name+1:end_of_school_name]
    
    # Return url of the school page, school name and location of the end of the latest grabbed url
    return url, school_name, end_quote  



def grab_raw_psle_score_table(url):
    """download html code from page of url and grab the portion that contains table of psle score"""
    
    # download all the html code
    page = get_page(url)
    
    # mark the start of score table
    start_psle_info = page.find('<!-- GET AGGREGATE RANGE SECTION -->')
    if start_psle_info == -1: 
        return "error: none"
    start_quote = page.find('>', start_psle_info)
    end_quote = page.find('<!-- END OF AGGREGATE RANGE SECTION -->', start_quote+1)
    psle_info = page[start_quote+1:end_quote]
    return psle_info

   
def parse_raw_psle_score_table(school, raw_info): 
    """parse the raw psle score table into something that can be processed easily"""
    # TODO Change school dictionary to class
    
    start_start_row     = 0
    
    while start_start_row != -1:
        school,  start_start_row = parse_one_row_of_raw_psle_score_table(school, raw_info, start_start_row)   
    print 'parsing data of %s' % school.name
    return school
    
def parse_one_row_of_raw_psle_score_table(school_dictionary, raw_info, start_of_next_row):
    """parse one row of raw psle score table into something that can be processed easily"""
    # grab the first row ONLY
    # STREAM, LOWER, UPPER, MEAN, MEDIAN, LOWER_AFFILIATE, UPPER_AFFILIATE, MEAN_AFFILIATE, MEDIAN_AFFILIATE

    start_start_row     = raw_info.find('<tr', start_of_next_row)

    if start_start_row == -1:
        return school_dictionary, start_start_row
    else: 
        end_start_row       = raw_info.find('>', start_start_row+1)

        # get the STREAM --> Express NormalA NormalT
        start_stream_name  = raw_info.find('<td', end_start_row) # lazy since there are many properties in between
        start_stream_name  = raw_info.find('>', start_stream_name) # lazy
        end_stream_name    = raw_info.find('</td>', start_stream_name+1)
        stream = raw_info[start_stream_name+1:end_stream_name] 

        # get NON_AFFILIATE values
        next_posted = raw_info.find("<td align='center'>", end_stream_name+1)
        next_none_posted = raw_info.find("<td align='center' colspan='2'>", end_stream_name+1)
        
        # stupid hack
        if next_posted == -1:
            next_posted = 10000
        if next_none_posted == -1:
            next_none_posted = 10000

        if next_posted < next_none_posted:

            # there is info on Non affiliate Lower and Upper value
            start_lower_non_affiliate        = raw_info.find("<td align='center'>", end_stream_name+1)
            start_lower_non_affiliate_value  = raw_info.find(";", start_lower_non_affiliate+1) # from &nbsp; 
            end_lower_non_affiliate_value    = raw_info.find("</td>", start_lower_non_affiliate_value+1) 
            lower_non_affiliate_value        = raw_info[start_lower_non_affiliate_value+1:end_lower_non_affiliate_value] 

            start_upper_non_affiliate        = raw_info.find("<td align='center'>", end_lower_non_affiliate_value+1)
            start_upper_non_affiliate_value  = raw_info.find(";", start_upper_non_affiliate+1) # from &nbsp; 
            end_upper_non_affiliate_value    = raw_info.find("</td>", start_upper_non_affiliate_value+1) 
            upper_non_affiliate_value        = raw_info[start_upper_non_affiliate_value+1:end_upper_non_affiliate_value] 

            start_mean_non_affiliate         = raw_info.find("<td align='center'>", end_upper_non_affiliate_value+1)
            start_mean_non_affiliate_value   = raw_info.find(";", start_mean_non_affiliate+1) # from &nbsp; 
            end_mean_non_affiliate_value     = raw_info.find("</td>", start_mean_non_affiliate_value+1) 
            mean_non_affiliate_value         = raw_info[start_mean_non_affiliate_value+1:end_mean_non_affiliate_value] 
            
            start_median_non_affiliate       = raw_info.find("<td align='center'>", end_mean_non_affiliate_value+1)
            start_median_non_affiliate_value = raw_info.find(";", start_median_non_affiliate+1) # from &nbsp; 
            end_median_non_affiliate_value   = raw_info.find("</td>", start_median_non_affiliate_value+1) 
            median_non_affiliate_value       = raw_info[start_median_non_affiliate_value+1:end_median_non_affiliate_value] 
            
            # convenience
            end_of_non_affiliate_values           = raw_info.find('d>', end_median_non_affiliate_value+1)

        else:
            
            # just assign none to all
            lower_non_affiliate_value   = "NA"
            upper_non_affiliate_value   = "NA"
            mean_non_affiliate_value    = "NA"
            median_non_affiliate_value  = "NA"

            # convenience
            # there are bound to have 2 x colspan=2
            end_of_non_affiliate_values          = raw_info.find("colspan='2'>", end_stream_name+1)
            end_of_non_affiliate_values          = raw_info.find('</td>', end_of_non_affiliate_values+1) #lazy
            end_of_non_affiliate_values          = raw_info.find("colspan='2'>", end_of_non_affiliate_values+1) #lazy
            end_of_non_affiliate_values          = raw_info.find('</td>', end_of_non_affiliate_values+1) #lazy

        next_posted = raw_info.find("<td align='center'>", end_of_non_affiliate_values+1)
        next_none_posted = raw_info.find("<td align='center' colspan='2'>", end_of_non_affiliate_values+1)
        
        # stupid hack
        if next_posted == -1:
            next_posted = 10000
        if next_none_posted == -1:
            next_none_posted = 10000
            
        # get AFFILIATE values
        if next_posted < next_none_posted:
            
            # there is info on Non affiliate Lower and Upper value
            start_lower_affiliate        = raw_info.find("<td align='center'>", end_of_non_affiliate_values+1)
            start_lower_affiliate_value  = raw_info.find(";", start_lower_affiliate+1) # from &nbsp; 
            end_lower_affiliate_value    = raw_info.find("</td>", start_lower_affiliate_value+1) 
            lower_affiliate_value        = raw_info[start_lower_affiliate_value+1:end_lower_affiliate_value] 

            start_upper_affiliate        = raw_info.find("<td align='center'>", end_lower_affiliate_value+1)
            start_upper_affiliate_value  = raw_info.find(";", start_upper_affiliate+1) # from &nbsp; 
            end_upper_affiliate_value    = raw_info.find("</td>", start_upper_affiliate_value+1) 
            upper_affiliate_value        = raw_info[start_upper_affiliate_value+1:end_upper_affiliate_value] 

            start_mean_affiliate         = raw_info.find("<td align='center'>", end_upper_affiliate_value+1)
            start_mean_affiliate_value   = raw_info.find(";", start_mean_affiliate+1) # from &nbsp; 
            end_mean_affiliate_value     = raw_info.find("</td>", start_mean_affiliate_value+1) 
            mean_affiliate_value         = raw_info[start_mean_affiliate_value+1:end_mean_affiliate_value] 
            
            start_median_affiliate       = raw_info.find("<td align='center'>", end_mean_affiliate_value+1)
            start_median_affiliate_value = raw_info.find(";", start_median_affiliate+1) # from &nbsp; 
            end_median_affiliate_value   = raw_info.find("</td>", start_median_affiliate_value+1) 
            median_affiliate_value       = raw_info[start_median_affiliate_value+1:end_median_affiliate_value] 
            
            # convenience
            end_of_affiliate_values          = raw_info.find('d>', end_median_affiliate_value+1)
        else:
            
            # just assign none to all
            lower_affiliate_value   = "NA"
            upper_affiliate_value   = "NA"
            mean_affiliate_value    = "NA"
            median_affiliate_value  = "NA"

            # convenience
            # there are bound to have 2 x colspan=2
            end_of_affiliate_values          = raw_info.find("colspan='2'>", end_of_non_affiliate_values+1)
            end_of_affiliate_values          = raw_info.find('</td>', end_of_affiliate_values+1) #lazy
            end_of_affiliate_values          = raw_info.find("colspan='2'>", end_of_affiliate_values+1) #lazy
            end_of_affiliate_values          = raw_info.find('</td>', end_of_affiliate_values+1) #lazy
            
        # get location of the </tr>
        end_of_row = raw_info.find('</tr>', end_of_affiliate_values+1) #lazy

        # school_dictionary['stream']                     = stream 
        
        if stream.strip() == 'Express':
            school_dictionary.NA_ExpressLower    = lower_non_affiliate_value
            school_dictionary.NA_ExpressUpper    = upper_non_affiliate_value
            school_dictionary.NA_ExpressMean     = mean_non_affiliate_value
            school_dictionary.NA_ExpressMedian   = median_non_affiliate_value       
            school_dictionary.A_ExpressLower     = lower_affiliate_value
            school_dictionary.A_ExpressUpper     = upper_affiliate_value
            school_dictionary.A_ExpressMean      = mean_affiliate_value
            school_dictionary.A_ExpressMedian    = median_affiliate_value
        elif stream.strip() == 'Normal (Academic)':
            school_dictionary.NA_NormalALower    = lower_non_affiliate_value
            school_dictionary.NA_NormalAUpper    = upper_non_affiliate_value
            school_dictionary.NA_NormalAMean     = mean_non_affiliate_value
            school_dictionary.NA_NormalAMedian   = median_non_affiliate_value       
            school_dictionary.A_NormalALower     = lower_affiliate_value
            school_dictionary.A_NormalAUpper     = upper_affiliate_value
            school_dictionary.A_NormalAMean      = mean_affiliate_value
            school_dictionary.A_NormalAMedian    = median_affiliate_value
        elif stream.strip() == 'Normal (Technical)':
            school_dictionary.NA_NormalTLower    = lower_non_affiliate_value
            school_dictionary.NA_NormalTUpper    = upper_non_affiliate_value
            school_dictionary.NA_NormalTMean     = mean_non_affiliate_value
            school_dictionary.NA_NormalTMedian   = median_non_affiliate_value       
            school_dictionary.A_NormalTLower     = lower_affiliate_value
            school_dictionary.A_NormalTUpper     = upper_affiliate_value
            school_dictionary.A_NormalTMean      = mean_affiliate_value
            school_dictionary.A_NormalTMedian    = median_affiliate_value
 
        
        """
        school_dictionary['lower_affiliate_value']      = lower_affiliate_value
        school_dictionary['upper_affiliate_value']      = upper_affiliate_value
        school_dictionary['mean_affiliate_value']       = mean_affiliate_value
        school_dictionary['median_affiliate_value']     = median_affiliate_value
        
        school_dictionary['lower_non_affiliate_value']  = lower_non_affiliate_value
        school_dictionary['upper_non_affiliate_value']  = upper_non_affiliate_value
        school_dictionary['mean_non_affiliate_value']   = mean_non_affiliate_value
        school_dictionary['median_non_affiliate_value'] = median_non_affiliate_value
        """
        
        """
        print "na: %s %s %s %s aa: %s %s %s %s n: %s stream: %s" % ( 
          school_dictionary['lower_non_affiliate_value'],
          school_dictionary['upper_non_affiliate_value'],
          school_dictionary['mean_non_affiliate_value'],  
          school_dictionary['median_non_affiliate_value'],
          school_dictionary['lower_affiliate_value'],     
          school_dictionary['upper_affiliate_value'],     
          school_dictionary['mean_affiliate_value'],    
          school_dictionary['median_affiliate_value'],
          school_dictionary['name'],
          school_dictionary['stream'])
        """
        
        # print school_dictionary.test_string()

        return school_dictionary, end_of_row
    
def get_psle_cutoff_point(all_schools):
    for key, value in all_schools.items():
        # print key, value
        raw_psle_score_table = grab_raw_psle_score_table(all_schools[key].url)
        all_schools[key] = parse_raw_psle_score_table(all_schools[key], raw_psle_score_table)
    return all_schools
    
class School(object):

    def __init__(self):
        self.name = 'No name'
        self.url  = 'No url'
        
        self.NA_ExpressLower    = 'NA'
        self.NA_ExpressUpper    = 'NA'
        self.NA_ExpressMean     = 'NA'
        self.NA_ExpressMedian   = 'NA'
        self.NA_NormalALower    = 'NA'
        self.NA_NormalAUpper    = 'NA'
        self.NA_NormalAMean     = 'NA'
        self.NA_NormalAMedian   = 'NA'     
        self.NA_NormalTLower    = 'NA'
        self.NA_NormalTUpper    = 'NA'
        self.NA_NormalTMean     = 'NA'
        self.NA_NormalTMedian   = 'NA'
        
        self.A_ExpressLower     = 'NA'
        self.A_ExpressUpper     = 'NA'
        self.A_ExpressMean      = 'NA'
        self.A_ExpressMedian    = 'NA'
        self.A_NormalALower     = 'NA'
        self.A_NormalAUpper     = 'NA'
        self.A_NormalAMean      = 'NA'
        self.A_NormalAMedian    = 'NA'     
        self.A_NormalTLower     = 'NA'
        self.A_NormalTUpper     = 'NA'
        self.A_NormalTMean      = 'NA'
        self.A_NormalTMedian    = 'NA'    

    def test_string(self):
        print '%s %s' % (self.name, self.url)
        print 'NA E: %s %s %s %s Na: %s %s %s %s Nt: %s %s %s %s' % (
          self.NA_ExpressLower, 
          self.NA_ExpressUpper, 
          self.NA_ExpressMean, 
          self.NA_ExpressMedian, 
          self.NA_NormalALower, 
          self.NA_NormalAUpper, 
          self.NA_NormalAMean, 
          self.NA_NormalAMedian, 
          self.NA_NormalTLower, 
          self.NA_NormalTUpper, 
          self.NA_NormalTMean, 
          self.NA_NormalTMedian)
        print 'A  E: %s %s %s %s Na: %s %s %s %s Nt: %s %s %s %s' % (
          self.A_ExpressLower, 
          self.A_ExpressUpper, 
          self.A_ExpressMean, 
          self.A_ExpressMedian, 
          self.A_NormalALower, 
          self.A_NormalAUpper, 
          self.A_NormalAMean, 
          self.A_NormalAMedian, 
          self.A_NormalTLower, 
          self.A_NormalTUpper, 
          self.A_NormalTMean, 
          self.A_NormalTMedian)
    
def dump_to_a_file(all_schools):
    # determine the filename header and footer
    filename = "SchoolsInfo.dat"
    
    header = """
      <?xml version="1.0"?>
      <ArrayOfSchoolInfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    """
    
    footer = """
      </ArrayOfSchoolInfo>
    """
    
    # Create a file object in "write" mode
    target = open(filename,'w')
    
    # Truncate the file. 
    target.truncate()

    target.write(header)
    target.write('\n')

    # JUST WHACK FOR NOW. DAMMIT SO MESSY
    for key, value in all_schools.items():
        # print key, value
        target.write('<SchoolInfo>')
        target.write('\n')
        
        target.write('<Name>')
        target.write(all_schools[key].name)
        target.write('</Name>')
        target.write('\n')
        
        target.write('<NA_ExpressLower>')
        target.write(all_schools[key].NA_ExpressLower)
        target.write('</NA_ExpressLower>')
        target.write('\n')
        
        target.write('<NA_ExpressUpper>')
        target.write(all_schools[key].NA_ExpressUpper)
        target.write('</NA_ExpressUpper>')
        target.write('\n')
        
        target.write('<NA_ExpressMean>')
        target.write(all_schools[key].NA_ExpressMean)
        target.write('</NA_ExpressMean>')
        target.write('\n')
        
        target.write('<NA_ExpressMedian>')
        target.write(all_schools[key].NA_ExpressMedian)
        target.write('</NA_ExpressMedian>')
        target.write('\n')
        
        target.write('<NA_NormalALower>')
        target.write(all_schools[key].NA_NormalALower)
        target.write('</NA_NormalALower>')
        target.write('\n')
        
        target.write('<NA_NormalAUpper>')
        target.write(all_schools[key].NA_NormalAUpper)
        target.write('</NA_NormalAUpper>')
        target.write('\n')
        
        target.write('<NA_NormalAMean>')
        target.write(all_schools[key].NA_NormalAMean)
        target.write('</NA_NormalAMean>')
        target.write('\n')
        
        target.write('<NA_NormalAMedian>')
        target.write(all_schools[key].NA_NormalAMedian)
        target.write('</NA_NormalAMedian>')
        target.write('\n')
        
        target.write('<NA_NormalTLower>')
        target.write(all_schools[key].NA_NormalTLower)
        target.write('</NA_NormalTLower>')
        target.write('\n')
        
        target.write('<NA_NormalTUpper>')
        target.write(all_schools[key].NA_NormalTUpper)
        target.write('</NA_NormalTUpper>')
        target.write('\n')
        
        target.write('<NA_NormalTMean>')
        target.write(all_schools[key].NA_NormalTMean)
        target.write('</NA_NormalTMean>')
        target.write('\n')
        
        target.write('<NA_NormalTMedian>')
        target.write(all_schools[key].NA_NormalTMedian)
        target.write('</NA_NormalTMedian>')
        target.write('\n')
        

        target.write('<A_ExpressLower>')
        target.write(all_schools[key].A_ExpressLower)
        target.write('</A_ExpressLower>')
        target.write('\n')
        
        target.write('<A_ExpressUpper>')
        target.write(all_schools[key].A_ExpressUpper)
        target.write('</A_ExpressUpper>')
        target.write('\n')
        
        target.write('<A_ExpressMean>')
        target.write(all_schools[key].A_ExpressMean)
        target.write('</A_ExpressMean>')
        target.write('\n')
        
        target.write('<A_ExpressMedian>')
        target.write(all_schools[key].A_ExpressMedian)
        target.write('</A_ExpressMedian>')
        target.write('\n')
        
        target.write('<A_NormalALower>')
        target.write(all_schools[key].A_NormalALower)
        target.write('</A_NormalALower>')
        target.write('\n')
        
        target.write('<A_NormalAUpper>')
        target.write(all_schools[key].A_NormalAUpper)
        target.write('</A_NormalAUpper>')
        target.write('\n')
        
        target.write('<A_NormalAMean>')
        target.write(all_schools[key].A_NormalAMean)
        target.write('</A_NormalAMean>')
        target.write('\n')
        
        target.write('<A_NormalAMedian>')
        target.write(all_schools[key].A_NormalAMedian)
        target.write('</A_NormalAMedian>')
        target.write('\n')
        
        target.write('<A_NormalTLower>')
        target.write(all_schools[key].A_NormalTLower)
        target.write('</A_NormalTLower>')
        target.write('\n')
        
        target.write('<A_NormalTUpper>')
        target.write(all_schools[key].A_NormalTUpper)
        target.write('</A_NormalTUpper>')
        target.write('\n')
        
        target.write('<A_NormalTMean>')
        target.write(all_schools[key].A_NormalTMean)
        target.write('</A_NormalTMean>')
        target.write('\n')
        
        target.write('<A_NormalTMedian>')
        target.write(all_schools[key].A_NormalTMedian)
        target.write('</A_NormalTMedian>')
        target.write('\n')


        target.write('</SchoolInfo>')
        target.write('\n')
    target.write(footer)
    
    
    target.close()
    

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)  
            
# get the links
all_schools = get_all_schools_info(get_seed())
# get necessary psle schore
all_schools = get_psle_cutoff_point(all_schools)

dump_to_a_file(all_schools)



