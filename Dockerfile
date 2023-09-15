#Deriving the latest base image
FROM python:3.9

# Debian Unstable Repository (codename "Sid").
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list

#Update
RUN apt-get update
#Installing firefox
RUN apt-get install -y --no-install-recommends firefox

# An working directory
WORKDIR /app

#to COPY the remote file at working directory in container
COPY . /app

# Now the structure looks like this '/app/webscrapping.py'
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD ["python", "./webscrapping.py"]
