# 02 Lokale Entwicklungsumgebung
[TOC]

## Ziele
Dieses Kapitel soll einen Überblick über die wichtigsten Tools und Technologien geben, die für die lokale Entwicklung zum Einsatz kommen.

## Grundsätze für die lokale Entwicklung
Um ein verteiltes System möglichst realitätsnah lokal testen zu können müssen die einzelnen Server / Systemkomponenten virtualisiert werden. Ebenso muss das Netzwerk virtualisiert werden. Aus Sicht der Systemkomponenten ist der Unterschied zwischen einem virtualisierten Netzwerk und einem physischen Netzwerk nicht zu erkennen. Dadurch wird es möglich, das Gesamtsystem, welches normalerweise über mehrere Rechner verteilt wird, auf einem Rechner zu virtualisieren.

Eine Voraussetzung für die Entwicklung von verteilten Systemen ist jedoch ein Rechner zu besitzen, der genügend Leistung bietet um mehrere Systeme parallel virtualisiert betreiben zu können. Je nach Grösse bzw. Performance-Anforderungen des Systems kann ein älteres bzw. nicht ganz so leistungsfähiges Gerät schnell an seine Grenzen stossen.

## Tools für die Virtualisierung
Um die verschiedenen Server bzw. Systemkomponenten auf dem Entwicklungsrechner betreiben zu können sind Tools für die Virtualisierung der Systemkomponenten nötig. Ein verteiltes System kann mit Containern oder mit virtuellen Maschinen (VM) betrieben werden.

### Engines für den Betrieb virtueller Maschinen (VM)
Der folgende Abschnitt befasst sich nur mit verteilten Systemen, die mit einzelnen Servern (VMs) realisiert wurden. Container werden im nächsten Kapitel behandelt.

Die folgende Tabelle ist nicht abschliessend, gibt aber einen Überblick über mögliche Software-Lösungen, die es erlauben VMs auf dem lokalen Rechner zu betreiben:

| Software             | Beschreibung                                                                                                                                                                                                                                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Oracle VM VirtualBox | VirtualBox ist eine weit verbreitete OpenSource-Lösung, die von Oracle gepflegt und weiterentwickelt wird.<br/>https://www.virtualbox.org/                                                                                                                                                                  |
| Hyper-V              | Ist von Microsoft und im Windows bereits mit integriert. Ab Windows 10 steht Hyper-V im System zur Verfügung.<br/>https://learn.microsoft.com/de-de/virtualization/hyper-v-on-windows/about/                                                                                                                |
| VMWare               | VMWare ist eine proprietäre Lösung, die aber weit verbreitet ist. VMWare war eines der ersten Unternehmungen überhaupt, die eine Engine für virtuellen Maschinen entwickelte und gilt auch heute noch als führend in dem Bereich (auch im Zusammenhang mit Clustering und VMs).<br/>https://www.vmware.com/ |
| KVM, QEMU            | KVM steht für Kernel-based Virtual Machine und QEMU für Quick Emulator. Beide werden häufig in Kombination und vor allem unter Linux eingesetzt. Die Unterschiede und das Zusammenspiel der beiden wird unter https://cloudzy.com/blog/qemu-vs-kvm/ erklärt.                                                |

Wird ein verteiltes System lokal für die Entwicklung aufgesetzt, dann bedeutet dies, dass alle VMs für alle vorhandenen und im Testing involvierten Systemkomponenten aufgebaut und richtig konfiguriert werden müssen. Dies kann unter Umständen ein relativ zeitintensives Unterfangen sein, sofern dies nicht automatisiert geschieht.

Für das automatisierte Setup der verschiedenen Systemkomponenten (VMs) in einem verteilten System kann beispielsweise Vagrant verwendet werden (Terraform wäre auch eine Möglichkeit, ist aber dann eher auf das deployment eines verteilten Systems auf der Produktivumgebung gedacht, weshalb wir Terraform hier nicht weiter betrachten). Bei Vagrant wird beschreibend angegeben, welche VMs und welche Netzwerke angelegt werden sollen. Es wird zudem angegeben welcher "Provider" für das Anlegen der VMs verwendet werden soll. Unter Provider versteht man, auf welcher VM-Engine die VMs und das Netzwerk zwischen den VMs aufgebaut werden soll. Wird beispielsweise VirtualBox als Provider verwendet, dann werden die VMs innerhalb von VirtualBox erstellt (bei Hyper-V analog in Hyper-V, etc.) und können im Anschluss auch über die VirtualBox-Oberfläche überprüft und verwaltet werden.

Viele Beispiele von Vagrant-Setup's sind unter https://gitlab.com/ch-tbz-it/Stud/m169/-/tree/main/vagrant zu finden. Im [Modul 169](https://gitlab.com/ch-tbz-it/Stud/m169) (gehört zum Lehrgang der Plattformentwickler) wird auf das Thema IaC (Infrastructure as Code) noch detaillierte eingegangen. Ein Blick in dieses Modul kann dann nützlich sein, wenn Sie sich im Umgang mit Vagrant (oder auch mit Terraform) weiter vertiefen möchten.

Bei der Übungsaufgabe unter [04 Datenhaltung](../04%20Datenhaltung/Cluster-Dateisystem.md) werden Sie Vagrant einsetzen, um die verschiedenen Server eines Cluster-Filesystems auf Ihrem lokalen Rechner als VMs automatisiert aufsetzen zu lassen.

