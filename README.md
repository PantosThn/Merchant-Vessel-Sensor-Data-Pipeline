You can run the main function (either by creating a venv and installing the requirments.txt or with docker compose) where it will launch the fast API and send a request to the upload file endpoint. 

Commands

docker-compose build

curl -X POST -F "file=@{path_to_the_csv}\DBdataset.csv" http://127.0.0.1:8000/uploadfile/
