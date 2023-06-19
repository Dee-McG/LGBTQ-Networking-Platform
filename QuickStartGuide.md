## Quick start

### Local IDE Users
Clone the repo:
```
git clone https://github.com/Daisy-McG/LGBTQ-Networking-Platform.git
```

Create virtual environment and activate
```
python -m venv .venv
.venv/Scripts/activate (windows)
source .venv/bin/activate (mac)
```

### Cloud IDE (Gitpod)

Create a new workspace from the main [repo](https://github.com/Daisy-McG/LGBTQ-Networking-Platform)

### Setup (All users)

Create an env.py file at the root directory and add the following

```
import os

os.environ["SECRET_KEY"] = "jr43jk5k3j54345m,madsad"
os.environ["DEVELOPMENT"] = "jr43jk5k3j54345m,madsad"
os.environ["HOST"] = "8000-daisymcg-lgbtqnetworkin-urc3apbybij.ws-eu99.gitpod.io" <--- Replace this with gitpod url - not needed for vscode ect.
os.environ["FULLHOST"] = "https://8000-daisymcg-lgbtqnetworkin-urc3apbybij.ws-eu99.gitpod.io" <--- Replace this with gitpod url - not needed for vscode ect.
```

Install requirements

```
pip install -r requirements.txt
```

Run Migrations

```
python manage.py migrate
```

Start the App

```
python manage.py runserver
```