### Containerumgebungen
Eine zweite Möglichkeit ist es nicht virtuelle Maschinen (VMs), sondern Container zu verwenden. Im [Modul 347](https://gitlab.com/ch-tbz-it/Stud/m347) haben Sie den Umgang mit Containern bereits ausführlich kennengelernt. Deshalb hier nur kurz zur Repetition eine Übersicht der relevanten Software / Technologien:
* Docker: Container-Engine (neben Docker gäbe es auch noch andere wie beispielsweise PodMan)
* Kubernetes: Orchestrierungslösung für Container. Diese gibt es in verschiedenen Varianten auch als "single-node"-Cluster für die lokale Entwicklung.

## Tools für das Testing von Schnittstellen
Im Zusammenhang mit der lokalen Entwicklung von Software ist auch ein schnelles Testing und Debugging wichtig. In nicht verteilten Applikationen wird üblicherweise mit Breakpoints gearbeitet. Gerade im Zusammenhang mit den verteilten Komponenten gibt es zusätzliche Herausforderungen. Eine Arbeit mit Breakpoints ist nicht unbedingt praktikabel. Denn wenn auf einer Systemkomponente bei einem Breakpoint gehalten wird, dann haben die anderen Systemkomponenten den Eindruck, dass die im Debugging befindliche Systemkomponente nicht mehr reagiert - obwohl dies in Tat und Wahrheit nicht zutrifft. Dadurch reagiert das Umsystem unter Umständen anders, wie wenn nicht debugged wird. Es gibt auch weitere Herausforderungen (beispielsweise Timing - nicht alle Systeme haben die gleiche Uhrzeit). Weitere Details werden erst im Kapitel [08 Monitoring und Logging, Testing und Debugging](../08%20Monitoring%20und%20Logging,%20Testing%20und%20Debugging) besprochen.

Wichtig für die lokale Entwicklung und die Einrichtung der Entwicklungsumgebung zu wissen ist jedoch, dass es für das Debugging verteilter System Lösungsansätze gibt. Neben Lösungsansätzen wie dennoch mit Breakpoints gearbeitet werden kann, gibt es auch Ansätze, dass die Systemkomponenten selbst Logfiles Ihrer Aktivitäten schreiben. Es existieren Softwarelösungen, um die Logfiles mehrerer Komponenten parallel anzeigen zu lassen. Es gibt auch die Möglichkeit "on demand" ein Logging oder eine Debugging-Ausgabe anzuschalten auf einer Systemkomponente die gerade Untersucht werden soll. Nicht alle Lösungen sind für alle Programmiersprachen geeignet oder passen für Ihren konkreten Anwendungsfall. Deshalb hilft hier nur "selbst recherchieren", welche Lösung für Sie am besten passt. Aber wichtig: es gibt für praktisch alles eine Lösung. Eine kurze Suche wie in Ihrem Fall unter Einsatz der durch Sie gewählten Technologien am besten getestet wird, kann hilfreich sein.

Im Zusammenhang mit dem Datenaustausch - also um konkrete Schnittstellen zu testen - gibt es eigene Tools die auch bei der lokalen Entwicklung eingesetzt werden können. Diese werden im Kapitel [05 Datenaustausch](../05%20Datenaustausch) behandelt.

<!--
Notizen (work in progress):
Remote Debugger -> Breakpoints in IDE setzen und mit Remote Debugger verbinden (wenn Deployment von Code auf entfernten Rechner geht)
https://www.jetbrains.com/help/idea/tutorial-remote-debug.html
https://learn.microsoft.com/en-us/troubleshoot/developer/visualstudio/debuggers/troubleshooting-remote-debugging
https://code.visualstudio.com/docs/editor/debugging
...

Debugging von Problemen unter Last

http://inet.haw-hamburg.de/teaching/ws-2019-20/verteilte-systeme-1/07_verteiltesdebugging.pdf

Unterschiedliche Latenzen -> Timing-Probleme

Breakpoint auf einem System bewirkt das anderes System denkt, das eine System wäre tot... ob wohl es noch am Leben ist. Dadurch andere reaktion durch Umsysteme möglich
//-->


## Zugriff auf LernMAAS ![](MAAS_Logo_without_text.png "Ubuntu MAAS")
Das LernMAAS bietet Ihnen eine bereits vorinstallierte Arbeitsumgebung auf einer Linux-VM. Diese werden wir im Rahmen der Projektarbeit (LB2) einsetzen. Es erhält jeder Lernende eine eigene VM. Auf dieser setzt er seine Systemkomponente des verteilten Systems auf und verbindet diese mit den andern Systemteilen der anderen Gruppenmitglieder.

Die Lehrperson wird Ihnen für die Einrichtung von WireGuard und die Zuteilung Ihrer VM entsprechend die Zugangsdaten zukommen lassen. Eine Beschreibung was das LernMAAS grundsätzlich ist und eine Hands-On-Übung wie Sie den Zugriff testen und die Zugangsdaten für sich abändern können, finden Sie unter https://gitlab.com/ch-tbz-it/Stud/m347/-/tree/main/LernMAAS. Bitte stellen Sie möglichst bald sicher, dass der Zugriff auf Ihre VM klappt, um optimal auf den Start der LB2 vorbereitet zu sein und bei allfälligen Problemen noch genügend Zeitreserve zu haben, diese zu lösen.