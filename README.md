# psdm-local-server
> Local server compiled to binary executable in order to be integrated into Electron app.

## Get started

Please install `Anaconda` first for data analysis.

Then create environment from `environment.yml`.

```
conda env create -f environment.yml
```


## Package

Use `scripts/package.py` to package app into executable binary.

```
python ./scripts/package.py
```

## Install new packages

```
conda install <new package name>
```

Then remember to update `environment.yml`.
```
conda env export > environment.yml
```