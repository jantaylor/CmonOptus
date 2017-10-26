# CmonOptus

CmonOptus is a python3 script which runs speed tests every now and again, to see whether the speeds that you're currently getting; are similar to that of what you pay for.

## Credit

These users helped me improve this script.
- [gregsifr](https://github.com/gregsifr)
- [sp0](https://github.com/sp0)

## Dependencies
- [pyspeedtest](https://github.com/fopina/pyspeedtest)
- [tweepy](https://github.com/tweepy/tweepy)
- [pyyaml](https://github.com/yaml/pyyaml)

# Installation
## Part A - Downloading the files

### Installing Dependencies

All three dependencies can be installed you Python's package manager, [pip](https://pip.pypa.io/en/stable/installing/)
Once you have pip installed, you can install three dependencies with

```
pip install pyspeedtest tweepy pyyaml
```

### Installing CmonOptus

#### Option 1 - Downloading here
Simply press the download button on this page, then proceed to press 'Download as ZIP'.

#### Option 2 - Downloading through Git
1. Firstly, you will need to download Git.
2. To do this you need to navigate to the following page: [git.](https://git-scm.com/).
3. You should then hit the download button which can be found on that page.
4. After downloading, install the software as you would any other (just hit next...)
5. Navigate to your desired directory in Terminal/Command Prompt and execute the following command;
```git clone https://github.com/slavkobojanic/CmonOptus```
6. If you check the folder that you designated to put it in; you should see a folder called 'CmonOptus'.

## Part B - Creating a Twitter App
1. Head to the (Twitter App Site)[https://app.twitter.com/].
2. Hit 'Create New App'.
3. Fill in the form displayed (only name, description, and website are needed), and agree to the developer agreement.
4. Hit 'Create App'.
5. You are now on your app management page, here you can important app details.
6. Hit the 'Keys and Access Tokens' tab near the top of the page.
7. It will display your consumer key, and consumer secret.
8. To get your access key, and access secret, scroll down and hit 'Create my access token'. The page will refresh and display your access codes.
9. Keep these close-by because they are important for the next part (consumer key, consumer secret, access key, access secret).

## Part C - Setting up the config.yaml file
1. In that /CmonOptus/ folder there is a file named 'config.yaml', open up this file in your favorite text editor and alter the values as needed.
2. Use the values that we got from the last part to fill the first four rows.
3. The ```check_interval``` value should be how often you want the software to run the speed test in seconds (the software randomly generates a time between check_interval*0.75 and check_interval*1.25, to look more legitimate).
4. The ```timeout_interval``` value will set a hard limit on how often CmonOptus can tweet. For example, it has a default of no more than once every hour (3600 seconds).
5. The ```paid_upload_speed``` and ```paid_download_speed``` should be the internet speed promised in your contract, in Mb/s.

## Part D - Running the app.
#### Option A - Simple
1. Simply run the command (this may be different if you choose to rename the file);
```python3 User.py```
2. Monitor the software to make sure it's working properly.
3. Voila.

#### Option B - Advanced
1. You can make as many '.yaml' files as you like with different app details, if you have multiple apps.
2. Run the command;
```python3 User.py (filename).yaml```
2. Monitor the software to make sure it's working properly.
3. Voila.
