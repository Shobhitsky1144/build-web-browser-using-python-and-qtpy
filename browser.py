import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Create the QWebEngineView
        self.view = QWebEngineView()
        self.view.load(QUrl("https://www.google.com"))

        # Create the URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.browse)

        # Create the back button
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.view.back)

        # Create the forward button
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.view.forward)

        # Create the refresh button
        self.refresh_button = QPushButton("⟳")
        self.refresh_button.clicked.connect(self.view.reload)

        # Create the layout
        layout = QVBoxLayout()
        nav_bar = QHBoxLayout()
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.forward_button)
        nav_bar.addWidget(self.refresh_button)
        nav_bar.addWidget(self.url_bar)
        layout.addLayout(nav_bar)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def browse(self):
        url = QUrl(self.url_bar.text())
        self.view.load(url)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
