## About

This repository contains a comprehensive data pipeline designed for cleaning and analyzing sensor data collected from merchant vessels. The pipeline includes a series of steps aimed at ensuring the quality and reliability of the data, starting from data cleaning to remove noise and outliers, followed by data transformation to create additional features such as sea currents speed and angle relative to the vessel. Visualization of the data cleaning process is provided to summarize the effectiveness of the cleaning steps.

Additionally, a bonus feature of this project is the dockerization of the environment, which allows for easy deployment of the pipeline. The Docker image encapsulates all the required components and dependencies, providing a containerized environment with an endpoint for interacting with the pipeline.

## Pipeline for AIS Data Processing

Created a simple pipeline via FastAPI that performs the following actions:
  - Keeps only relevant columns
  - Removes entries with missing latitude and longitude coordinates
  - Determines if AIS points are considered land or not and filters out land points
  - Calculates the sea current angle
  - Drops any remaining NaN values
  - Validates the data using Pydantic

## Before and After Cleaning


<img src="https://i.ibb.co/mDdJGXB/voyage-before.png" alt="Before Cleaning" width="375" style="float: left; margin-right: 10px;"> <img src="https://i.ibb.co/d2mgRNK/voyage-after-cleaning.png" alt="After Cleaning" width="400" style="float: left; margin-right: 10px;">


## Usage

To run the main function, follow these steps:

1. **Set csv filepath:**

   ```bash
   FILE_PATH="{your path}"  #eg FILE_PATH='C:\Users\thanos\ds-challenge-1\data\raw\DBdataset.csv'
   ```
   ```bash
   export HOST_DATA_PATH="{folder for volumes}" #eg export HOST_DATA_PATH="/c/Users/thanos/ds-challenge-1"

2. **Launch FastAPI Server:**

   Use Docker Compose to build and run the Docker containers:

   ```bash
   docker-compose up --build

3. **Send requests:**
    ```bash
   curl -X POST -F "file=@$FILE_PATH" http://127.0.0.1:8000/uploadfile/
    ```
