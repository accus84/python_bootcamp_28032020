print(locals)           #pokaqzuje zmienne lokalne
print(globals)          #pokazuje zmienne globalne

#co to jest pip - narzędzie umożliwiające instalację pakietów (z terminala pythonowego)
#pip3 list - jakie pakiety mam zainstalowane - pojawi się lista zależnośći zewnętrznych, przydatne gdy komuś przekazujemy swój kod
#instalacja nowszych wersji bibliotek też może być problemem
#pip freeze > requirements.txt - przekierowanie do pliku tekstowego, ten plik będzie przydatny gdy komuś przekażemy kod z naszymi pakietami wymaganymi
#instalacja z requiremets: pip install -r requirements.txt
#instalacja pojedynczego modułu: pip install django
#jak używać requests - pozwala na pobieranie lub wysyłanie dany7ch do stron internetowych
import json
import requests
resp = requests.get("https://alx.pl")
resp
resp.status_code
resp.content

resp.json()