# EwX: TraceGrid — Tetrahedral Pyramid Sweep Localization

This module implements a novel algorithm for estimating the 3D position of radio signal sources using a drone performing a **pyramid sweep trajectory**.

The drone flies along **six triangular faces of a tetrahedral pyramid**, allowing signal measurements from multiple geometrically distinct angles. The algorithm then computes the intersection of signal vectors and estimates the target's location in 3D space.

---

## 🚀 Highlights

- Estimate target position with only **one moving drone**
- No need for synchronized multi-station systems
- Uses azimuth and elevation from MUSIC or any DOA engine
- Geometry-inspired approach with **6-surface vertical tetrahedron**

---

## 🧠 How it works

1. Drone performs a predefined sweep over **6 triangle faces** of an upside-down tetrahedron.
2. In each triangle, the drone pauses at 3 positions and records azimuth/elevation from signal processing.
3. Each triangle becomes a "mini-array" to estimate a target vector.
4. All 6 estimates are averaged to get a robust final 3D position.

---

## 🔧 Functions

### `generate_tetrahedral_sweep(base_radius, height)`
Returns a list of 6 triangular faces (each with 3 points) defining the sweep trajectory.

### `triangulated_sweep_localization(freq, points, spectra)`
Estimates a 3D target vector from one triangle face using az/el directions.

### `tetrahedral_sweep_localization(freq, sweep_faces, spectra_list)`
Computes and averages all 6 triangulated localizations to determine final position.

---

## 📦 Example

```python
sweep_faces = generate_tetrahedral_sweep()
spectra_list = [ [...az/el tuples...] for each face ]
position = tetrahedral_sweep_localization(freq, sweep_faces, spectra_list)
```

---

## 🔬 Future directions

- Integrate IQ recording per point
- Visualize sweep volume and ray paths
- Apply weight confidence from signal power / SNR

---

## 🤝 Part of EwX: TraceGrid Project
This tool is a research component of the EwX ecosystem — an open-source Web3-based RF detection and security intelligence infrastructure.
