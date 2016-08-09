![python:3.5](https://img.shields.io/badge/python-3.5-brightgreen.svg) ![selenium:2.x](https://img.shields.io/badge/selenium-2.x-brightgreen.svg) ![License MIT](https://img.shields.io/badge/license-MIT-blue.svg) [![](https://img.shields.io/docker/stars/brightit/ipython-selenium.svg)](https://hub.docker.com/r/brightit/ipython-selenium 'DockerHub') [![](https://img.shields.io/docker/pulls/brightit/ipython-selenium.svg)](https://hub.docker.com/r/brightit/ipython-selenium 'DockerHub')

[Dockerfile](https://github.com/BrightIT/docker-ipython-selenium-client/blob/master/Dockerfile)

![](https://raw.githubusercontent.com/BrightIT/docker-ipython-selenium-client/master/example.png 'example')

### Prerequisites
Examples below use  `selenium_net` network to make connection between containers, we also use a prebuild selenium container with firefox, you can get both using this commands:

    $ docker network create --driver bridge selenium_net
    $ docker run -e no_proxy=localhost --network=selenium_net --name selenium_firefox -d -p 4444:4444 -p 5900:5900 selenium/standalone-firefox-debug

This will start a `firefox` with vnc access [vnc://localhost:5900](vnc://localhost:5900) and password: `secret` that can be used to run selenium tests.

### Usage - iPython interactive selenium session
Given the above container is running you can run an interactive ipython sessions  as follows:

    $ docker run -it --rm --network selenium_net -v $(pwd):/wrk -w /wrk brightit/ipython-selenium ipython
    ...
    In [1]: from selenium import webdriver; from selenium.webdriver.common.keys import Keys; from selenium.webdriver.common.by import By; from selenium.webdriver.support.ui import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC
    In [2]: browser = webdriver.Remote(command_executor='http://selenium_firefox:4444/wd/hub', desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    In [3]: browser.get("http://www.bright-it.com")
    In [4]: browser.close()
    In [5]: exit();


### Usage - script execution
To run a `script.py` in your current directory here you can run this:

    $ docker run -it --rm --network=selenium_net -v "$(pwd):/wrk" -w /wrk brightit/ipython-selenium python script.py
