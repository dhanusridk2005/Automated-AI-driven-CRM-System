from setuptools import setup, find_packages

setup(
    name="crm_email_classifier",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "imaplib",
        "email",
        "sqlite3",
        "ollama",
        "datetime"
    ],
    entry_points={
        'console_scripts': [
            'crm_email_classifier=main:main',
        ],
    },
    author="Your Name",
    author_email="your-email@gmail.com",
    description="A CRM email classifier that categorizes emails and stores them in a SQLite database.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/dhanusridk2005/Automated-AI-driven-CRM-System",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)