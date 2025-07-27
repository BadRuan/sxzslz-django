FROM python:3.12
ENV TZ Asia/Shanghai
WORKDIR /app
COPY . /app
RUN pip install --trusted-host mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple  -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--access-logfile", "-", "--error-logfile", "-", "sxzslz.wsgi:application"]