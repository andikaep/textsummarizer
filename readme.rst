==================
Text Summarizer App
==================

This project is a Django-based web application that provides an API for text summarization using the ``facebook/bart-large-cnn`` model from the Hugging Face Transformers library. The app allows users to input text and get a summarized version in return.

Prerequisites
=============

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.6 or above.
* You have installed Django in your working environment.

Installation
============

Follow these steps to get your development env running:

1. Clone the repository to your local machine:

   .. code-block:: bash

      git clone https://github.com/andikaep/text-summarizer.git

2. Change into the project directory:

   .. code-block:: bash

      cd text-summarizer

3. Install the required packages:

   .. code-block:: bash

      pip install -r requirements.txt

4. Make migrations and migrate the database:

   .. code-block:: bash

      python manage.py makemigrations
      python manage.py migrate

Setting Up the Summarization Model
==================================

To set up the ``facebook/bart-large-cnn`` model, follow these instructions:

1. Ensure you have the transformers library installed:

   .. code-block:: bash

      pip install transformers

2. The application automatically downloads and caches the model when you run it for the first time. However, if you want to pre-download the model, you can run a simple Python script:

   .. code-block:: python

      from transformers import pipeline
      summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

   Running this script will download and cache the model locally.

Usage
=====

To start the server:

.. code-block:: bash

   python manage.py runserver

Open a web browser and go to ``http://127.0.0.1:8000/summarizer/`` to see the application in action. Input your text and click "Summarize Text" to get the summarized text.

Contributing
============

Contributions to this project are welcome. Here are a few ways you can help:

- Report bugs and request features by creating issues.
- Improve documentation.
- Submit pull requests with improvements.

To contribute, clone this repository, create a new branch, make changes, and submit a pull request.

License
=======

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
================

This project uses the following open-source packages:

- Django
- Hugging Face Transformers