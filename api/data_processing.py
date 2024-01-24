from api.my_transformers import (
    ColumnDropper, LatLongDropper, OnLandAssigner,
    SeaCurrentsCalculator, SimpleImputer, DropNATransformer
)
from api.pydantic_validators import (
    PydanticValidator, RawInputModel
)
from sklearn.pipeline import Pipeline

def create_pipeline(columns_to_keep):
    column_dropper = ColumnDropper(columns_to_keep=columns_to_keep)
    lat_long_dropper = LatLongDropper()
    on_land_assigner = OnLandAssigner()
    sea_currents_calculator = SeaCurrentsCalculator()
    simple_imputer = SimpleImputer(strategy='mean')
    drop_nas = DropNATransformer()

    # Define the pipeline
    pipeline = Pipeline([
        ('name_dropper', column_dropper),
        ('lat_long_dropper', lat_long_dropper),
        ('on_land_assigner', on_land_assigner),
        ('sea_currents_calculator', sea_currents_calculator),
        ('drop_nas', drop_nas),
        ('pydantic_validator', PydanticValidator(RawInputModel))
    ])

    return pipeline