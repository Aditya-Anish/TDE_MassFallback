import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
input_path = os.path.join('data', 'tde_theoretical_curve.csv')
data = pd.read_csv(input_path)
time_days = data['time_days']
fallback_rate = data['fallback_rate']
m_dot_edd = 2.0  
radiative_efficiency = 0.1 
accretion_rate = np.minimum(fallback_rate, m_dot_edd)
luminosity_theoretical = radiative_efficiency * fallback_rate
luminosity_observed = radiative_efficiency * accretion_rate
data['accretion_rate'] = accretion_rate
data['luminosity_observed'] = luminosity_observed
data.to_csv(os.path.join('data', 'tde_eddington_curve.csv'), index=False)

plt.figure(figsize=(10, 6))
plt.plot(time_days, luminosity_theoretical, 
         linestyle='--', color='grey', label='Theoretical Fallback (t^-5/3)')
plt.plot(time_days, luminosity_observed, 
         linewidth=2.5, color='crimson', label='Observed Luminosity')
eddington_luminosity = float(radiative_efficiency * m_dot_edd)
plt.axhline(y=eddington_luminosity, color='black', linestyle=':', 
            alpha=0.7, label='Eddington Limit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time since disruption (Days)')
plt.ylabel('Luminosity (Arbitrary Units)')
plt.title('TDE Light Curve: Theoretical Fallback vs Eddington-Limited Accretion')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
os.makedirs('output', exist_ok=True)
output_file = os.path.join('output', 'eddington_lightcurve.png')
plt.savefig(output_file, dpi=300)
print(f"Success! Plot saved to {output_file}")
plt.show()