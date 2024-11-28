#!/bin/sh
docker run -v "$(pwd):/src" -e "PLATFORMS=windows" fydeinc/pyinstaller ./Windows.spec
