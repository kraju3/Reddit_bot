FROM python:3 as pythonbase

COPY * /usr/app/bot/

WORKDIR /usr/app/bot/

RUN ["pip3", "install", "-r", "requirements.txt" ]

FROM python:3-alpine

COPY --from=pythonbase /root/.cache /root/.cache

COPY --from=pythonbase /usr/app/bot/ /usr/app/bot/

COPY --from=pythonbase /usr/app/bot/requirements.txt /usr/app/bot/


WORKDIR /usr/app/bot/
RUN pip install -r requirements.txt && rm -rf /root/.cache


CMD ["python" ,"nsbot.py"]

ENTRYPOINT ["python","nsbot.py"]

