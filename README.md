# You must create your own Virtual Environment

```shell
python -m venv virtualenvironmentname
```

Activate your environment

## MacOS and Linux

```shell
source virtualenvironmentname/bin/activate
```

## Windows

```shell
virtualenvironmentname\Scripts\activate
```

Note: you may have to run

```shell
Set-ExecutionPolicy RemoteSigned
```

in order to allow the virtual environment script to run on Windows.
\
then install dependencies

```shell
pip install django && pip install django-bootstrap5
```
