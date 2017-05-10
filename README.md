# stan

install dependencies: `sudo pip install -r requirements.txt`

run tests: `python -m unittest discover`

run a server locally: `export FLASK_APP=app/__init__.py; flask run`

design features: 
classic MVC application; 
json conversion follows a clean functional approach;

absence of image, showImage, slug and title elements considered as a malformed json;
absence of episodeCount or drm considered normal, but the whole entry is skipped;

tests features: 
test positive scenario for the core function in the business logic - process();
test that negative scenarios raises exception;
