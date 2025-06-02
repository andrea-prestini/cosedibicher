import os
import sys
import csv
from fractions import Fraction
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QFileDialog,
    QSizePolicy,
    QFormLayout,
    QGridLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QProgressBar

# Workaround per macOS + uv + PyQt6
if sys.platform == "darwin":
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(
        sys.prefix,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
        "PyQt6",
        "Qt6",
        "plugins",
        "platforms",
    )


class ValoreAttesoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎲 Calcolatore di Valore Atteso")
        self.setGeometry(100, 100, 450, 400)

        self.esiti = []
        self.probabilita = []
        self.dark_mode = False

        self.init_ui()
        self.setStyleSheet("background-color: #f0f0f0;")

    def init_ui(self):
        layout = QVBoxLayout()

        self.descr_label = QLabel("Situazione:")
        self.descr_input = QLineEdit()
        self.descr_input.setMinimumHeight(30)

        form_layout = QGridLayout()
        self.valore_input = QLineEdit()
        self.valore_input.setPlaceholderText("Valore (€)")
        self.valore_input.setMinimumHeight(30)
        self.valore_input.returnPressed.connect(self.aggiungi_evento)

        self.prob_input = QLineEdit()
        self.prob_input.setPlaceholderText("Probabilità")
        self.prob_input.setMinimumHeight(30)
        self.prob_input.returnPressed.connect(self.aggiungi_evento)

        form_layout.addWidget(QLabel("Valore (€):"), 0, 0)
        form_layout.addWidget(self.valore_input, 0, 1)
        form_layout.addWidget(QLabel("Probabilità:"), 1, 0)
        form_layout.addWidget(self.prob_input, 1, 1)

        buttons_layout = QGridLayout()
        buttons_layout.setHorizontalSpacing(10)
        buttons_layout.setVerticalSpacing(10)
        buttons_layout.setContentsMargins(5, 10, 5, 10)

        self.aggiungi_btn = QPushButton("➕ Aggiungi")
        self.calcola_btn = QPushButton("✅ Calcola")
        self.resetta_btn = QPushButton("🔄 Reset")
        self.salva_btn = QPushButton("💾 Salva CSV")
        self.carica_btn = QPushButton("📂 Carica CSV")
        self.tema_btn = QPushButton("🌗 Tema Scuro/Chiaro")

        btns = [
            self.aggiungi_btn,
            self.calcola_btn,
            self.resetta_btn,
            self.salva_btn,
            self.carica_btn,
            self.tema_btn,
        ]

        for i, btn in enumerate(btns):
            btn.setMinimumHeight(35)
            btn.setStyleSheet("margin: 5px;")
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            buttons_layout.addWidget(btn, i // 3, i % 3)

        self.tabella = QTableWidget()
        self.tabella.setColumnCount(2)
        self.tabella.setHorizontalHeaderLabels(["Valore (€)", "Probabilità"])
        self.tabella.verticalHeader().setVisible(False)
        self.tabella.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.tabella.setMaximumHeight(120)
        self.tabella.setMinimumHeight(100)
        self.tabella.setColumnWidth(0, 120)
        self.tabella.setColumnWidth(1, 120)
        self.tabella.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.risultato_label = QLabel("")
        self.counter_label = QLabel("Eventi inseriti: 0")
        self.complemento_label = QLabel("Probabilità residua: 1.0000")

        self.aggiungi_btn.clicked.connect(self.aggiungi_evento)
        self.calcola_btn.clicked.connect(self.calcola_valore_atteso)
        self.resetta_btn.clicked.connect(self.resetta_tutto)
        self.salva_btn.clicked.connect(self.salva_csv)
        self.carica_btn.clicked.connect(self.carica_csv)
        self.tema_btn.clicked.connect(self.toggle_tema)
        self.tabella.cellChanged.connect(self.modifica_valore)

        layout.addWidget(self.descr_label)
        layout.addWidget(self.descr_input)
        layout.addLayout(form_layout)
        # Raggruppamento pulsanti
        gruppi_layout = QVBoxLayout()

        azioni_label = QLabel("Azioni dati:")
        stile_label = QLabel("Stile interfaccia:")

        dati_layout = QHBoxLayout()
        stile_layout = QHBoxLayout()

        for i, btn in enumerate(
            [self.aggiungi_btn, self.calcola_btn, self.resetta_btn]
        ):
            dati_layout.addWidget(btn)

        for i, btn in enumerate([self.salva_btn, self.carica_btn, self.tema_btn]):
            stile_layout.addWidget(btn)

        gruppi_layout.addWidget(azioni_label)
        gruppi_layout.addLayout(dati_layout)
        gruppi_layout.addWidget(stile_label)
        gruppi_layout.addLayout(stile_layout)

        layout.addLayout(gruppi_layout)
        layout.addWidget(self.tabella)
        layout.addWidget(self.counter_label)
        layout.addWidget(self.complemento_label)
        self.progress_label = QLabel("Progresso probabilità")
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_label.setStyleSheet("margin-top: 5px;")
        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress)
        layout.addWidget(self.risultato_label)

        self.setLayout(layout)

    def aggiorna_tabella(self):
        self.tabella.blockSignals(True)
        self.tabella.setRowCount(len(self.esiti))
        for i, (v, p) in enumerate(zip(self.esiti, self.probabilita)):
            self.tabella.setItem(i, 0, QTableWidgetItem(f"{v:.2f}"))
            self.tabella.setItem(i, 1, QTableWidgetItem(f"{p:.4f}"))
        self.tabella.blockSignals(False)
        self.counter_label.setText(f"Eventi inseriti: {len(self.esiti)}")
        self.aggiorna_complemento()

    def aggiungi_evento(self):
        try:
            valore = float(self.valore_input.text())
            prob_input = self.prob_input.text().strip()
            prob = (
                float(Fraction(prob_input)) if "/" in prob_input else float(prob_input)
            )
            if not (0 <= prob <= 1):
                raise ValueError
            if sum(self.probabilita) + prob > 1:
                QMessageBox.warning(
                    self,
                    "Errore",
                    "La somma delle probabilità supererebbe 1. Inserimento bloccato.",
                )
                return
            self.esiti.append(valore)
            self.probabilita.append(prob)
            self.valore_input.clear()
            self.prob_input.clear()
            self.aggiorna_tabella()
            self.aggiorna_complemento()
            self.valore_input.setFocus()
        except:
            QMessageBox.warning(
                self,
                "Errore",
                "Inserisci un valore numerico valido e una probabilità tra 0 e 1. Es: 0.25 o 1/4",
            )

    def modifica_valore(self, row, col):
        try:
            testo = self.tabella.item(row, col).text()
            valore = float(Fraction(testo)) if "/" in testo else float(testo)
            if col == 0:
                self.esiti[row] = valore
            else:
                if not (0 <= valore <= 1):
                    raise ValueError
                self.probabilita[row] = valore
        except:
            QMessageBox.warning(
                self,
                "Errore",
                f"Valore non valido in riga {row + 1}, colonna {col + 1}.",
            )
            self.aggiorna_tabella()

    def calcola_valore_atteso(self):
        if not self.esiti:
            self.risultato_label.setText("Nessun evento inserito.")
            return
        somma_prob = sum(self.probabilita)
        if abs(somma_prob - 1) > 1e-6:
            risposta = QMessageBox.question(
                self,
                "Normalizzare?",
                f"La somma delle probabilità è {somma_prob:.4f}. Vuoi normalizzarle?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if risposta == QMessageBox.StandardButton.No:
                return
            self.probabilita = [p / somma_prob for p in self.probabilita]
            self.aggiorna_tabella()
        valore_atteso = sum(e * p for e, p in zip(self.esiti, self.probabilita))
        descrizione = self.descr_input.text().strip()
        testo = (
            f"🎯 [{descrizione}] Valore atteso: {valore_atteso:.2f} €"
            if descrizione
            else f"🎯 Valore atteso: {valore_atteso:.2f} €"
        )
        self.risultato_label.setText(testo)

    def aggiorna_complemento(self):
        totale = sum(self.probabilita)
        complemento = 1.0 - totale
        self.complemento_label.setText(f"Probabilità residua: {complemento:.4f}")
        self.progress.setValue(min(int(totale * 100), 100))
        if complemento < 0:
            self.complemento_label.setStyleSheet("color: red;")
            self.progress.setStyleSheet(
                "QProgressBar::chunk { background-color: red; }"
            )
        elif complemento == 0:
            self.complemento_label.setStyleSheet("color: green;")
            self.progress.setStyleSheet(
                "QProgressBar::chunk { background-color: green; }"
            )
        else:
            self.complemento_label.setStyleSheet("color: black;")
            self.progress.setStyleSheet("")

    def resetta_tutto(self):
        self.esiti.clear()
        self.probabilita.clear()
        self.valore_input.clear()
        self.prob_input.clear()
        self.descr_input.clear()
        self.risultato_label.clear()
        self.tabella.setRowCount(0)
        self.counter_label.setText("Eventi inseriti: 0")

    def salva_csv(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Salva CSV", "valore_atteso.csv", "CSV files (*.csv)"
        )
        if filename:
            try:
                with open(filename, "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Valore (€)", "Probabilità"])
                    for v, p in zip(self.esiti, self.probabilita):
                        writer.writerow([v, p])
                QMessageBox.information(self, "Salvato", f"Dati salvati in: {filename}")
            except Exception as e:
                QMessageBox.warning(self, "Errore", f"Errore nel salvataggio: {e}")

    def carica_csv(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Carica CSV", "", "CSV files (*.csv)"
        )
        if filename:
            try:
                with open(filename, newline="") as f:
                    reader = csv.reader(f)
                    next(reader)
                    self.esiti.clear()
                    self.probabilita.clear()
                    for row in reader:
                        valore = float(row[0])
                        prob = float(row[1])
                        self.esiti.append(valore)
                        self.probabilita.append(prob)
                self.aggiorna_tabella()
            except Exception as e:
                QMessageBox.warning(
                    self, "Errore", f"Errore durante il caricamento: {e}"
                )

    def toggle_tema(self):
        if self.dark_mode:
            self.setStyleSheet("background-color: #f0f0f0; color: black;")
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #2b2b2b;
                    color: #e6e6e6;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #444;
                    border: 1px solid #666;
                    padding: 5px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
                QLineEdit, QTableWidget, QLabel {
                    background-color: #3c3c3c;
                    color: #ffffff;
                    border: 1px solid #666;
                }
                QProgressBar {
                    border: 1px solid #aaa;
                    border-radius: 3px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #00cc66;
                    width: 10px;
                }
            """)
        self.dark_mode = not self.dark_mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ValoreAttesoApp()
    window.show()
    sys.exit(app.exec())
