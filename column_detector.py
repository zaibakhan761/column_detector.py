import pandas as pd

def detect_column_types(df, threshold=20):
    """
    Detect column types in a DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame
        threshold (int): Unique values threshold for categorical
        
    Returns:
        dict: A dictionary with column names as keys and detected types as values
    """
    column_types = {}

    for col in df.columns:
        dtype = df[col].dtype
        
        # Case 1: Numeric but limited unique values (categorical-like)
        if pd.api.types.is_numeric_dtype(dtype):
            if df[col].nunique() < threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "numerical"
        
        # Case 2: Object or string type
        elif pd.api.types.is_string_dtype(dtype):
            if df[col].nunique() < threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "text"
        
        # Case 3: Other types (default to categorical)
        else:
            column_types[col] = "categorical"
    
    return column_types
