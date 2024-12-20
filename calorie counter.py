import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QComboBox

def calculate_calories(age, gender, weight, height, activity_level):
    bmr = 0

    # Расчет базового метаболизма в зависимости от пола
    if gender.upper() == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Для мужчин
    elif gender.upper() == 'F':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161  # Для женщин

    # Учет уровня физической активности
    if activity_level == '1, Малоподвижный образ жизни':  # Малоподвижный образ жизни
        return bmr * 1.2
    elif activity_level == '2, Легкие физические нагрузки':  # Легкие физические нагрузки
        return bmr * 1.375
    elif activity_level == '3, Умеренные физические нагрузки':  # Умеренные физические нагрузки
        return bmr * 1.55
    elif activity_level == '4, Сильные физические нагрузки':  # Сильные физические нагрузки
        return bmr * 1.725
    elif activity_level == '5, Очень сильные физические нагрузки':  # Очень сильные физические нагрузки
        return bmr * 1.9
    else:
        return bmr  # Если уровень активности не указан

class CalorieCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Расчёт калорий")

        # Создание виджетов
        self.age_label = QLabel("Возраст (лет):")
        self.age_entry = QLineEdit()

        self.gender_label = QLabel("Пол:")
        self.male_radio = QRadioButton("Мужской")
        self.female_radio = QRadioButton("Женский")
        self.male_radio.setChecked(True)

        self.weight_label = QLabel("Вес (кг):")
        self.weight_entry = QLineEdit()

        self.height_label = QLabel("Рост (см):")
        self.height_entry = QLineEdit()

        self.activity_level_label = QLabel("Уровень физической активности:")
        self.activity_level_combo = QComboBox()
        self.activity_level_combo.addItems(['1, Малоподвижный образ жизни', '2, Легкие физические нагрузки', '3, Умеренные физические нагрузки', '4, Сильные физические нагрузки', '5, Очень сильные физические нагрузки'])

        self.submit_button = QPushButton("Рассчитать")
        self.submit_button.clicked.connect(self.submit_button_clicked)

        #Добавление стилей
        self.setStyleSheet("""
            QLabel {
                   font-size: 12px;
                   color: purple;
                   text-align: center;
                   padding: 10px; 
                   background-color: lightgrey;                  
            }

            QWidget {
                    background-color: lightgrey;                           
                           }               

            QPushButton {
                    color: purple;
                    background-color: lightgrey;                                           
            }

            QComboBox {
                    background-color: white;                    
                    color: purple;
                                  } 

            QLineEdit {
                    background-color: white;  
                    color: purple;     
                           }                                  
                                        """)

        # Установка layout
        layout = QVBoxLayout()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_entry)
        
        layout.addWidget(self.gender_label)
        layout.addWidget(self.male_radio)
        layout.addWidget(self.female_radio)
        
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_entry)
        
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_entry)
        
        layout.addWidget(self.activity_level_label)
        layout.addWidget(self.activity_level_combo)
        
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def show_result(self, total_calories):
        result_text = (
            f"Необходимое количество калорий для поддержания веса: {total_calories:.2f} ккал.\n"
            f"Рекомендуемое количество калорий для завтрака: {(total_calories * 0.25):.2f} ккал."
        )
        QMessageBox.information(self, "Результат", result_text)

    def submit_button_clicked(self):
        try:
            age = int(self.age_entry.text())
            gender = 'M' if self.male_radio.isChecked() else 'F'
            weight = float(self.weight_entry.text())
            height = float(self.height_entry.text())
            activity_level = self.activity_level_combo.currentText()

            total_calories = calculate_calories(age, gender, weight, height, activity_level)
            self.show_result(total_calories)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Проверьте введенные значения.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalorieCalculator()
    calculator.show()
    sys.exit(app.exec_())

