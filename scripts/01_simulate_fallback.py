import pandas as pd
import numpy as np
import os
print("Initializing the TDE fallback simulation... ")
t_peak=30.0
m_dot_peak=10.0
time_days=np.linspace(t_peak,500,500)
fallback_rate=m_dot_peak*(time_days/t_peak)**(-5/3)
data=pd.DataFrame({
    'time_days':time_days,
    'fallback_rate':fallback_rate
})
os.makedirs('data',exist_ok=True)
output_path=os.path.join('data',"tde_theoretical_curve.csv")
data.to_csv(output_path, index=False)
print(f"Success! Pure theoritical fallback curve saved to {output_path}")
