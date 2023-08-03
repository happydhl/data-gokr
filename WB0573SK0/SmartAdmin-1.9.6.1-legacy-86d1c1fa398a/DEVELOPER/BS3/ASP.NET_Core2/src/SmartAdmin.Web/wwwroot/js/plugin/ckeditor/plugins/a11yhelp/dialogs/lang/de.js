﻿/*
 Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
CKEDITOR.plugins.setLang("a11yhelp",
    "de",
    {
        title: "Barrierefreiheitinformationen",
        contents: "Hilfeinhalt. Um den Dialog zu schliessen die Taste 'ESC' drücken.",
        legend: [
            {
                name: "Allgemein",
                items: [
                    {
                        name: "Editor Symbolleiste",
                        legend:
                            "Drücken Sie ${toolbarFocus} auf der Symbolleiste. Gehen Sie zur nächsten oder vorherigen Symbolleistengruppe mit TAB und SHIFT-TAB. Gehen Sie zur nächsten oder vorherigen Symbolleiste auf die Schaltfläche mit dem RECHTS- oder LINKS-Pfeil. Drücken Sie die Leertaste oder Eingabetaste, um die Schaltfläche in der Symbolleiste aktivieren."
                    },
                    {
                        name: "Editor Dialog",
                        legend:
                            "Innerhalb des Dialogs drücken Sie TAB um zum nächsten Dialogfeld zu gelangen, drücken Sie SHIFT-TAG um zum vorherigen Feld zu wechseln, drücken Sie ENTER um den Dialog abzusenden und ESC um den Dialog zu abzubrechen. Um zwischen den Reitern innerhalb eines Dialogs zu wechseln drücken sie ALT-F10. Um zum nächsten Reiter zu gelangen können Sie TAB oder die rechte Pfeiltaste. Zurück gelangt man mit SHIFT-TAB oder der linken Pfeiltaste. Mit der Leertaste oder Enter kann man den Reiter auswählen."
                    },
                    {
                        name: "Editor Kontextmenü",
                        legend:
                            "Dürcken Sie ${contextMenu} oder die Anwendungstaste um das Kontextmenü zu öffnen. Man kann die Pfeiltasten zum Wechsel benutzen. Mit der Leertaste oder der Enter-Taste kann man den Menüpunkt aufrufen. Schliessen Sie das Kontextmenü mit der ESC-Taste."
                    },
                    {
                        name: "Editor Listen",
                        legend:
                            "Innerhalb einer Listenbox kann man mit der TAB-Taste oder den Pfeilrunter-Taste den nächsten Menüeintrag wählen. Mit der Shift-TAB Tastenkombination oder der Pfeilhoch-Taste gelangt man zum vorherigen Menüpunkt. Mit der Leertaste oder Enter kann man den Menüpunkt auswählen. Drücken Sie ESC zum Verlassen des Menüs."
                    },
                    {
                        name: "Editor Elementpfadleiste",
                        legend:
                            "Drücken Sie ${elementsPathFocus} um sich durch die Pfadleiste zu bewegen. Um zum nächsten Element zu gelangen drücken Sie TAB oder die Pfeilrechts-Taste. Zum vorherigen Element gelangen Sie mit der SHIFT-TAB oder der Pfeillinks-Taste. Drücken Sie die Leertaste oder Enter um das Element auszuwählen."
                    }
                ]
            }, {
                name: "Befehle",
                items: [
                    { name: "Wiederholen Befehl", legend: "Drücken Sie ${undo}" },
                    { name: "Rückgängig Befehl", legend: "Drücken Sie ${redo}" }, {
                        name: "Fettschrift Befehl",
                        legend: "Drücken Sie ${bold}"
                    }, { name: "Italic Befehl", legend: "Drücken Sie ${italic}" },
                    { name: "Unterstreichung Befehl", legend: "Drücken Sie ${underline}" },
                    { name: "Link Befehl", legend: "Drücken Sie ${link}" },
                    { name: "Symbolleiste zuammenklappen Befehl", legend: "Drücken Sie ${toolbarCollapse}" },
                    {
                        name: "Zugang bisheriger Fokussierung Raumbefehl ",
                        legend:
                            "Drücken Sie ${accessPreviousSpace}  auf den am nächsten nicht erreichbar Fokus-Abstand vor die Einfügemarke zugreifen: zwei benachbarte HR-Elemente. Wiederholen Sie die Tastenkombination um entfernte Fokusräume zu erreichen. "
                    },
                    {
                        name: "Zugang nächster Schwerpunkt Raumbefehl ",
                        legend:
                            "Drücken Sie $ { accessNextSpace }, um den nächsten unerreichbar Fokus Leerzeichen nach dem Cursor zum Beispiel auf: zwei benachbarten HR Elemente. Wiederholen Sie die Tastenkombination zum fernen Fokus Bereiche zu erreichen. "
                    }, { name: "Eingabehilfen", legend: "Drücken Sie ${a11yHelp}" }
                ]
            }
        ]
    });
