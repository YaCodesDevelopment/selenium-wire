<<<<<<< HEAD
from .webdriver import Chrome, ChromeOptions
||||||| parent of cd2912e (Support both versions of undetected_chromedriver)
=======
try:
    import undetected_chromedriver as uc
except ImportError as e:
    raise ImportError(
        'undetected_chromedriver not found. '
        'Install it with `pip install undetected_chromedriver`.'
    ) from e

from seleniumwire.webdriver import Chrome

uc._Chrome = Chrome
Chrome = uc.Chrome
ChromeOptions = uc.ChromeOptions  # noqa: F811
>>>>>>> cd2912e (Support both versions of undetected_chromedriver)
