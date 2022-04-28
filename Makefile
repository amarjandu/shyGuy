.PHONY: link_interfaces
link_interfaces:
	ln -sv \
	${project_root}/python-type-stubs/cv2/__init__.pyi \
	${project_root}/.venv/lib/python3.9/site-packages/cv2

.PHONY cvenv
cvenv:
	if test -e .venv; then rm -rf .venv/; fi
	python -m venv .venv
	source /.venv/bin/activate