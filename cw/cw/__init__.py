
"""
Generating binary data
"""

from numpy import *
import pandas as pd

def binomial_mixture(
    npts=10,
    success_prob=None,
    mixture=None,
    n_components=2,
    n_trials=[1, 20],
    include_component_idx=False,
    include_component_prob=False,
    **kwargs
):
    """
    Generates a mixture of binomial distributions.

    Parameters:
    npts (int): Number of points to generate. Default is 10.
    success_prob (list or None): List of success probabilities for each component. If None, random probabilities are generated.
    mixture (list or None): Mixture proportions for each component. If None, random proportions are generated.
    n_components (int): Number of components in the mixture. Default is 2.
    n_trials (int or list): Number of trials. If int, specifies the range of trials. If list, directly specifies trials for each component. Default is [1, 20].
    include_component_idx (bool): Whether to include the component index in the output. Default is False.
    include_component_prob (bool): Whether to include the component probability in the output. Default is False.
    **kwargs: Additional keyword arguments.

    Returns:
    pd.DataFrame: A DataFrame containing the generated binary data with columns:
        - 'n_trials': Number of trials.
        - 'n_success': Number of successes.
        - 'component_idx' (optional): Index of the component.
        - 'component_prob' (optional): Probability of the component.

    Example:
    >>> import pandas as pd
    >>> df = binomial_mixture(npts=5, success_prob=[0.2, 0.8], n_trials=[10, 20])
    >>> isinstance(df, pd.DataFrame)
    True
    >>> len(df)
    5
    """
    if success_prob is not None:
        n_components = len(success_prob)
    elif mixture is not None:
        n_components = len(mixture)

    if success_prob is None:
        success_prob = random.rand(n_components)
    success_prob = array(success_prob)
    if mixture is None:
        mixture = random.rand(n_components)
    mixture = array(mixture)
    mixture = mixture / sum(mixture)

    n_trials_col = kwargs.get('n_trials_col', 'n_trials')
    n_success_col = kwargs.get('n_success_col', 'n_success')

    if callable(n_trials):
        n_trials = n_trials(npts)
    else:
        if isinstance(n_trials, int):
            n_trials = [1, n_trials]
        if len(n_trials) == 2:  # assume min and max are given
            n_trials = random.randint(n_trials[0], n_trials[1], size=npts)

    data = {n_trials_col: n_trials}
    n_success = random.binomial(n_trials, dot(random.multinomial(1, mixture, size=npts), success_prob))

    data[n_success_col] = n_success

    if include_component_idx:
        component_idx = argmax(random.multinomial(1, mixture, size=npts), axis=1)
        data['component_idx'] = component_idx

    if include_component_prob:
        component_prob = dot(random.multinomial(1, mixture, size=npts), success_prob)
        data['component_prob'] = component_prob

    return pd.DataFrame(data)
