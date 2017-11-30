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
  jpeg-dev \
  wget ca-certificates

# Copy requirements and install
COPY requirements/requirements.txt /tmp/requirements.txt
RUN pip install --no-deps -r /tmp/requirements.txt

# Copy test requirements and install
COPY requirements/requirements_test.txt /tmp/requirements_test.txt
RUN pip install --no-deps -r /tmp/requirements_test.txt

# Install wait-for script
RUN wget https://raw.githubusercontent.com/Eficode/wait-for/a93091b798cfbeae856f3bf3a1151a56629a61bf/wait-for \
  -P /usr/local/bin \
  && chmod 744 /usr/local/bin/wait-for

# Change ownership
RUN chown ${USER}:${USER} -R .

# Switch to non-root user
USER ${USER}
