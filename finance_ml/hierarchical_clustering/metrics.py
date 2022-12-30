def get_corr_dist(corr):
    """Calculate correlation distance
    
    Params
    ------
    corr: pd.DataFrame
    
    Returns
    -------
    pd.DataFrame
    """
    return ((1 - corr) / 2)**.5