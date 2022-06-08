docker build --build-arg CLICK_VERSION="7.1.2" -t click7/testing .
docker build --build-arg CLICK_VERSION="8.1.3" -t click8/testing .

docker run --rm -ti click7/testing /bin/bash -c "cd code; python3 -c 'import click; print(click.__version__)'; pytest -v"
docker run --rm -ti click8/testing /bin/bash -c "cd code; python3 -c 'import click; print(click.__version__)'; pytest -v"
