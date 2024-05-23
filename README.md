# You must create your own Virtual Environment

```shell
python -m venv venv
```

Activate your environment

## MacOS and Linux

```shell
source venv/bin/activate
```

## Windows

```shell
venv\Scripts\activate
```

Note: you may have to run

```shell
Set-ExecutionPolicy RemoteSigned
```

to allow the virtual environment script to run on Windows.
\
then install dependencies

```shell
pip install django
pip install django-bootstrap5
```
