script='HHFH_Movie_v1.0.3'
code={'Denmark':'DNK','Sweden':'SWE','Australia':'AUS','UK':'UK','Serbia':'SER','Norway':'NOR', 'South Korea':'KOR','Japan':'JPN','China': 'CHI', 'Germany':'GER', 'France':'FRE','Spain':'SPA'}  # Country Code Dictionary
################################### imports ############################################################################################
from urllib import unquote
from re import compile
from re import MULTILINE
from requests import get
import pyperclip
import os.path
import os
from getpass import getuser
import sys
################################### Parse Filename#######################################

while True:
	try:
		mgnt=pyperclip.paste()
		while mgnt[:3]=='+al':
			print '$$ ERROR: A HHFH entry is already in clipboard. Copy a valid magnet first\n\n'
			os.system('pause')
			mgnt=pyperclip.paste()
		ftag=compile(r'.*dn=((.*\))(?:\+EXTENDED)?\+(?:%5B)?((?:HDRip|DVDScr|WEB-DL\+720p|WEB-?HD|BluRay|DVDRip)(?:\+m?(?:720p|1080p))?)(?:%5D)?.*)%5B.*%5D\.(?:mkv|mp4|avi)')
		srchr=ftag.search(mgnt)
		fname=srchr.group(1)
		break
	except:
		print "$$ ERROR: String Search Failed. Magnet not in clipboard\n\n"
		os.system('pause')
print '\n' + 'Script by Itachi_Uchiha '.center(65,'=') + '\n'
print '## Script:\t\t\t%s' % 'HHFH_Movie v1.0.3'
fname=unquote(fname.replace('+',' '))   #fname=fname.replace('%E2%84%A2','$')
title=srchr.group(2)
qlt=srchr.group(3)
qlt=qlt.replace('+',' ')
############################ Search Page Download ######################################

searchurl='http://www.imdb.com/find?q=' + title + '&s=tt'#&ttype=ft'
title=unquote(title.replace('+',' ')).replace(';',':').replace(' -',':')
print '## MovieTitle:\t\t\t' + title + '\n## Video Quality: \t\t' + qlt
if qlt=='BluRay 720p' or qlt=='BluRay 1080p':
	ql=qlt.split()
	qlt='['+'] ['.join(ql)+'] ['
else:
	qlt='['+qlt +'] ['
html=get(searchurl).content
print '## SearchURL:\t\t\t%s' % searchurl
print '## Search Page Loaded'
############################ Search Page Parsing ########################################

regex=compile(r'href="/title/tt(\d+)/')
try:
	imdb='http://www.imdb.com/title/tt' + regex.search(html).group(1)
except:
	print '$$ ERROR:\n\tString Search Failed. No title found. Properly name your file'
	os.system('pause')
	sys.exit(0)
print '## Found the Imdb link:\t\t%s' % imdb
movh=get(imdb).content
print '## Movie Page Loaded'
regex2=compile(r'\/(g)enre\/(\w+)\?ref_=tt_ov|(">)(.*)&nbsp;<span |\/(country)\/.*\s*.*>(\w+)<|\/(language)\/.*\s*.*>(\w+)<',MULTILINE) #TRUE
try:
	r=regex2.findall(movh)
except:
	print '$$ ERROR:\n\tString Search Failed. Check the IMDB link'
	os.system('pause')
	sys.exit(0)
print '## Page search complete'
entry='+al movie'
genre=[]
hin=''
known=0
country=[]
flag=0
lang=[]
for tag in r:
	if tag[0]=='g':
			genre.append(tag[1])
	elif tag[4]=='country':	
			country.append(tag[5])
	elif tag[-2]=='language':
		lang.append(tag[-1])
	else :
		known=tag[3]
print '## Genre:\t\t\t%s' % ','.join(genre)
if known!=title[:-7]:
	print '## Also Known As:\t\t%s' % known
print '## Language:\t\t\t%s' % ','.join(lang)
print '## Country:\t\t\t%s' % ','.join(country)
ctr=''
if 'USA' in country:
	ctr=''
elif country[0]=='India':
	ctr=''
	if lang[0]=='Malayalam':
		hin='MAL] [Eng-Subs] ['
	elif lang[0]=='Tamil':
		hin='TAM] [Eng-Subs] ['
	else:
		hin='HIN] ['
elif country[0]=='UK' or country[0]=='Australia':
	ctr=code[country[0]] +'] ['
else:
	if lang[0]=='English':
		ctr=code[country[0]] +'] ['
	else:
		ctr=code[country[0]] +'] [Eng-Subs] ['
###################### Size Tag ######################################

user=getuser()
fpath='C:\Users\\' + user + '\\AppData\Local\ApexDC++\Logs\system.log'
fpath1='C:\Users\\' + user  + '\\AppData\Local\DC++\Logs\system.log'
def sizet(fp,fname):
	f=open(fp)
	regx=compile(r'\\' + fname.replace('(','\\(').replace(')','\\)').replace('[','\\[').replace(']','\\]')+ '.*' + r'> \((\d+)\.(\d{2}) ([MG])iB at')
	fnamef=f.read()
	k=regx.search(fnamef)
	try:
		d1=k.group(1)
	except:
		print "$$ ERROR:\n\tString Search Failed. Could not find the file size in 'system.log'. Rehash your file"
		os.system('pause')
		sys.exit(0)
	d2=k.group(2)
	mg=k.group(3)
	d11=int(d1)
	dot='.'
	flag=0
	if mg=='M':
			if int(d2)>=50:
				d1=str(int(d1)+1)
			if d1=='1024':
					d1='1'
					d2='00'
					mg='G'
					flag=1
			if flag==0:
				dot=''
				d2=''
	size=d1 + dot + d2 + ' ' + mg + 'iB'
	return size
if os.path.isfile(fpath):
	print '## Client Detected:\t\tApexDC++'
	print '## Log file path:\t\t%s' % fpath
	size=sizet(fpath,fname)	#print size

elif os.path.isfile(fpath1):
	print '## Client Detected:\t\tDC++'
	print '## Log file path:\t%s' % fpath1
	size=sizet(fpath1,fname)
else:
	print '$$ ERROR:\n\tUnsupported Client Detected. Get ApexDC++ or DC++. Make sure system logging is enabled'
	print '$$ Log file should exist in:\n\t%s' % fpath1
	os.system('pause')
	sys.exit(0)
print '## Found the size of the file'
sd=''
if qlt[:4]=='[WEB' or qlt[:4]=='[Blu':
	pass
else:
	sd='sd'
if known!=title[:-7]:
	title=title[:-6] + '(AKA ' + known + ')' + title[-7:]
subs='] '
if 'KOR+Hard-Subs' in mgnt:
	subs+='[KOR Hard-Subs] '
elif 'EXTENDED' in mgnt:
	subs+='[EXTENDED] '
entry='+al ' + sd + 'movie ' + qlt  + ctr + hin + '] ['.join(genre) + subs + title + ' [ ' + imdb + '/ ] [' + size +'] ' + mgnt
pyperclip.copy(entry)
print '## Finished Successfully.\n## You can now use {CTRL} + {V} to get the entry'
os.system('pause')