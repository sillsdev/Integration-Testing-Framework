#!/bin/bash

# Will help with memory leaks caused my mono & FLEX ~ Ryan
sync
echo 3 > /proc/sys/vm/drop_caches
