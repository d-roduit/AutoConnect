# AutoConnect

AutoConnect is a simple Python application created to make my life easier. It allows quick connection to Facebook or Instagram from a single button.

## Project Status
> Last updated on April 18, 2020 :warning:

## How to use this application ?

A few requirements are to noted before being able to use this application.

1. Python *(3.7 or higher)* must be installed on your machine.
2. The webdrivers of the browser you want to use (Chrome / Firefox) must be added to the PATH.<br>To add the webdriver to the PATH, consult the following page: [Driver requirements](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
3. Your own credentials must be put in the `credentials.py` file if you want to be able to connect to Facebook or Instagram automatically via the application.
4. You're good to go !!

🎉 You can now launch the application via your terminal or Python's IDLE.

## How AutoConnect works under the hood ?

The **AutoConnect** application relies on 2 dependencies :
1. The InternetBot class : A class I created to ease the use of [Selenium](https://selenium-python.readthedocs.io/).
2. [tkinter](https://wiki.python.org/moin/TkInter) :  Python's standard GUI package.

The **InternetBot** class also relies on 2 dependencies :
1. [The Selenium library](https://selenium-python.readthedocs.io/)
2. the Python [os module](https://docs.python.org/3/library/os.html)

## Author

👱 [Daniel Roduit](https://www.linkedin.com/in/daniel-roduit/)

## Application icon / Logo

![alt text](./autoConnect.ico "AutoConnect logo")
