#!/bin/bash
cd doc/
pdflatex -interaction=nonstopmode proyecto  
biber proyecto
makeglossaries proyecto
pdflatex -interaction=nonstopmode proyecto
cd ..
invoke clean     