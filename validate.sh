#!/bin/sh

for d in ./workitems/*/ ; do
    azbacklog -t test --validate-only $d
done