# pylint:disable=undefined-all-variable
""" Expose RealBrowserLocust subclasses at package level """
from realbrowserlocusts.locusts import FirefoxLocust, PhantomJSLocust, \
    ChromeLocust, HeadlessChromeLocust, HeadlessFirefoxLocust

__all__ = [
    'FirefoxLocust',
    'PhantomJSLocust',
    'ChromeLocust',
    'HeadlessChromeLocust'
    'HeadlessFirefoxLocust'
]

__version__ = "0.2"
