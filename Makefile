clean:
	rm -rf build
	rm -rf dist
	rm -rf intellivoid.egg-info

build:
	python3 setup.py build
	python3 setup.py sdist

install:
	python3 setup.py install

publish:
	python3 -m twine upload dist/*