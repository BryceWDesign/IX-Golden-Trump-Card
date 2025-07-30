# 🧲 Ring Contact Alignment Guide – IX-Golden-Trump-Card 🃏

This file defines the exact physical contact parameters and spatial tolerances for the 3 silver+gold micro clips that interface with the 24k gold ring in the IX-Golden-Trump-Card 🃏 system. Correct alignment and pressure are critical to achieve stable harmonic transfer without contact loss, overcompression, or vibrational instability.

---

## 📏 Contact Positioning Geometry

- **Clip Count**: 3
- **Distribution**: Equidistant 120° spacing around the ring circumference
- **Ring Size Reference**: U.S. Size 9 (Internal diameter ≈ 18.89mm)

### 📐 Recommended Positional Pattern:

| Clip Position | Clock Face Reference | Approx. Angular Location |
|---------------|----------------------|----------------------------|
| Clip 1        | 12 o’clock           | 0°                         |
| Clip 2        | 4 o’clock            | 120°                       |
| Clip 3        | 8 o’clock            | 240°                       |

- All clips should touch **both**:
  - The **outer circumference** of the ring  
  - The **foil surface** directly beneath the ring  
  - This forms a triangular phase injection matrix

---

## 🧪 Contact Physics: Force, Material Behavior, and Surface Prep

- **Target Contact Pressure**: ~40–80g of force per clip  
  - Enough to maintain uninterrupted contact  
  - Not enough to deform or dent the gold surface

- **Surface Cleanliness**:
  - Clean ring surface with **99% isopropyl alcohol** prior to contact  
  - Do not polish with abrasives — microstructural integrity is critical for resonance transfer
  - Use anti-static gloves to prevent oil or charge contamination

- **Contact Width at Tip**: ≤1.6mm (1/16 cm)  
  - Ensure clip jaws are **smooth and parallel**, not serrated  
  - Serrated clips disrupt field uniformity and generate phase artifacts

- **Gold Ring**:
  - Must be pure (24k), uncoated, unalloyed  
  - Any inscription or engraving will disrupt symmetry — use a blank ring only

---

## ⚡ Field Behavior Sensitivity

Small misalignments at the contact points can cause:
- Loss of phase lock across the clip triangle
- Field deformation across the foil surface
- Instability during waveform ramp-up
- Delayed resonance convergence

To minimize this:
- Use calipers to verify equal clip spacing within ±0.5mm
- Visually confirm all 3 clips touch both foil and ring simultaneously before powering on
- If a clip shifts during operation, shut down and realign before continuing

---

## 🧠 Best Practices

| Practice | Outcome |
|----------|---------|
| Use tripod stand or clip holders to stabilize contacts | Prevents ring shift from wire weight |
| Mark foil beneath ring lightly with template | Ensures ring is centered every time |
| Test continuity with DMM at each clip before operation | Confirms all contact points are live |
| Observe symmetry in waveform reflection (if scope is available) | Confirms phase balance and correct contact |

---

## ✅ Result

When all three clip contacts are aligned:
- A balanced harmonic injection field is established at the foil-ring interface
- Resonance propagation forms with minimal energy loss
- Gold’s field behavior can begin transferring into the aluminum foil substrate in real-time

Incorrect spacing or unstable clip geometry will result in incomplete entrainment and should be corrected before activating signal injection.

Proceed to `/hardware/foil_prep.md` to prepare the substrate correctly.
