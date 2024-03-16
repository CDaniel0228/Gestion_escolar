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
CMD ["python", "web2py.py", "-a", "'<recycle>'", "-i", "0.0.0.0", "-p", "8000"]
