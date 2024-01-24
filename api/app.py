from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import io
from api.data_processing import create_pipeline
from fastapi.responses import StreamingResponse
from io import BytesIO
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # Read the content of the uploaded file as a pandas DataFrame
        content = await file.read()
        raw_df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        
        # Apply pipeline to the raw DataFrame
        columns_to_keep = ['latitude', 'longitude', 'datetime', 'speed_overground',
                   'stw', 'direction', 'current_ucomp', 'current_vcomp', 
                   'draft_aft', 'draft_fore', 'comb_wind_swell_wave_height', 'power']

        pipeline = create_pipeline(columns_to_keep)
        df_transformed = pipeline.fit_transform(raw_df)

        # Specify the path to the processed data directory
        processed_data_dir = os.path.join(os.path.dirname(__file__), "data", "processed")

        # Make sure the directory exists, create it if necessary
        os.makedirs(processed_data_dir, exist_ok=True)

        # Specify the path to the transformed CSV file within the processed data directory
        transformed_csv_path = os.path.join(processed_data_dir, "transformed_output.csv")

        # Save the DataFrame to the CSV file
        df_transformed.to_csv(transformed_csv_path, index=False)

        # Return a message with the saved file path
        return {"message": "File saved successfully", "file_path": transformed_csv_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))