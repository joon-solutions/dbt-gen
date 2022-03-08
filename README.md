# dbt-gen
Tool for generating dbt model, source files.

## Commands

### 1. Generate dbt project from cookiecutter template

```bash
dbt_gen generate_dbt
```

### 2. Generate source

```bash
dbt_gen generate_source --help
usage: dbt_gen generate_source [-h] [--profile-path PROFILE_PATH]
                               [--profile-name PROFILE_NAME] [--target TARGET]
                               [--database DATABASE] [--threads THREADS]
                               source_folder

positional arguments:
  source_folder         Folder to write source YAML files

optional arguments:
  -h, --help            show this help message and exit
  --profile-path PROFILE_PATH
                        Path to dbt profile YAML. Default is
                        /home/tien/.dbt/profiles.yml
  --profile-name PROFILE_NAME
                        Dbt profile name. Default is `default`.
  --target TARGET       Dbt profile target. Default is `dev`.
  --database DATABASE   Database to inspect. Default is the database in
                        profile.
  --threads THREADS     Max threads. Default is your machine number of
                        threads.
```

### 3. Generate base models

```bash
dbt_gen generate_base_model --help
usage: dbt_gen generate_base_model [-h] [--profile-path PROFILE_PATH]
                                   [--profile-name PROFILE_NAME]
                                   [--target TARGET] [--threads THREADS]
                                   source_path output_folder

positional arguments:
  source_path           Path to dbt source YAML.
  output_folder         Folder to write base models.

optional arguments:
  -h, --help            show this help message and exit
  --profile-path PROFILE_PATH
                        Path to dbt profile YAML. Default is
                        /home/tien/.dbt/profiles.yml
  --profile-name PROFILE_NAME
                        Dbt profile name. Default is `default`.
  --target TARGET       Dbt profile target. Default is `dev`.
  --threads THREADS     Max threads. Default is your machine number of
                        threads.
```