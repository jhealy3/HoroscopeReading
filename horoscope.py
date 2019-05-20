import urllib.request
import urllib.error
import urllib
import os

#provjera interneta i spajanja na stranicu
try:
	urllib.request.urlopen('https://www.astrology.com/horoscope/daily/libra.html')
#provjera URLErrora iz urllib.error modula
except urllib.error.URLError as e:
	if hasattr(e,'reason'):
		print('Spajanje na server je odbijeno.')
		print('Razlog: ',e.reason)
		os.system('kill $PPID')
	elif hasattr(e,'code'):
		print('Server nije mogao ispuniti zahtjev.')
		print('Error kod: ',e.code)		
		os.system('kill $PPID')
	else:
		print('Sve je u redu')

#integer za kasniju provjeru tocnosti horoskopskog znaka
horoskopski_znak = 0


print('Unesite horoskopski znak')

#provjeravamo je li horoskopski znak jedan od mogucih
while horoskopski_znak not in ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'):
	#unosimo zeljeni horoskopski znak
	horoskopski_znak = input()

	#ispisi poruku ako horoskopski znak nije tocan
	if horoskopski_znak not in ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'):
		print('Vas horoskopski znak nije jedan od: aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces. Pokusajte ponovo.')

#stranica s horoskopom
url = 'https://www.astrology.com/horoscope/daily/{}.html'.format(horoskopski_znak)

#spajamo se na stranicu
response = urllib.request.urlopen(url)

#uzimamo sadrzaj stranice kao string
json = str(response.read())

#dohvatimo pocetni index teksta
pocetak = json.find('bg sign-color"></i>')
#dohvatimo posljednji index teksta
kraj = json.find('</p>')

#isprintamo tekst
print(json[pocetak + 28:kraj])