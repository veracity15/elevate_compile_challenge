## Challenge

- Create a GitHub workflow that does the following
  - Builds the image defined by the Dockerfile
  - Runs when a commit is pushed
  - Runs the tests using `pytest src/test_app.py`

- Compile libtiff 4.7.1 from https://gitlab.com/libtiff/libtiff
  - Ensure that libtiff is installed under the `/usr/` prefix
  - Configure libtiff to use `zstd` compression

The task is complete when a GitHub action has passing tests on a commit.

Make your changes on a fork of this repo.

Make a pull request from your fork to this repo with your final work.
