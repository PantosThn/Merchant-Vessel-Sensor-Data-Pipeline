docker-compose build

curl -X POST -F "file=@{path_to_the_csv}\DBdataset.csv" http://127.0.0.1:8000/uploadfile/
