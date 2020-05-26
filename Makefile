.PHONY: all clean

all: 

clean:
	rm -rf dist build secretpy.egg-info 
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
