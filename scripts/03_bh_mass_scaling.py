import numpy as np
import matplotlib.pyplot as plt
import os
M_star=1.0
t_peak_base=40.0
m_dot_peak_base=5.0
bh_masses=[1e5,1e6,1e7]
colors=['teal','darkorange','purple']
plt.figure(figsize= (11,7))
for i,M_bh in enumerate(bh_masses):
    mass_ratio=M_bh/1e6
    t_peak=t_peak_base*np.sqrt(mass_ratio)
    m_dot_peak=m_dot_peak_base*np.sqrt(mass_ratio)
    m_dot_edd=0.5*mass_ratio
    time_days=np.linspace(t_peak,800,500)
    fallback_rate=m_dot_peak*(time_days/t_peak)**(-5/3)
    accretion_rate=np.minimum(fallback_rate, m_dot_edd)
    label_name=f'$M_{{BH}}= 10^{int(np.log10(M_bh))}\ M_\odot$'
    plt.plot(time_days,accretion_rate,linewidth=2.5, color=colors[i],label=label_name)
    plt.axhline(y=m_dot_edd,color=colors[i],linestyle=':',alpha=0.6)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time since disruption (days)',fontsize=12)
plt.ylabel('Accretion Rate/ Luminosity',fontsize=12)
plt.title('TDE Super-Eddington Phases Scaled by Black Hole Mass',fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, which='both',ls='--',alpha=0.3)
os.makedirs('output',exist_ok=True)
output_file=os.path.join("output","bh_mass_scaling.png")
plt.savefig(output_file,dpi=300,bbox_inches='tight')
print(f"Success! Mass scaling plot saved to {output_file}")
plt.show()