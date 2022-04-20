import soundcard as sc
import soundfile as sf

output_file_name = "out.wav"    # file name.
samplerate = 48000              # [Hz]. sampling rate.
record_sec = 5                  # [sec]. duration recording audio.

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=samplerate) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=samplerate*record_sec)
    
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=output_file_name, data=data[:, 0], samplerate=samplerate)