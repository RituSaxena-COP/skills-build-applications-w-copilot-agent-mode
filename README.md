# Build Applications with GitHub Copilot Agent Mode

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey RituSaxena-COP!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/RituSaxena-COP/skills-build-applications-w-copilot-agent-mode/issues/1)

---

## Backend quickstart

1. Create & activate venv:

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Install backend requirements:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3. Ensure MongoDB is running (default: mongodb://localhost:27017)

4. Run migrations (note: djongo may have issues with some post-migrate SQL checks; if `migrate` fails during site creation, run the script below):

```bash
python octofit-tracker/backend/manage.py migrate
# If migrate errors out due to djongo SQL parsing, run:
python octofit-tracker/backend/scripts/create_default_site.py
python octofit-tracker/backend/manage.py migrate
```

5. Create a superuser:

```bash
python octofit-tracker/backend/manage.py createsuperuser
```

6. Run the dev server:

```bash
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

