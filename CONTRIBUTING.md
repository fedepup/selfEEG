# Contributing

Thank you for considering contributing to our project! We highly appreciate your
effort towards enhancing our project.

SelfEEG is designed to help building self-supervised learning (SSL) experiments on
electroencephalography (EEG) data, hoping that various teams working on this or
related areas will find this project useful for their research purposes.

Before getting started, please take a moment to review the following guidelines to
ensure a smooth collaboration.

## Table of Contents
* [Before you start](#Before-you-start)
* [How to Contribute](#How-to-contribute)
  * [Reporting Issues](#Reporting-issues)
  * [Suggesting Enhancements](#Suggesting-enhancements)
* [Getting Started](#Getting-started)
* [Set up a Python virtual environment](#Set-up-a-Python-virtual-environment)
* [Submitting Pull Requests](#Submitting-Pull-Requests)
* [License](#License)

## Before you start

If you are new to selfEEG or self-supervised learning in general, we recommend you
do the following before start working on the code:

 * Read the [Code of Conduct](https://github.com/MedMaxLab/selfEEG)
 * Familiarize yourself with the library. Introductory notebooks in the
   [Notebooks](https://github.com/MedMaxLab/selfEEG/Notebooks) folder are a
   good starting point.
 * Read about the self-supervised learning paradigm. The literature offers many
   review papers about this topic. Our recent
   [review](https://doi.org/10.1109/ACCESS.2023.3344531) can be a good
   starting point.

## How to contribute

You can contribute to this library by reporting and/or solving issues, or by
proposing and/or implementing novel features. Both contributions are very welcome.


### Reporting issues

If you come across any issues or bugs in the project, you can report them via our
[issue](https://github.com/MedMaxLab/selfEEG/issues) section.
Please ensure that you provide sufficient information to reproduce the issue.

### Suggesting enhancements

If you have any suggestions for new features, improvements or enhancements,
you can either open a new issue detailing your proposal or write directly to our
group. We highly value your input and will gladly review your suggestions.

The following (not exhaustive) list of possible additions,
sorted by priority order, can be used as a reference:

* add novel self-supervised learning algorithms
* add novel reproducibility features
* add models for EEG-analysis
* improve data augmentation performances
* add functionalities for other biosignals often included in EEG data analysis

## Getting started
To start contributing, follow these simple steps:

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch for your contribution.
4. Set up a python virtual environment.
5. Make necessary changes/additions to the source code.
6. Commit your changes using descriptive commit messages.
7. Push your changes to your forked repository.
8. Open a pull request to our repository, describing your changes and their benefits.
9. Wait for our review and discuss together with us how to merge your additions.

More details about setting your working environment and how to prepare your pulling
request can be found in the next sections.


## Set up a Python virtual environment

To work on your changes you first need to setup a virtual environment.
Just create a fresh environment, activate it and pip install the library with its
dependencies.

We suggest working with conda (or miniconda), where a new environment can be easily
created with the following commands:

```
conda create -n selfeegDev python=3.11
conda activate selfeegDev
```
To install the library with its dependencies, run the following command using the
project main directory as the working directory:
```
pip install -e .
```
this will install all the selfeeg main dependencies. As reported in the
[README.md](README.md) file, we suggest to also add jupyter-lab, matplotib,
and scikit-learn, which can facilitate the development and testing of
novel features.

## testing

It is important to ensure that all the implemented changes will not break any
existing library functionality. The [test](/test) folder provides an automatic
way to check all the library functionalities. Tests will be performed automatically
via GitHub Actions whenever changes to the test, selfeeg, or .github/workflows
folders are pushed to the remote repository. However, these tests are performed
only on a CPU device. For this reason, it is strongly suggested to perform tests
locally before any push in order to evaluate the functionalities of selfEEG also on
a GPU device.
Local tests can be performed with unittest by simply running the following command
using the main repository directory as the working directory:

```
python3 -m unittest discover test "*_test.py"
```
If you want to run only a specific test and not the entire battery, you can run
the following command, changing the syntax according to the specific test
```
python3 -m unittest test.EEGself.module.python_filename.UnittestClass.test_function

for example

python3 -m unittest test.EEGself.ssl.ssl_test.TestSSL.test_BYOL
```

Remember to add test functionalities if you are working on novel features.
More detail about tests can be found in the readme file in the test folder.


## Submitting Pull Requests

If you believe that your changes are ready for possible merging with our main
branch, it is time to send us a pull request, clearly explaining your changes and
their purpose. Before submitting a pull request we kindly ask you to ensure that:

1. Existing tests can be run without errors
2. Novel tests were added to check that an issue is solved or a novel feature works
   correctly.
4. Additions are properly documented and ready to be included without errors in our
   API documentation.
6. The code style follow that of the project. In particular, check that:
   * Indentations follow a 4 space rule.
   * Comments are provided wherever necessary for clarity.
   * The input arguments order is similar to that of other similar functions.
   * Functions follow the `lower_case_with_underscores` name format.
   * Classes follow the `CapitalizedWords` name format.
7. commit messages are clear, descriptive, and provide concise summaries that
   conveys its purpose.

After submitting a pull request, rest assured that everything will be done to
provide a response as soon as possible.

## License

By contributing to this project, you agree that your contributions will be licensed
under the project's [license](LICENSE.md) (MIT License).
