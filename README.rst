
***********
monkeypatch
***********

Reusable django/wagtail app that will patch django's migration code to reduce migration size, especially for streamfield blocks in wagtail.

Credits
-------
This is just a packaging of the code in these to articles and all credits to the author, Cynthia Kiser:
https://cynthiakiser.com/blog/2022/01/06/trimming-wagtail-migration-cruft.html
https://cynthiakiser.com/blog/2022/01/06/trimming-django-migration-cruft.html

Tested with:

* Python version 3.12.2
* Django version 5.0.2
* Wagtail version 6.0.1

Clone main repository:

.. code-block:: bash

    $ git clone https://github.com/weholt/monkeypatch.git    
    $ cd monkeypatch 
    $ pip install .

Or

.. code-block:: bash

    $ pip install git+https://github.com/weholt/monkeypatch.git

Add monkeypatch at the top of your installed apps:

.. code-block:: bash

    INSTALLED_APPS = [
        "monkeypatch",
    ]

Now the commands makemigrations and migrate will be patched.

