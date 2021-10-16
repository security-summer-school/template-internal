FILE	:= ../flag
FLAG	:= $(shell cat $(FILE))

build: generate
	docker build -f Dockerfile -t sss-web-ctf-final_challenge-name-1 ..

run: generate build
	docker run -d -p 8001:80 --name sss-web-ctf-final_challenge-name-1 sss-web-ctf-final_challenge-name-1

generate:
	sed 's/__TEMPLATE__/$(FLAG)/g' ../src/index.template.php > ../src/index.php

stop:
	docker stop sss-web-ctf-final_challenge-name-1

clean: stop
	docker rm sss-web-ctf-final_challenge-name-1

.PHONY: build run stop clean
