simple image generator with DiffusionPipeline
```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from stable_diffusion import DiffusionPipeline

class ImageGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.prompt_label = QLabel('Enter your prompt:', self)
        self.prompt_label.move(20, 20)

        self.prompt_input = QLineEdit(self)
        self.prompt_input.move(20, 50)
        self.prompt_input.resize(280, 40)

        self.generate_button = QPushButton('Generate Image', self)
        self.generate_button.move(20, 100)
        self.generate_button.clicked.connect(self.generate_image)

        self.image_label = QLabel(self)
        self.image_label.move(20, 150)
        self.image_label.resize(280, 280)

        self.setGeometry(100, 100, 320, 450)
        self.setWindowTitle('Stable Diffusion Image Generator')
        self.show()

    def generate_image(self):
        prompt = self.prompt_input.text()
        pipe = DiffusionPipeline()
        image = pipe(prompt).images
        image.save('result.jpg')
        pixmap = QPixmap('result.jpg')
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageGenerator()
    sys.exit(app.exec_())
```