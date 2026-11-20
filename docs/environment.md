# Development environment

Windows PowerShell: install free Python 3.13 (prefer latest security patch in this series) and Git from official sites if absent. Python 3.12 is supported by declared dependencies; 3.13 is the tested interpreter. Run from repository root:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.lock
.\.venv\Scripts\python.exe -m pip check
```

No activation or administrator permissions required. Linux equivalent: `python3.13 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.lock`. Day 1 uses pytest's src path, not package installation. Later add packaging/CLI entry point if required.

## Free tools and versions

- Python: PSF licence, https://docs.python.org/3.13/license.html ; Git: GPLv2, https://git-scm.com/about/free-and-open-source .
- openpyxl 3.1.5 (MIT): https://pypi.org/project/openpyxl/3.1.5/ ; defusedxml 0.7.1 (PSF): https://pypi.org/project/defusedxml/0.7.1/ ; pytest 9.0.2 (MIT): https://pypi.org/project/pytest/9.0.2/ . Transitive dependencies pinned; licences are available from package metadata: et-xmlfile MIT, iniconfig MIT, packaging BSD/Apache, pluggy MIT, Pygments BSD-2-Clause, colorama BSD-3-Clause. No paid dependencies.
- Planned, not installed: Airflow 3.4.0 (Apache-2.0), PostgreSQL 17 family (PostgreSQL licence), Linux Docker Engine/Compose. Airflow official prerequisites list Python 3.13 and PostgreSQL 17 support: https://airflow.apache.org/docs/apache-airflow/stable/installation/prerequisites.html ; https://www.postgresql.org/about/licence/ . Pin exact container patch/digest and official Airflow constraints at Day 4; keep separate orchestration constraints to avoid dependency conflicts. Airflow runs in WSL2/Linux containers, not native Windows. Docker Desktop is optional and free for personal use subject to terms: https://docs.docker.com/subscription-billing/desktop-license/ ; no subscription activation.

No cloud, trial, student credits, payment card, paid CI or paid API needed. Day 1 tests need neither Docker nor PostgreSQL. `requirements.lock` pins the dependency graph by version; hashes and supply-chain verification are not yet implemented.
