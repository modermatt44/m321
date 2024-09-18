# 04 Datenhaltung
[TOC]

## Einleitung
Wie die Datenhaltung in einem verteilten System realisiert wird, hängt stark von den Anforderungen an die Datenhaltung und von der Struktur der Daten ab. Folgende Faktoren sind für die Wahl einer sinnvollen Datenhaltung relevant:
* **Verfügbarkeit**: Müssen die Daten hochverfügbar (HA - High Availability) sein oder ist es nicht weiter tragisch, wenn der Knoten, der die Daten speichert, vorübergehend ausfällt? Je nachdem wird ein Cluster-System für die Datenhaltung (für HA) oder ein übers Netzwerk erreichbarer Speicher eingesetzt. Grundsätzlich ist ein Netzwerkspeicher einfacher einzurichten und zu verwalten.
* **Art / Struktur der Daten**: Insbesondere wenn es sich um temporäre Daten handelt, macht es allenfalls Sinn, diese lokal zu speichern und nicht in ein entferntes System zu bringen. Die lokale Speicherung sorgt für kürzere Latenzzeiten beim Lesen und Schreiben von Daten.

Abhängig von den Anforderungen gibt es mehrere Möglichkeiten, wie und wo Daten gespeichert werden können. Die folgenden Kapitel konkretisieren diese Möglichkeiten und geben Beispiele welche Technologien dabei zum Einsatz kommen können.

## Datenhaltung auf Netzwerkspeicher
Wenn die Datenhaltung nicht hochverfügbar sein muss, dann bietet sich eine Netzwerkspeicherlösung für die Speicherung der Daten an. Im Prinzip handelt es sich bei einem Netzwerkspeicher um eine auf einem Dateiserver freigegebenes Netzlaufwerk, das in anderen Systemen (Windows / Linux) als Netzlaufwerk eingebunden werden kann.

Konkret bedeutet dies, dass die Systemkomponente ihre Daten im gemounteten Netzlaufwerk ablegt. Das verwendete Protokoll für das Mounten des Netzlaufwerks sorgt anschliessend dafür, dass die Daten auf den entfernten Dateiserver kopiert bzw. von dort heruntergeladen werden.

