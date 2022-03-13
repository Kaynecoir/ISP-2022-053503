FROM python

WORKDIR /Lab_1

COPY splitter.py

CMD ["python", "Lab_1.py"]