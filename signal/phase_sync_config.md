# 🔄 Phase Synchronization Guide – IX-Golden-Trump-Card 🃏

This file explains how to achieve the required **120° phase offset** across the 3 ring contact clips using real-world signal generators, pulse boards, or analog timing hardware.

Correct phase offset is essential for **rotational Tesla-style harmonic injection** and to enable field convergence into the foil substrate.

---

## 🎛️ Target Phase Configuration

| Channel | Assigned Clip | Phase Offset |
|---------|----------------|--------------|
| CH1     | Clip 1         | 0°           |
| CH2     | Clip 2         | +120°        |
| CH3     | Clip 3         | +240°        |

The signal should repeat with exact symmetry in every full cycle. At 1 MHz, this means:

- One full cycle = 1 µs
- 120° phase shift = **333 nanoseconds**
- 240° phase shift = **666 nanoseconds**

---

## ⚙️ Method 1: Using 3-Channel Function Generator (Preferred)

If your signal generator supports:
- 3 independent outputs
- Phase configuration per channel

Steps:
1. Set all 3 channels to:
   - Frequency = 1 MHz
   - Amplitude = 3.3–5.0 V peak-to-peak
   - Waveform = sine (or triangle)
   - Output impedance = 50Ω

2. Apply phase offsets:
   - CH1 = 0°
   - CH2 = 120°
   - CH3 = 240°

3. Connect each channel to the corresponding ring clip.

---

## ⚙️ Method 2: Using Single Channel + Delay Line Logic (Fallback)

If you only have 1 output channel:
- Use logic delay ICs (e.g., 74HC4040, 74LS90) or analog delay lines
- Chain output to create shifted replicas

Example:
- Output → Ring Clip 1 directly
- Output → RC delay → Ring Clip 2 (approx. 333ns)
- Output → two-stage RC delay → Ring Clip 3 (approx. 666ns)

### RC Delay Formula:
\[
\tau = R \times C
\]

To achieve ~333ns:
- R = 3.3kΩ, C = 100pF (τ ≈ 330ns)

⚠️ This method is sensitive to component tolerance. Use precision caps and test with an oscilloscope if possible.

---

## ⚙️ Method 3: Software-Based Sync with GPIO or USB DAC

Use Python, MATLAB, or Arduino to:
- Generate 3 PWM or DAC outputs
- Offset each waveform in software by inserting delay into waveform array

Requirements:
- Synchronization via shared clock
- Output speed ≥ 5x target frequency for fidelity

Reference script: `/signal/pulse_waveform_generator.py`

---

## 🧪 Testing Your Phase Sync

Use an oscilloscope with at least 2 channels:
- Connect CH1 and CH2 to scope inputs
- Confirm consistent delay of 333ns between zero crossings
- Repeat for CH1 vs CH3 (should see 666ns delay)
- All waveforms must overlap in frequency and amplitude

If waveforms drift or oscillate inconsistently:
- Check for ground loops
- Shorten wire lengths
- Ensure signal source impedance is matched to clip leads

---

## 🧠 Result

Correct phase sync ensures that each ring clip injects energy in a **Tesla-style rotating vector**, not in-phase interference.

This rotational input causes field curvature at the gold-foil interface, initiating resonance entrainment and field behavioral transfer.

Now continue to `/signal/optional_thz_interface.md` if exploring direct phonon resonance injection.
