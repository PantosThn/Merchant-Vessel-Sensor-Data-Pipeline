import pandas as pd
import numpy as np
from global_land_mask import globe
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from api.logging.logger import logger

class NameDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_keep):
        self.columns_to_keep = columns_to_keep

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        logger.info(f"Number of columns before NameDropper: {X.shape[1]}")
        X_dropped = X[self.columns_to_keep]
        logger.info(f"Number of columns after NameDropper: {X_dropped.shape[1]}")
        return X_dropped
    
class LatLongDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        original_shape = X.shape
        logger.info(f"Shape before LatLongDropper: {original_shape}")
        X_dropped = X.dropna(subset=['latitude', 'longitude'])
        dropped_percentage = (1 - X_dropped.shape[0] / original_shape[0]) * 100
        dropped_percentage = round(dropped_percentage, 2)
        logger.info(f"Shape after LatLongDropper: {X_dropped.shape}")
        logger.info(f"Percentage of dropped observations: {dropped_percentage}%")
        return X_dropped

class OnLandAssigner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Assign 'on_land' column based on latitude and longitude
        X['on_land'] = X.apply(lambda row: globe.is_land(row['latitude'], row['longitude']), axis=1)

        return X
    
class SeaCurrentsCalculator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Assuming X is your DataFrame
        X['sea_currents_speed'] = np.sqrt(X['current_ucomp']**2 + X['current_vcomp']**2)
        X['sea_currents_angle'] = np.arctan2(X['current_vcomp'], X['current_ucomp'])

        # Convert angle to degrees
        X['sea_currents_angle'] = np.degrees(X['sea_currents_angle'])
        X['sea_currents_angle'] = (X['sea_currents_angle'] + 360) % 360

        return X

class SimpleImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy='mean'):
        self.strategy = strategy

    def fit(self, X, y=None):
        # Identify numeric columns with missing values
        self.cols_with_missing = X.select_dtypes(include=[np.number]).columns[X.isnull().any()]

        if not set(self.cols_with_missing).issubset(set(X.columns)):
            raise ValueError("Columns with missing values not present in the input DataFrame.")

        return self

    def transform(self, X):
        # Apply imputation only to numeric columns with missing values
        X['power'] = self.imputer.transform(X['power'])
        return X

class DropNATransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.dropna()