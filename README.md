# Tidal Disruption Event (TDE) Mass Fallback Simulator

This repository contains a theoretical computational pipeline for modeling the accretion dynamics and light curves of Tidal Disruption Events (TDEs). The scripts simulate the mass fallback rate of stellar debris, apply physical radiation constraints, and scale the resulting super-Eddington accretion phases across different Supermassive Black Hole (SMBH) masses.

## Scientific Objective

When a star is tidally disrupted by a supermassive black hole, the bound stellar debris returns to the pericenter at a rate dictated by Keplerian orbital mechanics. This pipeline models the resulting flare by calculating:
1. **The Theoretical Mass Fallback Rate:** The pure $\dot{M} \propto t^{-5/3}$ power-law decay.
2. **The Eddington Limit ($L_{Edd}$):** The radiation pressure bottleneck where the black hole's accretion rate is capped, resulting in a luminosity plateau during the early stages of the event.
3. **SMBH Mass Scaling:** The dependence of the peak fallback time, peak accretion rate, and Eddington threshold on the central black hole mass ($10^5 M_\odot$ to $10^7 M_\odot$).

## Repository Structure

* **`scripts/01_simulate_fallback.py`**: Generates the foundational theoretical mass fallback curve for a standard TDE, calculating the $t^{-5/3}$ decay and exporting the data array.
* **`scripts/02_eddington_luminosity.py`**: Ingests the theoretical curve and applies a vectorized Eddington cap, generating a comparative light curve that visualizes the super-Eddington plateau against the theoretical fallback rate.
* **`scripts/03_bh_mass_scaling.py`**: A comparative simulation testing SMBH masses from $10^5$ to $10^7 M_\odot$. It dynamically scales the peak timescales and Eddington limits to demonstrate how lower-mass black holes experience prolonged super-Eddington phases while higher-mass black holes quickly transition to the standard $t^{-5/3}$ decay.
* **`data/`**: Stores the generated fallback rate CSV files.
* **`output/`**: Contains the generated log-log plots visualizing the light curves and mass scaling dynamics.

## Dependencies

This pipeline requires Python 3 and the following scientific computing libraries:

```bash
pip install numpy pandas matplotlib
