# docker-ipython-selenium-client

Selenium client with ipython installed, perfect for interactive tests.

This examples will use new networking feature of docker so in order to run them
you need to create a network: `selenium_net` and then all contaiers should conenct to it

To run interactive ipython environment with a firefox browser you can us this commands
    $ docker network create --driver bridge selenium_net
    $ docker run -e no_proxy=localhost --network=selenium_net --name selenium_firefox -d -p 4444:4444 -p 5900:5900 selenium/standalone-firefox-debug
    $ docker run -it --rm -v $(pwd):/wrk -w /wrk brightit/ipython-selenium ipython
    ...
    In [1]: from selenium import webdriver; from selenium.webdriver.common.keys import Keys; from selenium.webdriver.common.by import By; from selenium.webdriver.support.ui import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC
    In [2]: browser = webdriver.Remote(command_executor='http://selenium_firefox:4444/wd/hub', desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    In [3]: browser.get("http://www.bright-it.com")
    In [4]: browser.close()
    In [5]: exit();


To run `script.py` in your current directory here you can run this:

    $ docker run -it --rm --network=selenium_net -v "$(pwd):/wrk" -w /wrk brightit/ipython-selenium python script.py
