# slim for this purpose since it has all basic resources in image
FROM python:3.8-slim-buster

WORKDIR /app

# move req file to container
COPY requirements.txt requirements.txt
# install imports to container env
RUN pip3 install -r requirements.txt
# move all ancillary files to container working DIR
COPY . .

# run python to standup the local server
CMD [ "python3", "-u", "application.py" ]
