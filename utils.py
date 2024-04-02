"""Utils for preprocessing and feature engineering"""
from sklearn.base import BaseEstimator, TransformerMixin # To create custom transformers
import numpy as np
import pandas as pd


class FrecuencyEncoder(BaseEstimator, TransformerMixin):
    """Aplica fecuency encoding a las columnas"""
    ...


def apply_base_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica el preprocesamiento base definido por el equipo"""
    new_df = df.drop(['id_colaborador', 'fecha_nacimiento', 'fecha_incorporacion'], axis=1)

    # preprocess each column, imputing using 0 and
    # changing dtype to integer.
    cols = ['id_ultimo_jefe', 'performance_score']

    for col in cols:
        new_df[col] = new_df[col].fillna(0)
        new_df[col] = new_df[col].astype(int)

    return new_df