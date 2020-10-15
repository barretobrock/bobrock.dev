start-dev:
	yarn webpack --mode development --watch & ~/venvs/bobrock.dev/bin/python3 debug_app.py

prod-build:
	yarn webpack --mode production