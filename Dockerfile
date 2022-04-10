FROM python:3.7
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["/bin/bash"]
