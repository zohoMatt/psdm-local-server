from psdm.fit_router.repo.PSDM import PSDM

import numpy as np
import pandas as pd
import pylab as plt

input_data = pd.DataFrame({
    'kf': 2.08e-3,
    'dp': 5.28e-6,
    'K': 35.3,
    '1/n': 1,
    'MW': 314,
    'MolarVol': 182,
    'BP': 156,
    'flrt': 1893,
    'epor': 0.5,
    'wt': 10200,
    'L': 114,
    'diam': 14.6,
    'rhop': 0.857,
    'rhof': 0.5344,
    'rad': 0.046,
    'influentID': 'Test'
}, index=['Test'])

# Tortuosity
# PSDFR is fixed to 5 in PSDM.run_psdm_kfit().
tortu = pd.DataFrame([1, 0.05], columns=['Test'], index=['tortu', 'psdfr'])

# Initial concentration
time = np.arange(280)
idx = pd.MultiIndex.from_tuples([('Test', 'Test')])
inflow_c0 = pd.DataFrame(1.84e-2, index=time, columns=idx)

compund_props = input_data[['MW', 'MolarVol']].transpose()

data_store = input_data[['K', 'kf', 'dp', '1/n']].transpose()

# fixme What does `q` mean?
data = pd.DataFrame(1, columns=data_store.columns, index=['q'])
data_store = data_store.append(data)
xn = data_store['Test']['1/n']

column_prop = input_data[
    ['epor', 'diam', 'L', 'wt', 'rhop', 'rhof', 'flrt', 'rad', 'influentID']
].transpose().append(tortu)

test_column = PSDM(
    column_prop['Test'],
    compund_props,
    inflow_c0,
    nr=9,
    nz=9,
    xn=xn,
    conc_type='ng',
    chem_type='PFAS',
    k_data=data_store,
    test_range=data_store.loc['K'].values,
    xn_range=data_store.loc['1/n'].values,
    optimize=False
)

comp, K, xn, ssq, md = test_column.run_psdm_kfit('Test')
plt.plot(md.index.values, md.values, '--', label='PFAS')
plt.ylabel('Concentration - ug/L')
plt.xlabel('time - days')

plt.legend()
plt.show()
plt.close()
md.to_csv('results.csv')
