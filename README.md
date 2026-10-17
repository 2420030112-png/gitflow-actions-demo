# Gitflow Actions Demo

A small Python calculator project for demonstrating Gitflow branching and
continuous integration with GitHub Actions.

## Features

- Addition, subtraction, multiplication, and division operations.
- Explicit `ZeroDivisionError` handling for division by zero.
- Unit tests written with Python's built-in `unittest` framework.
- Flake8 linting in local development and GitHub Actions.
- Automated checks on pushes and pull requests.

## Requirements

- Python 3.12
- Git

## Run locally

From the repository root, create and activate a virtual environment if
desired, then install the development dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the tests and lint checker:

```powershell
python -m unittest discover -v
flake8 .
```

## Project structure

```text
gitflow-actions-demo/
├── .github/
│   └── workflows/
│       └── python.yml
├── calculator.py
├── requirements.txt
├── test_calculator.py
└── README.md
```

## Gitflow workflow

This project uses three branch levels:

1. `main` contains stable, completed releases.
2. `develop` is the integration branch for completed features.
3. `feature/calculator` is a short-lived branch for calculator work.

The feature branch is merged into `develop` through a pull request. After
integration checks pass, `develop` can be merged into `main` for a release.

### Example Git commands

The repository currently has no commit. Create the first commit on `main`
before creating or pushing the other branches:

```powershell
cd C:\Users\Pavan\gitflow-actions-demo
git switch -c main
git add .
git commit -m "Add calculator Gitflow demo"
git push -u origin main
```

Create and publish the integration branch:

```powershell
git switch -c develop
git push -u origin develop
```

Create and publish the feature branch:

```powershell
git switch -c feature/calculator
git add calculator.py test_calculator.py requirements.txt .github/workflows/python.yml README.md
git commit -m "Add calculator and Python CI workflow"
git push -u origin feature/calculator
```

Open a pull request on GitHub from `feature/calculator` into `develop`.
After the pull request checks pass and it is reviewed, merge it on GitHub.
Then update the local integration branch:

```powershell
git switch develop
git pull origin develop
```

For a release, open a second pull request from `develop` into `main`.

## GitHub Actions verification

1. Open the repository on GitHub.
2. Select the **Actions** tab.
3. Select **Python CI**.
4. Open the latest workflow run for the push or pull request.
5. Confirm that **Install dependencies**, **Run Flake8**, and
   **Run unit tests** each have green check marks.

A successful run means the tested commit passed linting and all unit tests
under Python 3.12.
