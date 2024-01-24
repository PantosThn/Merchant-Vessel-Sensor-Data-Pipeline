
## About

Created a simple pipeline via FastAPI that performs the following actions:
  - Keeps only relevant columns
  - Removes entries with missing latitude and longitude coordinates
  - Determines if AIS points are considered land or not and filters out land points
  - Calculates the sea current angle
  - Drops any remaining NaN values
  - Validates the data using Pydantic

## Usage

To run the main function, follow these steps:

1. **Launch FastAPI Server:**

   Use Docker Compose to build and run the Docker containers:

   ```bash
   docker-compose up --build

1. **Send requests:**
```bash
   curl -X POST -F "file=@/path/to/your/file.csv" http://127.0.0.1:8000/uploadfile/

