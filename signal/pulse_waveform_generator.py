"""
pulse_waveform_generator.py
IX-Golden-Trump-Card 🃏

Generates synchronized 3-phase pulse waveforms at real-world harmonic test frequencies.
This script interfaces with any 3-channel capable DAC (e.g., Analog Discovery, Digilent WaveForms, LabJack, or audio card split with buffer) or simulation software (e.g., MATLAB, LTSpice).

Author: Bryce Wooster
License: MITRA Open Hardware License (see LICENSE)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ----- CONFIGURABLE PARAMETERS -----
frequency_hz = 1_000_000  # 1 MHz
sampling_rate = 50_000_000  # 50 MHz sampling for clean waveform
duration_s = 0.002  # 2 milliseconds total signal time
amplitude = 1.0  # peak amplitude in volts
waveform_type = 'sine'  # options: 'sine', 'square', 'triangle'
phase_offsets_deg = [0, 120, 240]  # Phase angles for clips 1, 2, 3
# -----------------------------------

# Derived values
t = np.arange(0, duration_s, 1/sampling_rate)
omega = 2 * np.pi * frequency_hz

# Generate waveforms
def generate_waveform(phase_deg):
    phase_rad = np.deg2rad(phase_deg)
    if waveform_type == 'sine':
        return amplitude * np.sin(omega * t + phase_rad)
    elif waveform_type == 'square':
        return amplitude * signal.square(omega * t + phase_rad)
    elif waveform_type == 'triangle':
        return amplitude * signal.sawtooth(omega * t + phase_rad, 0.5)
    else:
        raise ValueError("Invalid waveform type")

channel_1 = generate_waveform(phase_offsets_deg[0])
channel_2 = generate_waveform(phase_offsets_deg[1])
channel_3 = generate_waveform(phase_offsets_deg[2])

# Plotting
plt.figure(figsize=(12, 5))
plt.title("IX-Golden-Trump-Card 🃏 – 3-Phase Pulse Injection Waveforms")
plt.plot(t * 1e6, channel_1, label="Clip 1 – 0°", color='red')
plt.plot(t * 1e6, channel_2, label="Clip 2 – 120°", color='green')
plt.plot(t * 1e6, channel_3, label="Clip 3 – 240°", color='blue')
plt.xlabel("Time (µs)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Optional: export to CSV or DAC if hardware is connected (implement per device)
# Future expansion: real-time DAC output, USB/serial interface
