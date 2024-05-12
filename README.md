# YourTwitterAccountData

## Requirements

First download your twitter archive on the root of this directory

Link:

https://help.twitter.com/en/managing-your-account/how-to-download-your-x-archive
https://help.twitter.com/en/managing-your-account/how-to-download-your-x-archive

To make the code work you will need to have Python and Pip installed in your computer

Link to download python: https://www.python.org/downloads/

Link to download pip: https://pip.pypa.io/en/stable/installation/

Link to download google chrome: https://www.google.com/intl/fr_fr/chrome/ 


Download selenium:

```bash
    pip install selenium
```

To connect your twitter well you must have atleast 1 google chrome profil otherwise it won't work

Link to have the path of your google chrome: profile https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/

Then first login to your twitter account with your google profile by running this 

```bash
   python login_to_twitter.py
```

Then to get your data just run 

```bash
   python main.py
```

And you will see all your twitter data on a print and a data.json file
