def avg(df, id_col, order_col, agg_col, lag):
    """In SQL : AVG() OVER (PARTITION BY ORDER BY)"""
    window = df.sort_values(by=[order_col], ascending=True)\
                    .groupby(id_col)[agg_col]\
                    .rolling(lag, min_periods = 1).mean()\
                    .reset_index(drop=True, level=0)
    
    return window
