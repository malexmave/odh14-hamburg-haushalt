# -*- coding: utf-8 -*-
# Copyright (c) <YEAR>, <OWNER>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions 
# are met:
# 
# 1. Redistributions of source code must retain the above copyright 
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright 
# notice, this list of conditions and the following disclaimer in the 
# documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY 
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.

import csv

gruppenbez = {}
aggregatbez = {}
funktionsbez = {}
kapitelbez = {}
sonderkennzbez = {}
titelbez = {}
aufgabenblockbez = {}
planbez = {}

with open('gruppierung.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		gruppenbez[row[0]] = row[1]

with open('aggregat.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		aggregatbez[row[1]] = row[2]

with open('funktionen.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		funktionsbez[row[0]] = row[1]

with open('kapitel.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		kapitelbez[row[1]] = row[6]

with open('sonderkennz.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		sonderkennzbez[row[1]] = row[2]

with open('titelgruppen.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		titelbez[row[3]] = row[4]

with open('aufgabenblock.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		aufgabenblockbez[row[1]] = row[2]

with open('einzelpl.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		planbez[row[1]] = row[2]

output = []
with open('HH2014.csv', 'r') as datafile:
	datareader = csv.reader(datafile, delimiter=',')
	header = ["Einzelplan", "Einzelplanbezeichnung",
		"Aufgabenblock", "Aufgabenblockbezeichnung",
		"Aggregat", "Aggregatbezeichnung", 
		"Kapitel", "Kapitelbezeichnung",
		"Einnahme / Ausgabe", 
		"Hauptgruppe", "Hauptgruppenbezeichnung", 
		"Obergruppe", "Obergruppenbezeichnung",
		"Gruppe", "Gruppenbezeichnung",
		"Titelendnr", "Titelbezeichnung",
		"Finanzposition",
		"Finanzstelle AOB",
		"Zweckbestimmung",
		"Funktion", "Funktionsbezeichnung",
		"Übertragbar",
		"Leertitel",
		"wgf Ansatz",
		"Wegfall ab Gjahr",
		"E/A-Vermerk",
		"Sonderkennzeichen", "Sonderkennzeichenbezeichnung",
		"Budget-titel = x",
		"NSM-Titel = x",
		"Zuwendungsanteil",
		"Personalkosten-Anteil",
		"Hafenanteil",
		"Betrag",
		"Jahr"
		]
	output += [header]
	skip = True
	for row in datareader:
		if not skip:
			record2010 = [
				row[ 0].rstrip(), planbez[row[0]] if row[0] in planbez else "",
				row[ 1].rstrip(), aufgabenblockbez[row[1]] if row[1] in aufgabenblockbez else "",
				row[ 2].rstrip(), aggregatbez[row[2]] if row[2] in aggregatbez else "",
				row[ 3].rstrip(), kapitelbez[row[3]] if row[3] in kapitelbez else "",
				row[ 4].rstrip(),
				row[ 5].rstrip(), gruppenbez[row[5]] if row[5] in gruppenbez else "",
				row[ 6].rstrip(), gruppenbez[row[6]] if row[6] in gruppenbez else "",
				row[ 7].rstrip(), gruppenbez[row[7]] if row[7] in gruppenbez else "",
				row[ 8].rstrip(), titelbez[row[8]] if row[8] in titelbez else "",
				row[ 9].rstrip(),
				row[10].rstrip(),
				row[11].rstrip(),
				row[12].rstrip(), funktionsbez[row[12]] if row[12] in funktionsbez else "",
				row[13].rstrip(), 
				row[14].rstrip(),
				row[15].rstrip(),
				row[16].rstrip(),
				row[19].rstrip(),
				row[22].rstrip(), sonderkennzbez[row[22]] if row[22] in sonderkennzbez else "",
				row[23].rstrip(),
				row[24].rstrip(),
				row[25].rstrip(),
				row[26].rstrip(),
				row[27].rstrip(),
				row[28].rstrip(),
				"2010"
			]
			record2011 = [
				row[ 0].rstrip(), planbez[row[0]] if row[0] in planbez else "",
				row[ 1].rstrip(), aufgabenblockbez[row[1]] if row[1] in aufgabenblockbez else "",
				row[ 2].rstrip(), aggregatbez[row[2]] if row[2] in aggregatbez else "",
				row[ 3].rstrip(), kapitelbez[row[3]] if row[3] in kapitelbez else "",
				row[ 4].rstrip(),
				row[ 5].rstrip(), gruppenbez[row[5]] if row[5] in gruppenbez else "",
				row[ 6].rstrip(), gruppenbez[row[6]] if row[6] in gruppenbez else "",
				row[ 7].rstrip(), gruppenbez[row[7]] if row[7] in gruppenbez else "",
				row[ 8].rstrip(), titelbez[row[8]] if row[8] in titelbez else "",
				row[ 9].rstrip(),
				row[10].rstrip(),
				row[11].rstrip(),
				row[12].rstrip(), funktionsbez[row[12]] if row[12] in funktionsbez else "",
				row[13].rstrip(), 
				row[14].rstrip(),
				row[15].rstrip(),
				row[16].rstrip(),
				row[19].rstrip(),
				row[22].rstrip(), sonderkennzbez[row[22]] if row[22] in sonderkennzbez else "",
				row[23].rstrip(),
				row[24].rstrip(),
				row[25].rstrip(),
				row[26].rstrip(),
				row[27].rstrip(),
				row[29].rstrip(),
				"2011"
			]
			output += [record2010]
			output += [record2011]
		else:
			skip = False

with open('outfile.csv', 'wb') as of:
	writer = csv.writer(of, delimiter=",", quotechar='"')
	for row in output:
		writer.writerow(row)
