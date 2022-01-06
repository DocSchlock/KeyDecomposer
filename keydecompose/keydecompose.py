"""
-- License here

-- author credits here

purpose here

"""


from typing import Callable
import pandas as pd

def decompose_frame(frame:pd.DataFrame):
    """
    Runs a full decomposure against a given DataFrame
    :param: frame - a pandas dataframe
    :return: a pandas Series that is the smallest unique label set
    """
    _frame = frame.drop_duplicates()
    _frame_size = len(_frame)
    _weight_series = generate_weighted_series(_frame)

    return recur_weights(_frame,_weight_series,_frame_size,None)

def recur_weights(df_inc:pd.DataFrame,weight_series:pd.Series,drop_dupe_frame_size:int,last_column_removed:str|None) -> \
Callable | pd.Series:
    """
    Operates on the dataframe to find the smallest unique label combination
    :param: df_inc - a dataframe
    :param: weight_series - a weighted Series composed from the same input frame
    :param: drop_dupe_frame_size - an int that is the unique row count of the dataframe
    :param: last_column_removed - str or None, the label of the last removed column kept \
    in case the column removal deadends
    """

    # check if we've reached the max id
    if weight_series.tail(1).values == 1:
        return weight_series

    # store the last good series at the start of the run
    last_data = weight_series

    # is the current series label combination unique in the dataframe
    if len(df_inc[weight_series.index].drop_duplicates()) == len(drop_dupe_frame_size):
        # if it is unique, removed the last column
        try:
            removed_col = weight_series.idxmin()
        except ValueError:
            return last_data
        fields_del = weight_series.drop(removed_col) # drop the least weight item
        #if there are no fields left after the last column is removed, return
        if fields_del.size == 0:
            return last_data
        return recur_weights(df_inc,fields_del,drop_dupe_frame_size,removed_col)
    elif last_column_removed is not None:
        # add the last removed column back at the beginning of the Series
        # with a value of 1 to cause breaks
        weight_series = pd.concat(pd.Series([1],index=[last_column_removed]),weight_series)
        return recur_weights(df_inc,weight_series,drop_dupe_frame_size,None)
    else:
        return last_data

def generate_weighted_series(frame: pd.DataFrame) -> pd.Series:
    """
    Generates a Series with labels of the column names
    The values are weighted 1-0 versus the max distinct value
    of the unique frame values
    :param: frame - pandas.dataframe
    :return: pandas.Series containing weight unique values versus the contents of the frame
    """
    series_unique = frame.nunique()
    return series_unique.map(lambda x: x*(1/series_unique.max()), na_action='ignore') \
    .sort(ascending=False)
