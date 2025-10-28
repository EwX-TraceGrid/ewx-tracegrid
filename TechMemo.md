# 📑 Technical Memorandum  
**EwX — Radio Monitoring across 25–1699 MHz**

![Repo Size](https://img.shields.io/github/repo-size/EwX-TraceGrid/ewx-tracegrid)
![Last Commit](https://img.shields.io/github/last-commit/EwX-TraceGrid/ewx-tracegrid)

---

## 1. System Operating Range
At the core is the **EwX** radio front-end — a **multi-channel, software-defined receiver synchronized in phase and frequency**:

- **Operating range:** 25–1699 MHz  
- **Simultaneous reception:** multi-channel (phase-aligned processing)  
- **Synchronization:** GPSDO (10 MHz + PPS)

👉 Covers all key bands for tactical communications, drones/UAS, aviation, and navigation.  :contentReference[oaicite:1]{index=1}

---

## 2. Signal Classification within the Operating Range

### 🔹 Drones & UAS (primary priority)

| Class | Bands (MHz) | Notes |
|---|---|---|
| DJI / Autel / Parrot (consumer) | 433 / 868 / 915 / 1200–1300 | Control & telemetry; identifiable by RF signatures |
| FPV (kamikaze, DIY) | 433 / 868 / 915 | Control links; pulsed activity during launch/attack |
| Recon (Vector, eBee, Skydio) | 433 / 868 / 915 / 1200–1300 | Long on-air presence (1–3 h) |
| Military (Bayraktar, Orlan, Shahed, Switchblade) | 400–450 / 868 / 915 / 1200–1300 / 1575–1602 | Control, GPS; persistent link via operator/relay |

👉 **Conclusion:** EwX SDR covers all major drone/UAS control & telemetry channels except pure Wi-Fi (2.4/5.8 GHz).  :contentReference[oaicite:2]{index=2}

---

### 🔹 Tactical Radios (secondary priority)

| Band (MHz) | Mode | Typical users |
|---|---|---|
| 30–88 | Analog tactical | Battalion/company |
| 136–174 | VHF High Band | Police, security, legacy military |
| 225–400 | Aviation, military channels | NATO, air forces, army |
| 380–430 | TETRA | EU militaries, MoI, police |
| 400–470 | DMR, P25, Motorola/Harris | Modern secured comms |
| 30–512 (sub-bands) | R-168 “Akveduk”, “Azart” (RF) | Russian forces, FHSS |

👉 **Conclusion:** All key tactical and special-purpose bands fall within EwX SDR’s coverage.  :contentReference[oaicite:3]{index=3}

---

### 🔹 Other targets within range
- **GPS/GLONASS/Galileo** — 1575/1602 MHz  
- **ADS-B / Mode-S (aviation)** — 1090 MHz  
- **PMR / amateur** — 433, 446 MHz (often reused by PMCs and militaries)  
- **GSM/LTE (Band 8 — 900 MHz)** — within reception range  :contentReference[oaicite:4]{index=4}

---

## 3. Operating Modes & Target Counts

### 🔸 Mode 1: **Quasi-tracking (real-time)**
- Continuous hold on selected frequencies (up to 5 channels in parallel).  
- **Targets:** **5–10** simultaneously (e.g., several drones and radios).  
- Coordinate updates: up to **1 Hz**.  
- For tracking and precision support tasks.  :contentReference[oaicite:5]{index=5}

### 🔸 Mode 2: **Situational Overview (band scan)**
- Fast scan of the full 25–1699 MHz spectrum with ~2.5 MHz steps.  
- Detection of dozens to hundreds of signals, consolidated into a master list.  
- **Targets:** **50–100+** sources in the area.  
- Coordinate updates: every **5–10 s**.  
- For building the overall RF picture and reconnaissance.  :contentReference[oaicite:6]{index=6}

---

## 4. Information Delivery Format
- **Private Telegram channel**  
- Automatic export of **KML/KMZ** files for Google Earth  
  - Placemark = signal source  
  - Color/icon = target type (drone, radio, aviation)  
  - Attributes: frequency, signal level, classification confidence (%), timestamp  :contentReference[oaicite:7]{index=7}

---

## Pilot Deployment: 2–3 EwX Units
- Real-time detection of drone/UAS and tactical radio signals (quasi-tracking mode)  
- Area-wide overview of dozens of sources (scan mode)  
- Delivery in an intuitive Google Earth format  
- Enables seeing the **“invisible” RF battlespace**  :contentReference[oaicite:8]{index=8}
