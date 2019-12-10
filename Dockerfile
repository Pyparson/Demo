FROM python:3.7.3

RUN mkdir -p ~/test && python --version >~/test/a.txt && \
    pip install -r require.txt
