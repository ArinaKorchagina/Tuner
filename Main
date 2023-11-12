import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
import pyaudio
import wave
from playsound import playsound
from threading import Timer


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Project.ui', self)

        # Подключаем кнопку звук
        self.Sound.clicked.connect(self.sound_bt)
        # Подключаем кнопку запись
        self.Recording.clicked.connect(self.record_bt)
        # Подключаем кнопки выбора струны

        # Группируем кнопки выбора струны
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButton, 1)
        self.button_group.addButton(self.radioButton_2, 2)
        self.button_group.addButton(self.radioButton_3, 3)
        self.button_group.addButton(self.radioButton_4, 4)
        self.button_group.addButton(self.radioButton_5, 5)
        self.button_group.addButton(self.radioButton_6, 6)

        self.radioButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self, button):
        pass

    def clean_label(self):
        self.label_2.setText('')

    def sound_bt(self):
        num_string = self.button_group.checkedId()
        if num_string == 1:
            playsound('string1.mp3')
        elif num_string == 2:
            playsound('string2.mp3')
        elif num_string == 3:
            playsound('string3.mp3')
        elif num_string == 4:
            playsound('string4.mp3')
        elif num_string == 5:
            playsound('string5.mp3')
        elif num_string == 6:
            playsound('string6.mp3')
        else:
            self.label_2.setText('Выберите струну')
            timer = Timer(3, self.clean_label)
            timer.start()

    def record_bt(self):
        # имя файла для записи
        filename = "recorded.wav"
        # установить размер блока в 1024 сэмпла
        chunk = 1024
        # образец формата
        FORMAT = pyaudio.paInt16
        # моно, если хотите стере измените на 2
        channels = 1
        # 44100 сэмплов в секунду
        sample_rate = 44100
        record_seconds = 5
        # initialize PyAudio object
        p = pyaudio.PyAudio()
        # открыть объект потока как ввод и вывод
        stream = p.open(format=pyaudio.paInt16,
                        rate=44100,
                        channels=1,
                        input_device_index=1,  # вы можете изменить индекс вашей входной звуковой карты
                        input=True,
                        output=False,
                        frames_per_buffer=1024)
        frames = []
        print("Recording...")
        for i in range(int(44100 / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        print("Finished recording.")
        # остановить и закрыть поток
        stream.stop_stream()
        stream.close()
        # завершить работу объекта pyaudio
        p.terminate()
        # сохранить аудиофайл
        # открываем файл в режиме 'запись байтов'
        wf = wave.open(filename, "wb")
        # установить каналы
        wf.setnchannels(channels)
        # установить формат образца
        wf.setsampwidth(p.get_sample_size(FORMAT))
        # установить частоту дискретизации
        wf.setframerate(sample_rate)
        # записываем кадры как байты
        wf.writeframes(b"".join(frames))
        # закрыть файл
        wf.close()

    def calc(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
