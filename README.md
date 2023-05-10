
Requests:
_________

1. /books
2. /books/id
3. /books/id/orders
4. /books/id/orders/order_id

-Project executed using python!

-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the environment of the docker file.

-Create Docker Image by running : "docker build -t docker-python ."

-Check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 8050:8050 docker-python"

-Check running docker container by "docker ps"

-Have added an "Error handling functinality" when searched for the book numbers which are not stored on docker container. Usually it gives a "page not found/URL not found" error. It will not show "No Data Found" under this searched criteria. This provides a better user experience by indicating there is no data available for that particular book.

-Thats it!

-Thank you...
