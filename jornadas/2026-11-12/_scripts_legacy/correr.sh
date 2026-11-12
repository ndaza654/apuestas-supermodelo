#!/bin/bash
# Corre el supermodelo con cada entrada (prueba de la fase 1). Uso: bash correr.sh
cd /home/claude/supermodelo
for f in /home/claude/nov12/pub/entradas/*.json; do
  k=$(basename $f .json); d=/home/claude/nov12/corridas/$k; mkdir -p $d; cp $f $d/entrada.json
  if grep -q '"lineas":\[\]' $d/entrada.json; then echo "$k: sin cuotas, no se corre"; continue; fi
  s=$(date +%s); python3 -m supermodelo $d/entrada.json > $d/salida.md 2> $d/error.log; rc=$?
  echo "$k rc=$rc $(( $(date +%s) - s ))s $(wc -c < $d/error.log) bytes de error"
done
