all: build

build:
	mkdir -p build
	cd build && cmake ..
	cd build && make

clean:
	rm -rf build
