# loopback-capture-sample
Sample code which records system sounds (what you hear) in Python.

# Demo
[![](https://img.youtube.com/vi/7xQAhQWhLHs/0.jpg)](https://www.youtube.com/watch?v=7xQAhQWhLHs)

# Environments
This worked on Windows 10/11 and Ubuntu 18.04.

# Installation
1. Clone this repository
2. Go to the the directory you have just cloned
3. On Linux, you need to install libsndfile using your distribution’s package manager like apt in order to use SoundFile library
4. Run the following command (On Windows, I recommnend using [the current master branch of SoundCard](https://github.com/bastibe/SoundCard) because the released SoundCard has a bug related to Windows. Check [this issue I opend](https://github.com/bastibe/SoundCard/issues/166) for more infomation.)
```bash
pip install -r requirements.txt
```

# Usage
1. Before running the program, start outputting sound from the device`s speaker or headphones so that the program can record that sound.
2. Run the program as below.
```bash
python capture.py
```

3. After seconds, the program produces an audio file named out.wav.
4. Check if the program could record system sounds by playing out.wav.
