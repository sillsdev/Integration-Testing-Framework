#!/bin/bash

echo "test 1"
python -c "import os; os.system('./call_from_py.sh'); print 'after call'"
echo "test 2"
