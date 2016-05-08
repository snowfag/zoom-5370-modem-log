#!/usr/bin/env python2
import requests
import itertools
from bs4 import BeautifulSoup
import sys
try:
  requests.session().post("http://192.168.100.1/goform/login", data="{'EnterSubmit': 'Submit', 'loginUsername': 'admin', 'loginPassword': 'admin', 'LoginUserApply': '1'}", timeout=5)
except:
  print('Connection Error: Couldn\'t login.')
  sys.exit(1)
else:
  def info(url):
    try:
      return [[cell.text for cell in row("td")] for row in BeautifulSoup(requests.session().get(url, timeout=5).content, "lxml")("tr")]
    except:
      print('Connection Error: Error while connecting to {0}.').format(url)
      sys.exit(1)
  def gl(line):
    return ','.join(line).replace(u'\xa0',u'').replace(u'\n',u'')
  c = info('http://192.168.100.1/RgConnect.asp')
  s = info('http://192.168.100.1/RgSwInfo.asp')
  l = info('http://192.168.100.1/RgEventLog.asp')
  try:
    print ('###CONNECTION\n,\n#Startup\n,\nProcedure,Status,Comment\n{0}\n{1}\n{2}\n{3}\n{4}\n,\n#Downstream Bonded Channels\n,\nChannel,Lock Status,Modulation,Channel ID,Frequency,Power,SNR,Correctables,Uncorrectables\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}\n{12}\n{13}\n{14}\n{15}\n{16}\n{17}\n{18}\n{19}\n{20}\n,\nTotal Corractables,Total Uncorrectables\n{21}\n,\n#Upstream Bonded Channels\n,\nChannel,Lock Status,US Channel Type,Channel ID,Symbol Rate,Frequency,Power\n{22}\n{23}\n{24}\n{25}\n,\nCM IP Address,Duration,Expires\n{26}\n,\n###SOFTWARE\n,\n#Information\n,\n{27}\n{28}\n{29}\n{30}\n{31}\n{32}\n{33}\n,\n#Status\n,\n{34}\n{35}\n{36}\n,\n###SNMP Event Log\n,\n').format(gl(c[3]), gl(c[4]), gl(c[5]), gl(c[6]), gl(c[7]), gl(c[10]), gl(c[11]), gl(c[12]), gl(c[13]), gl(c[14]), gl(c[15]), gl(c[16]), gl(c[17]), gl(c[18]), gl(c[19]), gl(c[20]), gl(c[21]), gl(c[22]), gl(c[23]), gl(c[24]), gl(c[25]), gl(c[27]), gl(c[30]), gl(c[31]), gl(c[32]), gl(c[33]), gl(c[34]), gl(s[2]), gl(s[3]), gl(s[4]), gl(s[5]), gl(s[6]), gl(s[7]), gl(s[8]), gl(s[10]), gl(s[11]), gl(s[12]))
    for log in itertools.islice(l , 1, len(l)-1):
      logf = '|'.join(log).replace(u',',u';').split('|')
      print(gl(logf))
  except:
    print('Error occurred while formatting output.')
    sys.exit(1)
