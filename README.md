# 🌳 GHTree

Web app similar to LinkTree using information from GitHub profile.  
> From [simplesite template](https://github.com/tataraba/simplesite)

![ShowCase](showcase.png)

## 🧪 Try it out

> It may take a few seconds to load the first time.

### [https://ghtree.fly.dev/](https://ghtree.fly.dev/)

## 🚀 Deploy

You can run your own instance locally or deploy it to a serverless platform like [Fly.io](https://fly.io/).

### -> Locally

There are two ways to run the app locally, using Docker or Python.

#### 🐳 Docker (recommended)

```sh
docker run --rm -p 8000:8000 ghcr.io/rooyca/ghtree:master
```

You could also build the image yourself.

```sh
docker build -t ghtree .
docker run --rm -p 8000:8000 ghtree
```

There are three Dockerfiles, one with full `python` image, one with `python:slim` and one with `python:alpine`. You can use the one that suits you best. For example, if you want to use the `slim` version, you can do:

```sh
docker build -t ghtree -f Dockerfile.slim .
docker run --rm -p 8000:8000 ghtree
```

Although I recommend using the [alpine version](Dockerfile), since it is the smallest one. Let's look at the size of each image.

| Dockerfile | Size |
| --- | --- |
| [Dockerfile (alpine)](Dockerfile) | 163 MB |
| [Dockerfile.slim](Dockerfile.slim) | 562 MB |
| [Dockerfile.full](Dockerfile.full) | +1 GB |


#### 🐍 Python

```sh
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### -> Serverless

You can deploy the app to any serverless platform that supports Python apps, like [Fly](https://fly.io/) or any other.

#### 🦋 Fly.io

```sh
fly launch
fly deploy
```

## 🛠️ Build with

- [FastAPI](https://fastapi.tiangolo.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [HTMX](https://htmx.org/)
- [GitHub API](https://docs.github.com/en/rest)
- [Font Awesome](https://fontawesome.com/)

## 📝 TODO

- [ ] Add nix support

## 📄 License

[MIT](LICENSE)