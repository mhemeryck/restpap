# Minimal python image
FROM python:3.6.3-alpine3.6
MAINTAINER {{cookiecutter.email}}

# Variables
ENV UID=1000 \
  GUID=1000
ARG USER={{cookiecutter.username}}
ARG ROOT=/app

# Working folders
WORKDIR ${ROOT}

# Non-root user
RUN addgroup -S -g ${GUID} ${USER} \
  && adduser -S -g ${USER} -u ${UID} ${USER}

# Required for building some python packages
RUN apk --no-cache add \
  mariadb-dev python3-dev build-base \
  jpeg-dev

# Copy requirements and install
COPY requirements/requirements.txt /tmp/requirements.txt
RUN pip install --no-deps -r /tmp/requirements.txt

# Copy test requirements and install
COPY requirements/requirements_test.txt /tmp/requirements_test.txt
RUN pip install --no-deps -r /tmp/requirements_test.txt

# Change ownership
RUN chown ${USER}:${USER} -R .

# Switch to non-root user
USER ${USER}
