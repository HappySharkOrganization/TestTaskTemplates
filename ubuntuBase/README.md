# Ubuntu Base Task

This task uses the [latest ubuntu](https://hub.docker.com/_/ubuntu?tab=tags) docker image to allow flexible exploratory task construction.

## Specifying package requirements
To add package requirements add a line for each requirement to the `packages.txt`. For example to install `wget` and binaries for `graphviz` you would put the following lines in `packages.txt`:

```bash
wget
graphviz
```


## Entry Point

The main entry point for the task is `src/main.sh`, which does nothing initially. 

Modify the contents of `src/` folder and the entry point to build your task.