# EwX Drone-Mounted RF Module: Technical Specifications (v0.1)

## 📡 Purpose
Lightweight, autonomous direction-finder for detecting and triangulating radio-emitting drone operators. Designed for swarm deployment.

---

## ⚙️ Core Specifications

- **Weight:** ≤ 1 kg (target: 700–900 g)
- **Frequency Range:** 25 MHz – 6 GHz
- **Number of RF channels:** 5 synchronized
- **Direction Finding (DoA):** sub-5° accuracy (goal: <3°)
- **Processing:** onboard SDR + microcontroller (Raspberry Pi CM4 or similar)
- **Power Supply:** DC 5–12 V, ~8–10 W typical
- **Antenna configuration:** uniform linear array (ULA), 5 elements
- **Data output:** UDP/serial telemetry + blockchain logging
- **Estimated detection radius (active):** 30 km
- **Detection radius (passive reflection):** ~2–4 km
- **Telemetry hash interval:** every 10–30 sec

---

## 🔧 Planned Integration

- Triangulation software: adapted from KrakenSDR (GNU Radio)
- Blockchain logging: Ethereum L2 + EwX token auth
- Swarm sync: time-aligned GPS + LoRa mesh

---

## 🧪 Status
Design in concept stage. Hardware component selection pending.  
Current work focuses on simulation and drone mounting constraints.
