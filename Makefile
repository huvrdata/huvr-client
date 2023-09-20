
build:
	docker compose build

run:
	docker compose run --rm --interactive --tty python $(cmd)

generate_api:
	make run cmd="bash -c 'cd codegen && ./main.py -u $(url)'"

test:
	make run cmd="pytest huvr_client"

.PHONY: build bash test
