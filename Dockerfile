# Somewhat overkill to package a single python command... discuss.
FROM python:3.7-alpine
WORKDIR /manifests
EXPOSE 80
CMD ["python", "-m", "http.server", "80"]
