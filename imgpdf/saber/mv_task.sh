#!/bin/bash

for i in {10..99}
do
    mv "$i.jpg" "0$i.jpg"
done
