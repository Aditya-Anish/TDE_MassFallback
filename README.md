# TDE Light Curve & Accretion Modeling

I wrote these Python scripts to model the mass fallback rates of Tidal Disruption Events (TDEs). The goal was to go beyond the basic $t^{-5/3}$ power law and actually simulate the super-Eddington accretion phases for varying supermassive black hole (SMBH) masses.

### What this code does
*   **`01_simulate_fallback.py`**: Calculates the raw theoretical mass fallback rate ($t^{-5/3}$ decay) and exports the data array.
*   **`02_eddington_luminosity.py`**: Takes that raw fallback curve and applies an Eddington limit cap, showing the plateau where the black hole chokes on radiation pressure.
*   **`03_bh_mass_scaling.py`**: Compares the accretion dynamics across $10^5$, $10^6$, and $10^7 M_\odot$ black holes, showing how smaller black holes get stuck in a prolonged super-Eddington phase while larger ones swallow the debris much more easily.

### How to run it
Clone the repo, ensure you have the required libraries (`pip install numpy pandas matplotlib`), and run the scripts in order. The plots save automatically to the `output/` folder.