Die folgenden Protokolle / Technologien kommen im Bereich von Netzwerkspeicher häufig vor:
* **SMB (server message block):** Wurde durch Microsoft geprägt. Ist auch unter dem Begriff Samba bekannt und ist für Linux-Systeme vorhanden. 
* **CIFS (common internet file system):** Ist eine veraltete Version bzw. Abspaltung von SMB und sollte heute nur noch in Ausnahmefällen eingesetzt werden. Anstatt CIFS sollte SMB (wenn möglich in der aktuellsten Version) zum Einsatz kommen.
* **NFS (network file system):** Ist eine Alternative zu SMB. Der Fokus liegt aber weniger auf der Freigabe von Ressourcen im Allgemeinen, sondern eher Freigaben vom Dateisystem. SMB im Vergleich zu NFS kann auch beispielsweise Drucker freigeben (nicht nur Files).
* **iSCSI (internet Small Computer System Interface):** Wird häufig im Zusammenhang mit NAS (Network Attached Storage) oder SAN (Storage Area Network) als Protokoll für die Freigabe des Netzwerkspeichers verwendet. iSCSI arbeitet auf Blocklevel. D. h. der Speicher wird als Blockdevice wie eine physische Festplatte freigegeben. Geräte die iSCSI nutzen müssen auf den Speicher - ähnlich wie bei einer Festplatte - erst ein Filesystem (Partition) darauf instanziieren, um konkrete Files lesen und speichern zu können. Üblicherweise wird iSCSI im zusammenhang mit dem Speichern von Festplattenabbildern von virtuellen Maschinen (VM's) verwendet.

Möchten Sie sich hier weiter zu den Unterschieden vertiefen, finden Sie unter Quellen weiterführende Links und Artikel, die weitere Details zu den unterschiedlichen Protokollen beschreiben.

## Datenhaltung in Cluster-Filesystem (inkl. Failover)
Bei einem Cluster-Filesystem handelt es sich um ein Dateisystem welches gegen aussen als eine logische Einheit auftritt. Im Hintergrund werden die Daten aber auf mehreren physisch getrennten Servern abgelegt und unter diesen Synchron gehalten.

Ziel eines Cluster-Filesystems ist die Hochverfügbarkeit der Daten. Ein weiteres Ziel ist die Skalierbarkeit des Filesystems. Dadurch, dass die Daten auf mehrere Knoten im Cluster verteilt werden (mehrere Kopien der Daten), kann ein Node im Cluster ausfallen, ohne dass das Gesamtsystem dadurch ausfallen würde. Weil auf mehreren Knoten Kopien der Daten vorliegen, können viele gleichzeitige Zugriffe auf die verschiedenen Nodes im Cluster verteilt werden (Lastenverteilung). Somit lässt sich das System einfach skalieren.

### Split Brain Problematik
Im Falle eines Ausfalls eines Knotens (auf Englisch Node) oder auch der Verbindungen zwischen Knoten kann es zu einer sogenannten "split brain"-Situation kommen. Wenn beispielsweise ein Cluster mit zwei Knoten vorliegt und die Netzwerkverbindung zwischen den beiden Knoten ([Cluster Interconnect](https://de.wikipedia.org/wiki/Cluster_Interconnect)) ausfällt, aber nicht die Netzwerkverbindung zu den Benutzern, dann denkt jeder der beiden Knoten, der andere Knoten wäre ausgefallen. Wenn Benutzer nun weiter auf beide Knoten ihre Daten schreiben (hinzufügen, entfernen, verändern), dann laufen die Datenbestände auseinander, weil Schreibvorgänge auf den einen Knoten nicht mehr auf den anderen Knoten repliziert werden. Dadurch entsteht ein inkonsistenter Datenbestand (beide Knoten sehen nur die eigenen Änderungen an den Daten aber nicht die des anderen Knotens im Cluster). Nachdem die Verbindung zwischen den beiden Knoten wiederhergestellt wird, müssten die Daten wieder zu einem konsistenten Zustand zusammengeführt werden. Automatisiert ist dies jedoch nicht möglich. Es wäre eine manuelle Arbeit und deshalb mit unverhältnismässig hohem Aufwand verbunden.

Um die Problematik zu umgehen, gibt es die folgenden Lösungsansätze:
* **Mehr als 50% der Knoten sichtbar:** Wenn ein Ausfall passiert, dann darf der Cluster bzw. der Clusterteil nur dann seinen Dienst weiter anbieten, wenn er noch mehr wie 50% aller im Cluster befindlichen Knoten erreichen kann. Wenn beispielsweise 5 Knoten in einem Cluster existieren und der Cluster bricht in zwei Teile (einmal 2 Knoten und einmal 3 Knoten), dann steht nur noch der Teil des Clusters mit 3 Knoten (3/5 aller bestehenden Nodes im Cluster sichtbar) weiterhin zur Verfügung für die Nutzung. Die 2 anderen Knoten übernehmen dann den Datenbestand der Dreiergruppe, sobald die Verbindung wiederhergestellt werden konnte. Der Fachbegriff für diese Art der Problemlösung ist [Quorum](https://de.wikipedia.org/wiki/Quorum_(Informatik)).
* **Auslastung der Cluster-Teile**: Die Auslastung der noch verfügbaren Clusterteile (bzw. die Auslastung vor dem Ausfall - also dort hin wo die meisten Verbindungen hin offen waren), kann ebenfalls als Kriterium verwendet werden um zu entscheiden, welcher Teil des Clusters weiterlaufen darf.
* **Witness host:** Es kann ein zusätzlicher Host (der Zeuge) ausserhalb des Clusters platziert werden, der die Metadaten des Clusters enthält und diesen von aussen überwacht und bei einem Split-Brain-Szenario entscheidet, welcher Teil des Clusters weiterleben darf. VMWare verwendet diesen [Lösungsansatz](https://core.vmware.com/blog/understanding-vsan-witness-host) bei deren System (vSAN).

Quelle & weitere Details: https://de.wikipedia.org/wiki/Split_Brain_(Informatik)

### Open Source Cluster-Filesysteme
Es existieren verschiedene Opensource-Cluster-Filesysteme. Hier eine Auswahl von drei Systemen:
* **HDFS (Hadoop Distributes File System):** Genauer Apache hadoop genannt. Das FS gibt es seit 2005. Vor allem Google war mit vielen Beiträgen dazu involviert und wird hauptsächlich im Zusammenhang mit Big Data und maschinellem Lernen eingesetzt ([Quelle & Details](https://de.wikipedia.org/wiki/Apache_Hadoop)).
* **Ceph-Cluster:** Seit 2012 am Markt. Gilt seit 2016 als Stabil. Zu dem Filesystem haben Organisationen wie Canonical (die Entwickler von Ubuntu), CERN, Cisco, Fujitsu, Intel, RedHat, SanDisk und SUSE beigetragen([Quelle & Details](https://de.wikipedia.org/wiki/Ceph)).
* **GlusterFS:** Seit 2006 am Markt und Ende 2011 von RedHat gekauft ([Quelle & Details](https://de.wikipedia.org/wiki/GlusterFS))

Um diese Cluster-Filesystem-Lösungen einfach lokal installieren und ausprobieren zu können, gibt es verschiedene Vagrant-Vorlagen, die von der Community entwickelt und zur Verfügung gestellt wurden. In der Übungsaufgabe [Cluster Dateisystem](./Cluster-Dateisystem.md) können Sie eines der vorgestellten Open Source Cluster-Filesysteme ausprobieren.

## Datenhaltung im Zusammenhang mit Docker / Kubernetes
Wenn Daten im Zusammenhang mit Containern persistent gespeichert werden sollen, geschieht dies über sogenannte volumes. Volumes bedienen sich der im Absatz [Datenhaltung auf Netzwerkspeicher](#datenhaltung-auf-netzwerkspeicher) (weiter oben auf dieser Seite) kennen gelernten Fileshare-Protokolle. Dabei werden die Volumes im Filesystem des Containers via Mounts eingehängt und so aus Sicht des Containers "lokal" zugreifbar gemacht. Die Protokolle schauen im Hintergrund dann, dass die Daten entsprechend auf den entfernten Rechner übertragen bzw. von da gelesen werden.

Weitere Details im Zusammenhang mit der Verwendung von Volumes können Sie im [Modul 347](https://gitlab.com/ch-tbz-it/Stud/m347/) unter [Volumes](https://gitlab.com/ch-tbz-it/Stud/m347/-/blob/main/Container/docker/Volumes.md) nachlesen / repetieren.

## Quellen / Weiterführende Informationen
### Zu Datenhaltung auf Netzwerkspeicher
* https://www.computerweekly.com/de/definition/Common-Internet-File-System-CIFS: Artikel der die Zusammenhänge bzw. Unterschiede zwischen SMB und CIFS erklärt.
* https://aws.amazon.com/de/compare/the-difference-between-nfs-and-cifs/: Artikel von Amazon der die Zusammenhänge bzw. Unterschiede von NFS und CIFS erklärt.
* https://wiki.ubuntuusers.de/Samba_Server/: Der Artikel erklärt wie SMB (Samba) unter Linux installiert und verwendet wird.
* https://de.wikipedia.org/wiki/Storage_Area_Network: Wikipedia-Artikel der erklärt was ein SAN (Storage Area Network) ist.
* https://docs.linuxfabrik.ch/topics/nfs-vs-iscsi.html: Erklärt den Unterschied zwischen iSCSI und NFS.

### Zu Cluster-Dateisystemen
* https://de.wikipedia.org/wiki/Cluster_Interconnect: Verbindung zwischen Clustern
* https://de.wikipedia.org/wiki/Split_Brain_(Informatik): Artikel zu Split Brain Thematik in Clustern
* https://core.vmware.com/blog/understanding-vsan-witness-host: Artikel der vSAN mit witness-Host erklärt
* https://docs.ceph.com/en/reef/rados/: Dokumentation zum Ceph Cluster FS
* https://hadoop.apache.org/: Offizielle Seite für Apache Hadoop Cluster FS
* https://www.gluster.org/: Offizielle Seite für GlusterFS Cluster FS