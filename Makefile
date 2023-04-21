NAME=fox-app
version=1.0
IMAGE=$(NAME):$(version)
PORT=5001

stop :
	- docker kill ${NAME}

build :
	docker build -t ${IMAGE} .

run : build
	mkdir -p $(shell pwd)/db
	docker run -dit ${DEVICE} --rm -p $(PORT):5000 --mount type=bind,source=$(shell pwd)/db,target=/app/db --name ${NAME} ${IMAGE}

debug : build
	mkdir -p $(shell pwd)/db
	docker run -it ${DEVICE} --rm -p $(PORT):5000 --mount type=bind,source=$(shell pwd)/db,target=/app/db --name ${NAME} ${IMAGE}

clean :
	rm -rf $(shell pwd)/db
	docker rmi -f ${IMAGE}
