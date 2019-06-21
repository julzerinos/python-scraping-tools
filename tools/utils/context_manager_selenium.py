from contextlib import contextmanager


@contextmanager
def driver_manager(driver):
    """Context manager for selenium webdriver instances

    Webdriver item is imported in settings.py of the scraping project directory
    """
    d = driver()
    yield d
    d.quit()
