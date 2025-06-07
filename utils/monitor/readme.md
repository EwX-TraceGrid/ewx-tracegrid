# Passive RF Monitor

This is a lightweight Python script to passively monitor multiple radio frequencies using SDR (or 5 RTL-SDRs in independent mode).

## 📡 Features

- Scans 5 predefined frequencies (can be customized)
- Detects signal presence by measuring signal power
- Prints real-time status of each band
- Designed for wideband surveillance and signal spotting

## 🔧 Requirements

- Python 3.7+
- `pyrtlsdr` Python library

Install with:

```bash
pip install pyrtlsdr
```

## 🚀 Usage

```bash
python monitor.py
```

## 🛠 Frequencies (default)

- VHF Airband (118.000 MHz)
- ACARS/VDL2 (136.975 MHz)
- ADS-B (1090 MHz)
- Aero Satellite (1545 MHz)
- Spare / ISM Band (433.92 MHz)

## ⚙️ Customization

You can edit the `frequencies` dictionary inside `monitor.py` to monitor different bands.

## 📘 Notes

- You can modify `SIGNAL_THRESHOLD_DB` to change detection sensitivity.
- This script works with standard RTL-SDRs but is optimized for KrakenSDR's architecture.

## 👾 License

MIT — use it, improve it, contribute back!

