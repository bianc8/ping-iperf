In terminale linux eseguire in ordine:
    1) traceroute 88.80.187.84
    2) il numero di righe è il numero di hop
    3) fare un po di prove cambiando il numero max nel ciclo for dello script ttl.sh
    4) ./ttl.sh

Aprire in un termainale il server di zingirian con:
    ssh {matricola}@88.80.187.84

    dentro al server di zingirian lancia istanza server di iperf
    <xyz> = 13000+ultime 4 cifre matricola
    iperf -s -p <xyz>

In un terminale in linux eseguire lo script iperf.sh che lancia dieci volte il comando iperf:
    ./iperf.sh

    Inserisci il bandwith in Mbit/s su un file excel

Ora esegui il file ping.sh che chiama 29 volte il comando ping dove ogni volta fa 100 ICMP_REQUEST al server di zingirian:
    ./ping.sh


Una volta che ping.sh ha finito:
    nella cartella results rinomina i file con numeri < 1000 con degli zeri, ad es:
        51.txt diventa 0051.txt
        151.txt diventa 0151.txt
        ...
        951.txt diventa 0951.txt

    ora lancia con python3 il file clean.py che crea (o sovrascrive) il file raw.xlsx con i dati estratti dai vari file di testo del ping
        python3 clean.py
    
Apri il file raw.xlsx e vai nella scheda rttMin, copia tutti i dati
Vai su google sheets e incolla i dati copiati da raw.xlsx
Metti delle intestazioni, x es:
    packetsize [bytes]	rtt min [ms]	rtt avg [ms]	rtt max [ms] 	rtt dev std [ms]
    51	                58,338         	97,747      	142,839     	24,18

Seleziona i dati comprese le intestazioni e vai su inserisci -> Grafico e seleziona grafico a linee
Modifica il grafico (in dx) --> Personalizza --> Serie --> Cambia "Applica a tutte le serie" in "rtt min" seleziona Linea di tendenza e su etichetta anzichè "Nessuna" metti "Utilizza equazione"

Così nell'equazione ti mostra la pendenza della retta
Altrimenti in una cella scrivi la formula
=PENDENZA(dati_y; dati_x) 
    al posto  di dati_y metti i dati del rtt minimo,
    al posto  di dati_x metti i dati del packetsize

Ora manca il confronto con i dati ottenuti da iperf:
    Il bandwith in MBits/sec di iperf dovrebbe essere simile a 1/pendenza
    In una cella fai =1/cella pendenza

