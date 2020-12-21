# internet_conn

Simple programme to establish an outbound socket connection to a configurable host (an always-on host such as `1.1.1.1` by default) to check state of internet connectivity, log any exceptions and suggest a potential root cause/fix.

Boilerplate generated from [**here**](https://www.python-boilerplate.com/py3+executable+gitignore+logging+pytest+tox), skeleton of the function stolen from [**here**](https://stackoverflow.com/a/33117579) and added my own tweaks to it ⇒ quite liked the thinking behind:

"... - Avoid DNS resolution (we will need an IP that is well-known and guaranteed to be available for most of the time)
     - Avoid application layer connections (connecting to an HTTP/FTP/IMAP service)
     - Avoid calls to external utilities from Python or other language of choice (we need to come up with a language-agnostic solution that doesn't rely on third-party solutions)..."

## How To Run
Simply `cd` inside and do:
```
docker build . -f docker/Dockerfile -t internet_conn:<your tag>
docker run --rm internet_conn:<your tag> --env-file docker/sample.env
```
This will install required packages, run a sample unit test, load the env variables (see Known Issues) and bring up the programme.

## What Could Improve
The following would be nice-to-have for an application but could be a bit of an overkill for a script this size and limited time.
  - There is some structure repetition around errno codes in the main snippet, would prefer if I had time to write a dictionary (a switch/case equivalent)
  - I would have preferred to do an initial check when programme comes up to make sure the port we are trying to reach is not blocked on the outbound firewall rules otherwise this whole thing would be a false positive.
  - Make it more Object-oriented with a class and and initialiser

## Known Issues
- I spent some time trying to get the unit test for the socket module to work but it turned out to be pretty challenging, lot more than I initially thought anyway. Even with an external module like `unittest`, it seems quite tricky to mock a socket connection. So I left a sample dummy test there just to demonstrate the docker step for now.
- The other challenge I faced was injecting sample `.env` variables in at docker runtime. The standard `os.getenv` simply didn't do anything so I've left the configurability bit in the code itself for time being and left the sample.env for demonstration purpose (values get overwritten by the ones hard-coded), one for the future I suppose :-)
