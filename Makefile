
build:
	docker compose build

run:
	docker compose run --rm --interactive --tty python $(cmd)

generate_client:
	# example:
	# 		make generate_client open_api_url="https://docs.huvrdata.app/openapi/63239c77e03070000fdc03d0"
	make run cmd="bash -c 'cd codegen && ./main.py -u $(open_api_url)'"
	make lint

test:
	make run cmd="pytest huvr_client"

ipython:
	make run cmd="ipython -c 'from huvr_client import get_huvr_client, HuvrClient' -i"

lint:
	make run cmd="black huvr_client"


.PHONY: build bash test
