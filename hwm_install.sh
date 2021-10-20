#!/bin/bash
mkdir thirdparty
git clone https://github.com/rilma/pyHWM14.git thirdparty/pyHWM14
cd thirdparty/pyHWM14 && pip3 install -e . 
