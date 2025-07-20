FROM python:3.12
ENV TZ Asia/Shanghai
WORKDIR /app
COPY . /app
RUN pip install --trusted-host mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple  -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
EXPOSE 80