import os, subprocess, openai, requests, sys

# 1. Fetch the PR diff
pr = sys.argv[sys.argv.index('--pr')+1]
repo = os.environ['GITHUB_REPOSITORY']
token = os.environ['GITHUB_TOKEN']
headers = {'Authorization': f'token {token}'}
diff = requests.get(
    f'https://api.github.com/repos/{repo}/pulls/{pr}',
    headers=headers,
    params={'mediaType': 'diff'}
).text

# 2. Ask ChatGPT for a review
openai.api_key = os.environ['OPENAI_API_KEY']
prompt = f"""You are ReviewAgent. Here's a PR diff:
{diff}

1. Summarize what changed.
2. Point out any style, testing, or architecture issues.
3. Suggest concrete improvements."""
resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)
review = resp.choices[0].message.content

# 3. Post the review as a PR comment
requests.post(
    f'https://api.github.com/repos/{repo}/issues/{pr}/comments',
    headers=headers,
    json={'body': review}
)