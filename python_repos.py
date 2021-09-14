import requests

# Make an API call and store the response.
def get_data_from_github():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    status_code = r.status_code
    print(f"Status code: {status_code}")

    # Store API response in a variable.
    response_dict = r.json()
    total_repositories = response_dict['total_count']
    print(f"Total repositories: {total_repositories}")

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")
    
    return status_code, total_repositories, repo_dicts

get_data_from_github()
