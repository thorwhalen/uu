# cw

Generating binary data

To install:	```pip install cw```

# Examples

```python
>>> from cw import binomial_mixture
>>> import pandas as pd
>>> df = binomial_mixture(npts=5, success_prob=[0.2, 0.8], n_trials=[10, 20])
>>> isinstance(df, pd.DataFrame)
True
>>> len(df)
5
```