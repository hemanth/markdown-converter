from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="markdown-converter",
    version="0.1.1",
    author="Hemanth HM",
    author_email="hemanth.hm@gmail.com",
    description="A Flask-based web service to convert any document/url to Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hemanth/markdown-converter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "flask>=2.0.0",
        "flask-cors>=3.0.0",
        "markitdown>=0.0.1a3",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "markdown-converter=markdown_converter.cli:main",
        ],
    },
)
