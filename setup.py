from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="img2sketch",
    version="0.0.4",
    description="A Python package to convert your photos into pencil art or pencil sketch.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pavansai018/img2sketch_terminal",
    author="Pavan Sai Eshwar Chandra",
    author_email="bpavansai1998@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        
        
        "Programming Language :: Python :: 3.7",
        
    ],
    packages=["img2sketch"],
    include_package_data=True,
    install_requires=["opencv-python","numpy"],
    entry_points={
    "console_scripts": [
    "img2sketch=img2sketch.img2sketch:main",
    ]
    }
   
)