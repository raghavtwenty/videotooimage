from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

setup(
    name="videotooimage",
    version="2024.03.19.1.0.0",
    description="Video to Image converter",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    url="https://github.com/raghavtwenty/videotooimage",
    author="Raghav",
    author_email="raghavtwenty@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["opencv-python"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
