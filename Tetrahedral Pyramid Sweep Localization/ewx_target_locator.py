# EwX: TraceGrid — 3D Target Localization with Pyramid Sweep
# =============================================================
# This module estimates 3D position of a radio-emitting target using a vertical tetrahedral (4-vertex) drone trajectory.
# The drone flies through 6 triangular faces of the pyramid, each forming a plane for triangulation.

import numpy as np
from scipy.linalg import eigh

C = 299_792_458  # speed of light (m/s)

# === Steering Vector ===
def steering_vector(freq, array_geometry, theta, phi):
    wavelength = C / freq
    k = 2 * np.pi / wavelength
    theta_rad = np.radians(theta)
    phi_rad = np.radians(phi)

    direction = np.array([
        np.cos(phi_rad) * np.cos(theta_rad),
        np.cos(phi_rad) * np.sin(theta_rad),
        np.sin(phi_rad)
    ])

    return np.exp(1j * k * array_geometry @ direction)[:, np.newaxis]


# === 2D MUSIC Algorithm ===
def music_2d(cov_matrix, freq, array_geometry, az_range, el_range):
    eigvals, eigvecs = eigh(cov_matrix)
    noise_space = eigvecs[:, :-1]
    spectrum = np.zeros((len(el_range), len(az_range)))

    for i, el in enumerate(el_range):
        for j, az in enumerate(az_range):
            a = steering_vector(freq, array_geometry, az, el)
            proj = noise_space.conj().T @ a
            spectrum[i, j] = 1 / np.linalg.norm(proj)**2

    return spectrum


# === Triangulated Sweep Estimation ===
def triangulated_sweep_localization(freq, sweep_positions, spectra):
    dirs = []
    for (az, el) in spectra:
        theta = np.radians(az)
        phi = np.radians(el)
        dirs.append(np.array([
            np.cos(phi) * np.cos(theta),
            np.cos(phi) * np.sin(theta),
            np.sin(phi)
        ]))

    P = np.array(sweep_positions)
    D = np.array(dirs)
    A = np.eye(3) * 1e-6
    b = np.zeros(3)
    for i in range(len(P)):
        d = D[i]
        p = P[i]
        A += np.outer(d, d)
        b += d * (d @ p)

    est_position = np.linalg.solve(A, b)
    return est_position


# === Tetrahedral Pyramid Sweep Estimation ===
def tetrahedral_sweep_localization(freq, sweep_faces, spectra_list):
    all_estimates = []
    for face_points, spectra in zip(sweep_faces, spectra_list):
        est = triangulated_sweep_localization(freq, face_points, spectra)
        all_estimates.append(est)
    return np.mean(all_estimates, axis=0)


# === Optimized Pyramid Trajectory ===
def generate_tetrahedral_sweep(base_radius=5, height=4):
    top = np.array([0, 0, height])
    base = [
        np.array([ base_radius, 0, 0]),
        np.array([-base_radius/2,  np.sqrt(3)*base_radius/2, 0]),
        np.array([-base_radius/2, -np.sqrt(3)*base_radius/2, 0])
    ]
    center = np.mean(base, axis=0)
    sweep_faces = [
        [top, base[0], base[1]],
        [top, base[1], base[2]],
        [top, base[2], base[0]],
        [center, base[0], base[1]],
        [center, base[1], base[2]],
        [center, base[2], base[0]]
    ]
    return sweep_faces


# === Example Usage ===
if __name__ == "__main__":
    freq = 915e6
    sweep_faces = generate_tetrahedral_sweep()
    spectra_list = [
        [(10,15), (12,14), (11,16)],
        [(13,14), (12,15), (11,13)],
        [(10,16), (9,15), (11,14)],
        [(12,14), (13,15), (11,13)],
        [(11,14), (10,15), (12,13)],
        [(12,13), (11,14), (13,15)]
    ]
    est = tetrahedral_sweep_localization(freq, sweep_faces, spectra_list)
    print("[Tetrahedral Pyramid Sweep] Estimated 3D target position:", est)
