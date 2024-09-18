# 03 Migration zu verteiltem System
Die Migration hin zu verteilten Systemen ist meist mit der Umstrukturierung der Applikation verbunden. Dabei müssen die Teile identifiziert werden, die eine logische Einheit bilden und diese voneinander so weit wie möglich entkoppelt werden. Üblicherweise liegen in monolithischen Systemen enge Kupplungen zwischen logisch getrennten Teilen vor. Für die Migration hin zu verteilten Systemen müssen die engen Kupplungen gelöst und durch klar definierte Schnittstellen ersetzt werden. Sollen die Teile auch "zeitlich" voneinander entkoppelt werden, können Systeme, wie beispielsweise ein Message Broker, zum Einsatz kommen.

## Beispiel
Es liegt ein Lagerhaltungssystem vor, dass auf dem Rechner des Lageristen installiert wurde. Das Lagerhaltungssystem gibt dem Lageristen die Möglichkeit, nach Produkten innerhalb des Lagers zu suchen, neue Produkte dem Lager hinzuzufügen oder Produkte aus dem Lager entfernen. Um die Software an unterschiedliche Lager-Situationen anpassen zu können, lassen sich auch die Anzahl der Regale und Ebenen (sprich die Lagerpositionen) verwalten.

Als Monolith ist Datenhaltung und Logik alles in einer Applikation enthalten. Wenn die Applikation nun auf eine verteilte Applikation umgebaut werden soll, müssen erst die logisch zusammengehörenden Einheiten erkannt werden. Im vorliegenden Beispiel wären dies:
* Lagerpositionen (inkl. Datenhaltung)
* Produktverwaltung (inkl. Produktdaten)
* Logging der Lagerbewegungen (inkl. Logdaten)
  * Einbuchen von angelieferten Produkten
  * Ausbuchen von ausgelieferten Produkten
  * Verändern der Lagerposition von bestehenden Produkten
* Suche nach Produkten

Wichtig bei verteilten Systemen ist, dass die Daten und die Logik die zusammengehört in der Regel gemeinsam losgelöst werden. Üblicherweise werden deshalb mehrere Datenbanken angelegt (Für Lagerpositionen, Produktdaten, Logdaten und gegebenenfalls Suchhistorie jeweils eine). Die Datenbanken und auch die Logik-Teile werden dadurch kleiner und überschaubarer. 

Wichtig: Die Aufteilung ist nur ein möglicher Vorschlag. Die Applikation könnte auch noch weiter bzw. anders unterteilt werden. Es gibt nicht die eine richtige Lösung. Manchmal werden auch Teile vorerst zusammen gelassen und erst später aufgetrennt. So könnte beispielsweise die Lagerposition auch enthalten, welches Produkt aktuell auf Ihr gelagert wird. Es könnte aber auch auf dem Produkt gespeichert werden, auf welcher Lagerposition es sich befindet. Es wäre aber auch denkbar, dass die Information, wo sich ein Produkt befindet, als eigene logische Einheit umgesetzt werden könnte (oder sogar bei der Suche untergebracht würde).

Wie der Monolith aufgeteilt wird, ist abhängig von den Präferenzen der Entwickler, aber auch von den Wünschen des Kunden oder der Strukturierung der Daten selbst. Es gibt hier kein "Patentrezept", dass für die Aufteilung angewendet werden kann, sondern muss von Fall zu Fall entschieden werden.