import numpy as np
import pyaudio


def sine(volume, fs, duration, freq):
    p = pyaudio.PyAudio()
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32).tobytes()
    output_bytes = (volume * samples)#.tobytes()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    stream.write(output_bytes)
    stream.close()
    p.terminate()


