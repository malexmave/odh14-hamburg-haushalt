odh14-hamburg-haushalt
======================

Open Data Day 2014: Hamburger Haushalt aus den Daten von daten.hamburg.de in ein Format für openspending.org bringen.

Das Projekt ist im Rahmen des Open Data Hackathon 2014 in Hamburg entstanden. Der Code ist eher auf der Seite eines bösen hacks als eines ernsthaften Skripts, aber es funktioniert.

# Dateien
In diesem Repository sind einige Dateien verstreut:

    HH2014.csv - Rohdaten des Hamburger Haushalts, extrahiert aus der Excel-Datei
    
    aggregat.csv
    aufgabenblock.csv
    einzelpl.csv
    funktionen.csv
    gruppierungen.csv
    kapitel.csv
    sonderkennz.csv
    titelgruppen.csv
    -- All diese Dateien enthalten Kategorisierungen der Transaktionen,
    ebenfalls aus der Excel-Datei extrahiert.
    
    haushalt-final.csv - Die Ausgabedatei des parser-skriptes
    
    parse.py - Parser-Skript, welches die Daten kombiniert und lesbar macht.

# Lizenz

Die Daten stehen unter der Datenlizenz Deutschland Namensnennung, (c) Freie und Hansestadt Hamburg, Finanzbehörde, 2014.

Das Skript steht unter der BSD 2-Clause License.
