# Copyright 2020 winshare
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()




setuptools.setup(
    name="d-arth", # Replace with your own username
    version="0.0.2",
    author="Winshare Tom",
    author_email="tanwenxuan@live.com",
    description="The Satellite Imagery DataSet Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OOXXXXOO/DARTH",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "certifi==2020.6.20",
        "decorating==0.6.1",
        "esdk-obs-python==3.20.1",
        "GDAL==3.1.0",
        "numpy",
        "olefile==0.46",
        "Pillow==7.1.2",
        "python-slugify==3.0.3",
        "text-unidecode==1.2",
        "tqdm==4.46.1"
    ],
    python_requires='>=3.6',
)
