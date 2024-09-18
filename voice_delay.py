import pyaudio
import threading
import time
import tkinter as tk

class VoiceDelayApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Delay Application")

        self.delay_seconds = tk.DoubleVar(value=3.0)
        self.running = False

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="遅延秒数を設定してください:").pack(pady=5)

        self.delay_slider = tk.Scale(self.master, from_=0.5, to=5.0, resolution=0.1,
                                     orient=tk.HORIZONTAL, variable=self.delay_seconds)
        self.delay_slider.pack(pady=5)

        self.start_button = tk.Button(self.master, text="開始", command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text="停止", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(self.master, text="ステータス: 停止中")
        self.status_label.pack(pady=5)

    def start(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="ステータス: 実行中")
            threading.Thread(target=self.record_and_play).start()

    def stop(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="ステータス: 停止中")

    def record_and_play(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK)

        frames = []

        while self.running:
            data = stream.read(CHUNK)
            frames.append(data)

            # 遅延時間を経過したフレームを再生
            if len(frames) > int(RATE / CHUNK * self.delay_seconds.get()):
                stream.write(frames.pop(0), CHUNK)

        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceDelayApp(root)
    root.mainloop()
