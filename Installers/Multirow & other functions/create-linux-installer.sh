#!/bin/sh
docker run -v "$(pwd):/src" -e "PLATFORMS=linux" fydeinc/pyinstaller ./Linux.spec
