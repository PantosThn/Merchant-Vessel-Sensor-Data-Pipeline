# pydantic_validators.py
from pydantic import BaseModel, ValidationError, constr, validator
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from api.logging.logger import logger

class RawInputModel(BaseModel):
    latitude: float
    longitude: float
    datetime: constr(strip_whitespace=True, max_length=50)
    speed_overground: float
    stw: float
    direction: float
    current_ucomp: float
    current_vcomp: float
    draft_aft: float
    draft_fore: float
    comb_wind_swell_wave_height: float
    power: float
    sea_currents_angle: float

    @validator("sea_currents_angle")
    def validate_sea_currents_angle(cls, value):
        if not 0.0 <= value <= 360.0:
            raise ValueError("sea_currents_angle must be between 0 and 360.")
        return value

class RawInputValidator:
    def __init__(self, model):
        self.model = model

    def validate(self, df):
        validated_data = []
        for _, row in df.iterrows():
            try:
                item = self.model(**row)
                validated_data.append(item.dict())
            except ValidationError as e:
                logger.error(f"Validation error for raw input: {e}")

        # Log success message after the loop
        logger.info("Pydantic tests have been passed successfully.")
        
        return pd.DataFrame(validated_data)
        

# Custom Transformer for Pydantic Validation
class PydanticValidator(BaseEstimator, TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        validator = RawInputValidator(self.model)
        return validator.validate(X)


pydantic_validator = PydanticValidator(RawInputModel)