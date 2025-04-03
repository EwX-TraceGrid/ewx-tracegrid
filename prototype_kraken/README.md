# Prototype: KrakenSDR-Based RF System

This subdirectory contains the initial base from the open-source [KrakenSDR project](https://github.com/krakenrf/gr-krakensdr), licensed under GNU GPL v3.

We use it as a technical foundation for early-stage development of the EwX decentralized RF detection network.

---

## 🧩 Why KrakenSDR?

KrakenSDR is one of the most well-known open-source SDR-based direction-finding implementations.  
It provides a strong starting point for:

- Multi-antenna RF capture
- Signal direction-of-arrival processing
- GNU Radio integration

---

## 🔧 EwX Modifications (Planned / In Progress)

We plan to adapt this codebase for the EwX system, including:

- Drone-mounted lightweight porting
- Integration with onboard triangulation logic
- RF event compression and hash generation
- Logging into decentralized Ethereum-based telemetry system
- Swarm coordination between multiple airborne nodes

---

## 📜 License & Credits

This code is based on the original work by **KrakenRF**, under:

**GNU General Public License v3 (GPL-3.0)**  
See full license text here: [COPYING](https://github.com/krakenrf/gr-krakensdr/blob/main/COPYING)

All our modifications will remain open and licensed under the same terms.

