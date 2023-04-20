NAME=fox-app
version=1.0
IMAGE=$(NAME):$(version)
PORT=5001

stop :
	- docker kill ${NAME}

build :
	docker build -t ${IMAGE} .

run : build
	docker run -dit ${DEVICE} --rm -p $(PORT):5000 --name ${NAME} ${IMAGE}

debug : build
	docker run -it ${DEVICE} --rm -p $(PORT):5000 --name ${NAME} ${IMAGE}

clean:
	- docker rmi -f ${IMAGE}
	- docker rm /${NAME}
	- docker images --quiet --filter=dangling=true | xargs --no-run-if-empty docker rmi
