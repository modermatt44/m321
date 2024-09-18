# Auftrag Schnittstellenbeschreibung
[TOC]

## Lernziele
Wie in der [Theorie](./README.md) gelernt, werden Schnittstellen heutzutage üblicherweise in maschinenlesbaren standardisierten Sprachen beschrieben und nicht mehr als Textbeschreibung wie früher üblich. Ziel ist es, dass Sie aus einer gegebenen Schnittstellenbeschreibung (so wie früher in Textform) eine Schnittstellendefinition in GraphQL und OpenAPI erstellen. Ziel dabei ist es, den Aufbau von GraphQL und OpenAPI zu verstehen und auf eigene Schnittstellen im Berufsalltag anwenden zu können.

## Rahmenbedingungen
* **Sozialform:** Einzelarbeit oder zu Zweit (Tandem-Arbeit)
* **Dauer:** 45 Min (1 Lektionen)

## Auftrag
Gegeben ist folgende Schnittstellendefinition (mit der freundlichen Unterstützung durch ChatGPT):

Stellen Sie sich eine API für eine Bibliotheksverwaltung vor. Diese API ermöglicht es, Bücher und Autoren zu verwalten. Die API bietet Funktionen, um Bücher hinzuzufügen, zu aktualisieren, zu löschen und Details über Bücher abzurufen. Ebenso können Autoren hinzugefügt, aktualisiert und abgerufen werden. Jedes Buch ist mit einem oder mehreren Autoren verknüpft.

### Anforderungen:

1. **Bücher:**
   * **Abrufen aller Bücher:** Eine Liste aller Bücher in der Bibliothek.
   * **Abrufen eines Buches nach ID:** Detaillierte Informationen zu einem bestimmten Buch, einschliesslich Titel, Beschreibung, Veröffentlichungsjahr und der zugehörigen Autoren.
   * **Erstellen eines neuen Buches:** Ein neues Buch mit Titel, Beschreibung, Veröffentlichungsjahr und Autoren hinzufügen.
   * **Aktualisieren eines Buches:** Die Details eines bestehenden Buches aktualisieren.
   * **Löschen eines Buches:** Ein Buch aus der Bibliothek entfernen.

2. **Autoren:**
   * **Abrufen aller Autoren:** Eine Liste aller Autoren in der Bibliothek.
   * **Abrufen eines Autors nach ID:** Detaillierte Informationen zu einem bestimmten Autor, einschliesslich Name, Geburtsdatum und Liste der geschriebenen Bücher.
   * **Erstellen eines neuen Autors:** Einen neuen Autor mit Name und Geburtsdatum hinzufügen.
   * **Aktualisieren eines Autors:** Die Details eines bestehenden Autors aktualisieren.

### Vorgehen
1. Wählen Sie das Schnittstellendefinitionsformat (GraphQL oder OpenAPI), mit dem Sie Ihre erste Schnittstellendefinition umsetzen möchten.
2. Wandeln Sie die oben gegebene Beschreibung in Ihr gewähltes Schnittstellendefinitionsformat um. Recherchieren Sie dazu zuerst über den Aufbau des gewählten Formats und halten Sie Ausschau nach allfälligen Beispielen. Um einen schnellen Einstieg zu finden, können Sie sich auch durch eine generative KI den Text oben in ihr gewähltes Format umwandeln lassen. Vergleichen Sie dann aber unbedingt die generierte Schnittstellendefinition mit dem Prosa-Text und auch mit den Regeln des gewählten Schnittstellendefinitionsformats. Hat die KI alles richtig gemacht? Oder müssen Sie noch nachbessern?
3. Nehmen Sie zur Validierung Ihrer Schnittstellendefinition auch einen Validator zur Hilfe, der Ihnen die Schnittstellendefinition auf korrekte Syntax prüfen kann.
4. Wandeln Sie nun die Schnittstellendefinition von Ihrem anfangs gewählten Format in das noch verbleibende Format um. Wenn Sie beispielsweise eine GraphQL-Definition erstellt haben, dann wandeln Sie diese in OpenAPI um. Wenn die Definition in OpenAPI vorliegt, dann machen Sie daraus eine GraphQL-Definition.
5. Vergleichen Sie die Unterschiede zwischen den beiden Formaten. Welches Format finden Sie persönlich besser? Wieso?

### Challenge (optional) - Ausprobieren von Tools zur Codegenerierung
Implementieren Sie die Schnittstelle aufgrund der erstellten Schnittstellendefinition. Suchen Sie dafür nach geeigneten Tools, die Ihnen aus GraphQL oder OpenAPI für die Programmiersprache Ihrer Wahl ein Grundgerüst an Code generieren. Wenden Sie die Tools auf Ihre Schnittstellendefinition an und vergleichen Sie, welches der Tools für Ihre Zwecke am besten geeignet ist. Halten Sie Ihre Erkenntnisse fest, um diese später im Berufsalltag wiederverwenden zu können. 

### Abgabe
Die Lehrperson wird Sie darüber informieren ob bzw. wie Sie diese Übungsaufgabe abgeben sollten.