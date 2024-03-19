#version used
FROM python:3.11

#create folder
WORKDIR /app

#project libraries
COPY requirements.txt ./

#install the libraries
RUN pip install --no-cache-dir -r requirements.txt

#copy the project files
COPY . .

#service port
EXPOSE 8000


#start application
CMD ["sh","start.sh"]
