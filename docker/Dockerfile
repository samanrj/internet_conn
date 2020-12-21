# let's go with python3
FROM python:3
MAINTAINER Saman Rajaei

#
## we'll do a multi-stage build here by first resolving dependencies from
## the requirements file so Docker can cache them in the base+1 layer,
## while this won't matter much for end prod image (or at all for a project this size),
## it helps significantly reduce the development cycle when doing local testing
#
COPY requirements.txt app/
WORKDIR app/
RUN pip install -r requirements.txt

#
## set some blank envs to be at runtime
#
ENV _REQ_TIMEOUT_SECS=
ENV _PREFERRED_HOST=
ENV _PREFERRED_PORT=
ENV _CHECK_FREQUENCY_SECS=

#
## now copy the rest in and let's run a unit test
## there as well as part of the build to make sure
## we didn't break anything
#
COPY . app/
WORKDIR app/
LABEL stage=test
RUN pytest ./tests/test_sample.py

#
## now execute the main
#
ENTRYPOINT ["/bin/bash", "-c", "python ./src/main.py"]
