# Übungsaufgabe Cluster-Dateisystem
[TOC]

## Lernziele
Sie vertiefen, was Sie im Kapitel [02 Lokale Entwicklungsumgebung](../02%20Lokale%20Entwicklungsumgebung) über Vagrant gelernt haben in der praktischen Anwendung. Sie lernen ein ausgewähltes Cluster-Dateisystem (Ceph, GlusterFS oder HDFS - [siehe Theorie](./README.md#datenhaltung-in-cluster-filesystem-inkl-failover)) näher kennen, indem Sie es lokal installieren (mehrere VMs via Vagrant-Setup) und ausprobieren.

## Rahmenbedingungen
* **Sozialform:** Einzelarbeit, Tandem oder Dreiergruppe
* **Dauer:** 90-135 Min (2-3 Lektionen)

## Auftrag
### Zielzustand
Am Ende der Übung sollten Sie einen 3-Node-Cluster mit Ceph, GlusterFS oder HDFS (ein System wählen - nicht alle drei... wäre zu aufwendig) aufgebaut haben. Ebenso soll eine Client-VM vorhanden sein, die diesen Cluster verwenden kann. Schreiben Sie als "Proof of concept" Files auf diesen Cluster und lesen Sie davon. Testen Sie (bei genügend Reservezeit oder falls Sie gerne Zuhause noch etwas daran machen möchten) auch wie der Cluster reagiert, wenn Sie einen der Nodes herunterfahren.

**Hinweis:** installieren Sie den Cluster auf Ihrem lokalen Rechner. Die VM im LernMAAS hat zu wenig RAM um 4 VMs parallel zu betreiben. Sollte Ihr Rechner auch zu wenig Leistung haben können Sie sich auch zu dritt zusammenschliessen. Jeder installiert auf seiner VM einen Node. Die drei LernMAAS-VMs verbinden Sie dann zu einem Cluster. Ihr lokales Arbeitsgerät nehmen Sie als Client um auf das Cluster-Dateisystem zuzugreifen.

### Vorgehen
Um den Zielzustand zu erreichen, gibt es zwei mögliche Wege:
1. Setup und Konfiguration aller VMs von Hand. Vorteil: Sie wissen am Ende genau was Sie gemacht haben - Fehler in Setup-Scripts aus Anleitungen, inkompatible Versionen, seltsame Fehlermeldungen, sind unwahrscheinlicher. Nachteil: Sie haben vermutlich etwas mehr selbst zu tun bevor Sie den Cluster ausprobieren können.
2. Setup und Konfiguration mithilfe von Vagrant oder anderen Orchestrierungslösungen. Vorteil: Sie starten nicht bei Null, sondern haben Anleitungen, die für andere offensichtlich mal geklappt haben. Nachteil: Sie verlassen sich auf den Code Anderer. D. h. der Code der bei anderen mit anderen Software-Versionen lief, muss bei Ihnen nicht unbedingt laufen. Eindenken in den Code Anderer, Debuggen und Optimieren vom Code der Anderen wird vermutlich nötig sein.

Sowohl für den 1. als auch den 2. Weg gibt es Anleitungen für jeden der drei Cluster-Dateisysteme im Internet. Einige Anleitungen sind unten (geordnet nach Cluster-Dateisystem) gegeben. Diese Liste ist jedoch nicht abschliessend. Die Anleitungen sind alle nicht optimal (meist veraltet). Sollten Sie bei eigenen Recherchen auf bessere Anleitungen stossen, senden Sie bitte Ihrer Lehrperson den Link zu der Anleitung zu, damit dieser in dieser Übungsaufgabe ergänzt werden kann.

Die Übungsaufgabe kann in folgende Arbeitsschritte unterteilt werden:
1. Wählen Sie ein Cluster-Dateisystem aus, mit welchem Sie Ihren Cluster aufbauen wollen.
2. Recherchieren Sie zum gewählten Cluster - eventuell finden Sie eine besser passende Anleitung.
3. Wählen Sie eine Anleitung nach der Sie das Cluster-Dateisystem aufsetzen möchten.
4. Folgen Sie der Anleitung, notieren Sie allfällige Probleme und deren Lösung bis Sie den lauffähigen Cluster in Betrieb genommen haben.
5. Schreiben Sie einige Testdaten vom Client auf das Cluster-Dateisystem.
6. Fahren Sie einen Node im Cluster herunter. Können Sie die Daten noch lesen? Können Sie diese editieren und löschen?
7. Fahren Sie einen zweiten Node herunter. Was passiert jetzt? Können Sie die Daten noch lesen / schreiben?
8. Starten Sie alle heruntergefahrenen Nodes wieder. Verbinden Sie sich automatisch wieder mit dem Cluster? Funktioniert der Cluster automatisch wieder wie gewohnt oder müssen noch zusätzliche Aktionen ausgeführt werden?
9. Challenge (optional): Details siehe [unten](./Cluster-Dateisystem.md#challenge-optional).

#### Ceph-Cluster
* https://github.com/carmstrong/multinode-ceph-vagrant: etwas veraltet (letzter commit im 2020), benötigt Vagrant-Plugins (die nicht mehr weiterentwickelt werden)

#### GlusterFS
* https://github.com/halkyon/glusterfs-vagrant: etwas veraltet (letzter commit im 2021), braucht keine speziellen Vagrant-Plugins
* https://github.com/carmstrong/multinode-glusterfs-vagrant: Etwas aktuellere Anleitung, jedoch wird das deprecated vagrant-cachier-Plugin verwendet

#### HDFS (Hadoop Distributed File System)
* https://community.cloudera.com/t5/Community-Articles/Spinning-up-Hadoop-HDP-cluster-on-local-machine-using/ta-p/246431: Artikel ok... allerdings etwas viele Einzelschritte (hätte mit Vagrant automatisiert werden können)
* https://github.com/ssalat/vagrant-hadoop-cluster: letzter Commit aus dem Jahr 2015
* https://medium.com/@jaryya/a-compilation-of-the-best-infrastructure-as-code-tools-81dae56a4c4a: neueren Datums (aus 2023) aber komplett veraltete Linux-Versionen im Einsatz


### Challenge (optional)
Die Anleitungen im Netz sind etwas in die Jahre gekommen. Helfen Sie der Informatiker-Gemeinschaft, indem Sie selbst eine Anleitung schreiben und / oder Ihr optimiertes Vagrantfile, dass bei Ihnen für das Setup des Cluster-Dateisystems funktioniert hat öffentlich zur Verfügung stellen. Die Idee ist, dass wir als Klasse unseren Beitrag dazu leisten, dass die Anleitungen für die Installation von Cluster-Dateisystemen wieder etwas aktueller wird.

Wenn Sie wünschen, dass die TBZ Ihre Anleitung in GitLab in den Modulunterlagen zur Verfügung stellt, geben Sie diese bitte der Lehrperson ab.