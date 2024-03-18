FROM python
WORKDIR /app
COPY ./llama_cpu_server.py /app/llama_cpu_server.py
RUN pip install llama-cpp-python
EXPOSE 5000
CMD ["python", "llama_cpu_server.py"]