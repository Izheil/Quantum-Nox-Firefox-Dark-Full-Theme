#!/bin/sh
docker run -v "$(pwd):/src" fydeinc/pyinstaller -e "PLATFORMS=windows" ./Windows.spec
