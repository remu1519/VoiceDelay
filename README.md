# Voice Delay Application

## Overview

The Voice Delay Application is a desktop application that adds a delay to real-time audio input and outputs it. Users can freely set the delay time, and the recorded audio will be played back after the specified delay time.

## Features

- **Delay Time Adjustment**: Set delays ranging from 0.5 seconds to 5.0 seconds.
- **Simple GUI**: An intuitive user interface that's easy to operate.
- **Real-Time Processing**: Real-time delayed playback of audio.

## Operating Environment

- **Operating System**: Windows, macOS, Linux
- **Python Version**: Python 3.x
- **Required Libraries**:
  - `pyaudio`
  - `tkinter` (usually included with Python)

## Installation Instructions

1. **Install Python 3.x**: Download it from the official website.

2. **Install Required Libraries**:

   ```bash
   pip install pyaudio
   ```

   > **Note**: If you encounter errors during the installation of `pyaudio`, please refer to the following additional steps.

   - **For Windows**:
     1. Download the appropriate `whl` file for your Python version from the [official PyAudio wheel files](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
     2. Install it using the downloaded file:
        ```bash
        pip install path/to/the/downloaded/file.whl
        ```

   - **For macOS**:
     ```bash
     brew install portaudio
     pip install pyaudio
     ```

## How to Use

1. **Download the Script**: Download `voice_delay_app.py` from this repository.

2. **Run the Script**:

   ```bash
   python voice_delay_app.py
   ```

3. **Operating the Application**:

   - The application window will appear.
   - Adjust the slider to set the delay time (0.5 seconds to 5.0 seconds).
   - Click the **"Start"** button to begin delayed audio playback.
   - Click the **"Stop"** button to stop the delayed playback.

## Notes

- **Beware of Audio Loops**: If the sound output from the speakers is picked up by the microphone, it may cause feedback (howling). It is recommended to use a headset or earphones.
- **Volume Settings**: Please set the volume appropriately. If the volume is too high, it may cause sound distortion or feedback.

## License

This project is released under the MIT License.

## Contribution

Bug reports and suggestions for feature improvements are welcome. We look forward to your Issues and Pull Requests.

## Acknowledgments

Thank you for using this application. We welcome your feedback and comments.
