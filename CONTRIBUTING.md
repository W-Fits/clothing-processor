# Contributing

Please review this document before for guidance on how to make make changes. 

## Structure

```bash
├───.vscode # Editor settings
├───data
│   ├───models # ML Models
│   └───test-images
├───docs 
│   └───images
│   └───DOCS.md
├───scripts
├───utils
├───main.py
├───run_script.py
├───requirements.txt
├───CONTRIBUTING.md # You are here :)
├───README 
├───LICENSE
├───.gitignore
├───.env.example
```

## Development

### Clone on your local machine

```bash
git clone https://github.com/W-Fits/clothing-processor/.git
```

### Navigate to project directory

```bash
cd clothing-processor
```

### Create a new Branch

```bash
git checkout -b new-branch 
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Environment variables

Copy the example `.env` and insert the correct environment variables.
```bash
cp .env.example .env
```

### Pushing changes

```bash
git add .
git commit -a -m "init commit"
git push -u origin new-branch
```

Now you can create a pull request and request reviewers to merge the changes you have made.

### Commit message guidance

We make use of semantic commit messages in our organisation, please follow [this](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) guide for more information.