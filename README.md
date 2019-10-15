# juice-box
Get juiced, brah.

## Getting Started ##
Clone the repo into a directory of your choosing:

`$ git clone git@github.com:dannytannertantrum/juice-box.git`

Bring up the containers with `docker-compose`:

`$ docker-compose -d --build`
If this is your first time running the application, use the `--build` flag. Use `-d` for detached mode if you wish to run the containers in the background.

### That's it! ###
Your app should be running at http://127.0.0.1:5000/


## Testing with Pytest ##
Shell into the `api` container from the root directory:
`$ docker exec api`

Within the container, run pytest to run all tests:
`$ pytest`

To run one test file at a time:
`$ pytest path/to/file/test_file.py`


## Helpful Commands ##
To use bash in the `api` container, run the following in the root directory:
`$ docker exec -it juice-box_api_1 /bin/bash`
