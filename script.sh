#!/bin/bash

echo $1 | sudo tee /sys/class/backlight/amdgpu_bl2/brightness
