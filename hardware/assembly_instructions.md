# 🛠️ Assembly Instructions – IX-Golden-Trump-Card 🃏

These instructions define the exact assembly procedure for the IX-Golden-Trump-Card 🃏 field transference system. Build precision is essential — clip spacing, material handling, and foil integrity all influence resonance fidelity.

No glue, solder, adhesives, or chemical processes are used. This is a **clean, physical contact and frequency-injection platform**.

---

## 📐 Step-by-Step Assembly Guide

### Step 1: Prepare the Base and Foil

- Place the **non-conductive baseplate** (acrylic, wood, or ceramic) on a vibration-stable surface.
- Cut a **30.5cm × 30.5cm** square of aluminum foil (standard Reynolds Wrap). Use scissors, not hands, to avoid micro-crinkling.
- Carefully **flatten the foil** on the base. No folds, waves, or punctures. Use anti-static gloves.
- Optionally tape foil corners with **non-conductive tape** for stability (Kapton or Scotch tape).

---

### Step 2: Mount the Outer (Foil) Clips

- Attach 4x **silver + 24k gold-plated standard clips** to the **4 corners of the foil**.
  - Placement: ~5mm in from each corner.
  - Ensure **firm but non-crushing** grip. Avoid tearing foil.
- Route clip leads away from the center, evenly spaced to avoid field imbalance.
- If grounding the foil: connect **one of these clips to chassis ground** on a floating or shielded bench.

---

### Step 3: Center the 24k Gold Ring

- Place the **24k gold ring** in the **exact center of the foil**.
  - Orientation: Ring should lie flat (horizontal).
  - Ensure full **unbroken surface contact** between ring and foil — no stacking, tilting, or loose gaps.
- Do not secure the ring with adhesive. Physical contact and pressure will stabilize it during operation.

---

### Step 4: Place the Inner Triad Clips on Ring

- Take 3x **micro alligator clips** (silver core, gold-plated, 1/16 cm tip width).
- Position them at **evenly spaced 120° intervals** around the ring:
  - First clip: reference "12 o’clock" position.
  - Second clip: rotate clockwise to "4 o’clock".
  - Third clip: "8 o’clock".
- Each clip should **touch both the outer edge of the ring and the foil surface simultaneously** — forming an equilateral triangle of contact symmetry.
- Use calipers or compass for geometric accuracy:
  - Target spacing between clips: **exactly 12.8mm** (based on ring diameter ~18.9mm)
  - Placement error margin: ±0.5mm

---

### Step 5: Connect Signal Wires

- Each of the 3 micro clips connects to a **dedicated output channel** on your function generator or pulse driver.
  - CH1 → Clip 1 (0° phase)
  - CH2 → Clip 2 (120° phase offset)
  - CH3 → Clip 3 (240° phase offset)
- If using analog driver boards, ensure **synchronized pulse logic with phase offset manually tuned**.

---

### Step 6: Final Pre-Operation Checks

- Confirm:
  - No shorting between clips
  - Foil is flat and intact
  - All clips are secure but not damaging foil or ring
  - No bare conductor wire contacts the foil outside designated clips
- Optional: Photograph or diagram layout before energizing for documentation

---

## 🔄 Operational Notes

- Once assembled, **do not move the foil, ring, or base** during operation. Resonance lock relies on geometric alignment.
- Keep all external RF sources away (WiFi routers, phones, etc.)
- Operate in a thermally stable, EM-quiet room if possible.
- Do not run the system for more than 10 minutes continuously unless you have thermal imaging tools monitoring foil behavior.

---

## 🧠 Next Step

Once physically assembled, proceed to `/signal/pulse_waveform_generator.py` for configuring the harmonic input.

System is now mechanically aligned. Do not attempt signal injection until waveform generation is properly set up.

—  
Bryce Wooster  
IX-Golden-Trump-Card 🃏 Project  
