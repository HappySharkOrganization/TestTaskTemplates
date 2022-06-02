# Tensorflow 2.x Base Task with Jupyter Notebook

This task uses the [tensorflow/tensorflow:latest-jupyter](https://hub.docker.com/r/tensorflow/tensorflow/tags) docker image, which is built on Linux Debian.

## Specifying package requirements
To add package requirements add a line for each requirement to the `packages.txt`. For example to install `wget` and binaries for `graphviz` you would put the following lines in `packages.txt`:

```bash
wget
graphviz
```

## Specifying Python requirements
To specify python package requirements, modify the `requirements.txt`

### Installing a pip dependency
If the package is available through pypi add the name of the package, and optional version. 
The syntax for specifying version is available on [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers).
For example, to add `numpy` version 1.20, and latest `matplotlib` as dependencies add the following lines to the `requirements.txt` file:

```bash
numpy==1.20
matplotlib
```

### Installing directly from git
If the package is not on pip, or you want the latest version, you can [install from git or other VCS](https://pip.pypa.io/en/stable/topics/vcs-support/).
The syntax is to `git+https://github.com/user/repo.git[@ref]`, where `ref` is optional and can be a branch, tag, or commit. For example,
```bash
git+https://github.com/user/repo.git@master
git+https://github.com/user/repo.git@v1.0
git+https://github.com/user/repo.git@da39a3ee5e6b4b0d3255bfef95601890afd80709
git+https://github.com/user/repo.git@refs/pull/123/head
```

For example if I wanted the latest version of `sonnet` then I would add this line to `requirements.txt`:
```bash
git+https://github.com/deepmind/sonnet.git
```

## Entry Point

The main entry point for the task is `src/main.py`. 

Modify the contents of `src/` folder and the entry point to build your task.