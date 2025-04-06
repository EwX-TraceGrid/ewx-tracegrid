# KrakenSDR Wideband Monitor (Multi-Frequency)
# Requires: pyrtlsdr
# Install with: pip install pyrtlsdr

from rtlsdr import RtlSdr
import numpy as np
import time

# Define monitoring frequencies (in Hz)
frequencies = {
    'VHF_Airband': 118.0e6,  # Example: 118.0 MHz
    'ACARS_VDL2': 136.975e6,  # Example: 136.975 MHz
    'ADS-B': 1090e6,  # ADS-B
    'AERO_SAT': 1545e6,  # Satellite Aero
    'SPARE': 433.92e6  # Spare frequency (e.g. ISM)
}

# Threshold for signal presence detection (in dB)
SIGNAL_THRESHOLD_DB = -30

# Duration of each scan window (in seconds)
SCAN_DURATION = 1

# Function to detect if signal is present
def signal_detected(samples):
    power = 10 * np.log10(np.mean(np.abs(samples)**2))
    return power > SIGNAL_THRESHOLD_DB, power

# Start monitoring on each defined frequency
def monitor():
    sdr = RtlSdr()
    sdr.sample_rate = 2.048e6  # 2 MHz sample rate
    sdr.gain = 'auto'

    print("Starting KrakenSDR Passive Monitor...")
    try:
        while True:
            for name, freq in frequencies.items():
                sdr.center_freq = freq
                samples = sdr.read_samples(256*1024)
                detected, power = signal_detected(samples)
                print(f"{name}: {'SIGNAL' if detected else 'noise'} @ {freq/1e6:.3f} MHz | Power: {power:.2f} dB")
            print("--- cycle complete ---\n")
            time.sleep(SCAN_DURATION)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    finally:
        sdr.close()

if __name__ == '__main__':
    monitor()
