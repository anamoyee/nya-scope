#!/usr/bin/env bash

set -euo pipefail

# build, then publish via uv

# assume PYPI token is stored in GNU password-store
# at /pypi_tokens/{TOKEN_NAME}

TOKEN_NAME="__main__"

if [[ TOKEN_NAME == "" ]]; then
	echo "Provide a TOKEN_NAME in a form of a (GNU password-store) path" >&2
	exit 1
fi

uv build
UV_PUBLISH_USERNAME="__token__" UV_PUBLISH_PASSWORD="$(/bin/pass "pypi_tokens/${TOKEN_NAME}")" uv publish
