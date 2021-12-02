#!/bin/bash

pip install ottopy==0.1.19
jupyter nbextension install ottopy --user --py
jupyter nbextension enable ottopy --user --py

python -c "import ottopy; print(ottopy.__version__)"