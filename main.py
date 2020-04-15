import github
import argparse
import json
import os
from tqdm import tqdm

GITHUB_TOKEN = open('token.txt', 'r').read().strip()


def run(github_api, repo_name, output_path, logging_path):
    own_user = github_api.get_user(github_api.get_user().login)
    users = {}
    results = []
    print('[*] Fetch followings...')
    followings = list(own_user.get_following())
    print('[*] Fetch followers...')
    followers = list(own_user.get_followers())
    repository = github_api.get_repo(repo_name)
    print('[*] Fetch stargazers...')
    stargazers = list(repository.get_stargazers())

    print('[*] Generating users list...')
    for user in tqdm(followings + followers):
        users.setdefault(user.login, True)
    print('[*] Generating intersections...')
    with open(logging_path, 'a') as f:
        for c in tqdm(stargazers):
            if users.get(c.login, None):
                f.write('{repository} : {user}\n'.format(repository=repository.html_url, user=c.html_url))
                results.append(c.html_url)
    if os.path.isfile(output_path):
        with open(output_path, 'r') as f:
            json_object = json.load(f)
    else:
        json_object = {}
    with open(output_path, 'w') as f:
        json_object[repository.html_url] = results
        json.dump(json_object, f)
    print('[*] Finished, output in {output}...'.format(output=output_path))


def main():
    parser = argparse.ArgumentParser(description='Github Friend')
    parser.add_argument('-r', '--repo-name', dest='repo_name', type=str,
                        help='repository name', required=True)
    parser.add_argument('-l', '--log', dest='logging_path', type=str,
                        help='output path', required=False, default='log.txt')
    parser.add_argument('-o', '--output', dest='output_path', type=str,
                        help='output path', required=False, default='output.json')
    args = parser.parse_args()
    repo_name = args.repo_name
    output_path = args.output_path
    logging_path = args.logging_path
    github_api = github.Github(GITHUB_TOKEN)
    run(github_api, repo_name, output_path, logging_path)


if __name__ == '__main__':
    main()
