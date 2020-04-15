# Github Friend

Intersect github repositories stargazers with your following & followers

## Install

Create Personal Access Token and paste it in `./token.txt` ([might help](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line))

```
▶ git clone https://github.com/eLoopWoo/github-friend.git
▶ cd github-friend
▶ echo $TOKEN > token.txt # github personal access token
▶ pip install -r requirements.txt
```

## Example

```
▶ python3 main.py -r kelseyhightower/nocode
```

## Helper

```
▶ python3 main.py -h
usage: main.py [-h] -r REPO_NAME [-l LOGGING_PATH] [-o OUTPUT_PATH]

Github Friend

optional arguments:
  -h, --help            show this help message and exit
  -r REPO_NAME, --repo-name REPO_NAME
                        repository name
  -l LOGGING_PATH, --log LOGGING_PATH
                        output path
  -o OUTPUT_PATH, --output OUTPUT_PATH
                        output path
```

## Help & Guidance

Create issues with the specific problem.
Any further questions or requests Tweet me [@tomereyz](https://twitter.com/tomereyz)

## Authors

* **Tomer Eyzenberg** - *Initial work* - [eLoopWoo](https://github.com/eLoopWoo)
