install poetry:
    poetry init

add this to the top of the pyproject file:

[tool.poetry]
package-mode = false

[tool.poetry.requires-plugins]
poetry-plugin-export = ">=1.8"


then run:
poetry install

and 

poetry add ANYTHING_YOU_WANT_TO_INSTALL (numpy etc)

and type:

poetry export -f requirements.txt --output requirements.txt --without-hashes



anytime a new thing is installed, just replicate the last two steps to install, and then add to requirements