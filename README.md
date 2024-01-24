
## About

Created a simple pipeline via FastAPI that performs the following actions:
  - Keeps only relevant columns
  - Removes entries with missing latitude and longitude coordinates
  - Determines if AIS points are considered land or not and filters out land points
  - Calculates the sea current angle
  - Drops any remaining NaN values
  - Validates the data using Pydantic

Please take a look at my EDA.ipynb as well as my word document in the e-mail for how I concluded to those actions.

## Usage

To run the main function, follow these steps:

1. **Launch FastAPI Server:**

   Use Docker Compose to build and run the Docker containers:

   ```bash
   docker-compose up --build

2. **Set csv filepath:**

   ```bash
   FILE_PATH="{your path}"
   ```
3. **Send requests:**
    ```bash
   curl -X POST -F "file=@$FILE_PATH" http://127.0.0.1:8000/uploadfile/
    ```
