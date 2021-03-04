# Python Facebook Automation
A Selenium Script to share Facebook status in multiple groups Automatically

![Instagram-Python-Automation](https://miro.medium.com/max/2400/1*9VryBS4mvUIIViO27i3ymQ.jpeg)

we will be using selenium and the chrome web Driver to get a Facebook post and then share it on multiple Facebook groups with only a couple of steps.

if you have not used the chrome web Driver before it will be installed for the first time(will take only a few seconds), but then it will not be installed each time it’s executed … it will get the setup from the cache. we will provide the link to the post that we want to share, we also need to provide the password and email of the Facebook account that we are using to share.

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
```

if your google chrome is in English you might get an error using this script because it uses a couple of french words when looking for buttons ( words such as Publier = Publish)… because the browser I use at work is in french.
This is not the perfect script, it’s a quick solution that can be further developed.
