from setuptools import setup, find_packages

setup(
    name="rag-evaluator",
    version="0.1.0",
    description="A library for evaluating Retrieval-Augmented Generation (RAG) systems",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="muhammadhussain_2009",
    author_email="mhussain.20094@gmail.com",
    packages=find_packages(),
    install_requires=[
        "torch",
        "sacrebleu",
        "rouge-score",
        "bert-score",
        "transformers",
        "nltk",
        "textblob"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)