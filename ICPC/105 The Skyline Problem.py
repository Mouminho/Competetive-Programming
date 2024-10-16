import sys
"""
wir erstellen 5 listen 
"""
skyline = [0] * 1000000
"""
list 'skyline' ist eine liste mit 1000000 index, wobei jedes index entspricht eine x stelle, der wert eines index ist der ensprechende
y wert dieses index
"""
start = [0] * 10000
"""
liste 'start' der länge 10000 speichert am index i den startpunkt von gebäude i (line i)
"""
height = [0] * 10000
"""
liste 'height' der länge 10000 speichert am index i die höhe von gebäude i (line i)
"""
end = [0] * 10000
"""
liste 'end' der länge 10000 speichert am index i den endtpunkt von gebäude i (line i)
"""
resault = []
"""
leere liste 'resault' zum speichern der Ausgabe
"""
max_index = 0
"""
max_index entpricht die maximale breite also die letzte benötigte x stelle wegen endlosschleifen
"""
i= 0
"""
i entspricht gebäude i (line i)
"""
while True:
    """
    while schleife zur aktualisierung der listen: 'start, height & end' und zur bestimmung der maximal benötigte x stellen
    die werte werden aus stdin ausgelesen und mit den initialisierten werten verglichen
    """
    line = sys.stdin.readline().strip()
    if not line:
        break
    start[i], height[i], end[i] = map(int, line.split()) 
    for j in range(start[i], end[i]):
        if height[i] > skyline[j]: 
            skyline[j] = height[i]
    if end[i] > max_index:
        max_index = end[i]
    i += 1
index = 0
"""
index i zwischen 0 und maximale x stelle 
"""
for i in range(max_index + 1):
    """
    for schleife zum einfügen der werte in der liste 'resault'
    hier werden die indexes und deren y werten nacheinander hinzugefügt unter der bedingung dass eine änderung an diesem index gibt
    """
    if skyline[i] != index:
        resault.append(i) 
        resault.append(skyline[i]) 
        index = skyline[i]
    sys.stdout.write(str(resault[0]))
    for i in range(1, len(resault)):
        """
        for schleife zur Ausgabe der elemente aus liste 'resault'
        """
        sys.stdout.write(" " + str(resault[i]))
    sys.stdout.write("\n")
###