
Requests:
_________

1. /books
2. /books/id
3. /books/id/orders
4. /books/id/orders/order_id

-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the environment of the docker file.

-Create Docker Image by running : "docker build -t docker-python ."

-Check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 8050:8050 docker-python"

-Check running docker container by "docker ps"
