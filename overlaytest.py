import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QLinearGradient

class OverlayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Get the screen size
        screen_rect = self.geometry()
        width = screen_rect.width()
        height = screen_rect.height()

        # Define the glow color and width
        glow_color = QColor(162, 0, 255)  # Purple with full opacity
        glow_width = 10  # Adjust this value to change the width of the glow

        # Create and draw gradients for each edge
        self.draw_edge_gradient(painter, 0, 0, width, glow_width, Qt.Vertical)  # Top edge
        self.draw_edge_gradient(painter, 0, height - glow_width, width, glow_width, Qt.Vertical, True)  # Bottom edge
        self.draw_edge_gradient(painter, 0, 0, glow_width, height, Qt.Horizontal)  # Left edge
        self.draw_edge_gradient(painter, width - glow_width, 0, glow_width, height, Qt.Horizontal, True)  # Right edge

    def draw_edge_gradient(self, painter, x, y, width, height, orientation, reverse=False):
        gradient = QLinearGradient()
        if orientation == Qt.Vertical:
            gradient.setStart(x, y)
            gradient.setFinalStop(x, y + height)
        else:
            gradient.setStart(x, y)
            gradient.setFinalStop(x + width, y)

        if reverse:
            gradient.setColorAt(0, QColor(162, 0, 255, 0))
            gradient.setColorAt(1, QColor(162, 0, 255, 100))
        else:
            gradient.setColorAt(0, QColor(162, 0, 255,100))
            gradient.setColorAt(1, QColor(162, 0, 255, 0))

        painter.fillRect(QRect(x, y, width, height), gradient)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayWidget()
    sys.exit(app.exec_())