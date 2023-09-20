
build:
	docker compose build

run:
	docker compose run --rm --interactive --tty python $(cmd)

generate_api:
	make run cmd="bash -c 'cd codegen && ./main.py -u $(url)'"

test:
	make run cmd="pytest huvr_client"

ipython:
	make run cmd="ipython -c 'from huvr_client import get_huvr_client, HuvrClient' -i"

.PHONY: build bash test
