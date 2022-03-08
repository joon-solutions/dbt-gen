from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "pyarrow==6.0.1",
    "pyYAML==6.0",
    "pandas==1.3.4",
    "google-cloud-bigquery==2.34.0",
    "snowflake-connector-python==2.7.4",
    "jinja2==3.0.3",
    "tqdm==4.63.0",
]

TEST_REQUIREMENTS = [
    "flake8==4.0.1",
    "black==22.1.0",
    "pytest==7.0.1",
]

setup(
    name="dbt_gen",
    version="0.1.0",
    description="Tool to generate dbt resources.",
    author="Joon Solutions",
    author_email="tien.tq@joonsolutions.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dbt_gen=dbt_gen.cli:main"
        ]
    },
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["templates/*.sql"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
