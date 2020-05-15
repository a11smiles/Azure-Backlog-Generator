#!/bin/sh

for d in ./workitems/*/ ; do
    main.py -t test --validate-only $d
done