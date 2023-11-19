import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
import pyaudio
import wave
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
from threading import Timer


class Violin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('violin.ui', self)

        # Подключаем кнопки
        self.Recording.clicked.connect(self.record_bt)
        self.Graf.clicked.connect(self.graf_bt)
        self.Exit.clicked.connect(self.exit_bt)

        # Группируем кнопки выбора струны
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButton, 1)
        self.button_group.addButton(self.radioButton_2, 2)
        self.button_group.addButton(self.radioButton_3, 3)
        self.button_group.addButton(self.radioButton_4, 4)

        self.radioButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self, button):
        pass

    def clean_label(self):
        self.label_2.setText('')

    def record_bt(self):
        num_string = self.button_group.checkedId()
        timer = Timer(3, self.clean_label)
        # Записываем звук
        filename = "recorded.wav"
        chunk = 1024
        format = pyaudio.paInt16
        channels = 1
        sample_rate = 44100
        record_seconds = 5
        p = pyaudio.PyAudio()
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
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        # Анализируем звуковой файл
        wf = wave.open('recorded.wav', 'rb')
        swidth = wf.getsampwidth()
        rate = wf.getframerate()
        window = np.blackman(chunk)
        p = pyaudio.PyAudio()
        stream = p.open(format=
                        p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=rate,
                        output=True)

        data = wf.readframes(chunk)
        list_ch = []
        while len(data) == chunk * swidth:
            indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), data)) * window
            fft_data = abs(np.fft.rfft(indata)) ** 2
            which = fft_data[1:].argmax() + 1
            if which != len(fft_data) - 1:
                y0, y1, y2 = np.log(fft_data[which - 1:which + 2:])
                x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
                freq = (which + x1) * rate / chunk
                list_ch.append(freq)
            else:
                freq = which * rate / chunk
                list_ch.append(freq)
            data = wf.readframes(chunk)
        if data:
            stream.write(data)
        stream.close()
        p.terminate()

        if num_string == 1:
            if max(list_ch) < 658:
                self.label_2.setText('Подтяните струну')
            elif max(list_ch) > 660:
                self.label_2.setText('Ослабьте струну')
            else:
                self.label_2.setText('Струна настроена')
            timer.start()
        elif num_string == 2:
            if max(list_ch) < 439:
                self.label_2.setText('Подтяните струну')
            elif max(list_ch) > 441:
                self.label_2.setText('Ослабьте струну')
            else:
                self.label_2.setText('Струна настроена')
            timer.start()
        elif num_string == 3:
            if max(list_ch) < 293:
                self.label_2.setText('Подтяните струну')
            elif max(list_ch) > 295:
                self.label_2.setText('Ослабьте струну')
            else:
                self.label_2.setText('Струна настроена')
            timer.start()
        elif num_string == 4:
            if max(list_ch) < 195:
                self.label_2.setText('Подтяните струну')
            elif max(list_ch) > 197:
                self.label_2.setText('Ослабьте струну')
            else:
                self.label_2.setText('Струна настроена')
            timer.start()
        else:
            self.label_2.setText('Выберите струну')
            timer.start()

    def graf_bt(self):  # Вывод графика
        freq, sound = scipy.io.wavfile.read("recorded.wav")
        dur = len(sound) / freq
        time = np.arange(0, dur, 1 / freq)

        plt.plot(time, sound)
        plt.ylabel('высота тона')
        plt.xlabel('время')
        plt.show()

    def exit_bt(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Violin()
    ex.show()
    sys.exit(app.exec())
