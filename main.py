import os
from from githu import Github
g = Github(os.environ.get("GITHUB_TOKEN"))
repo = g.get_repo("mike_davis_1978@hotmail.com/githubforlinux")

code_content = '''def main():
    print("Hello from src/main.py!")
    if __name__ == "__main__":
        main()
    '''
result = repo.create_file(
    path = "src/main.py", 
    message = "create src/main.py", 
    content = code_content, 
    branch = "main"
    )
print(f"created file at:{result['content'].html_url}")
g.close()