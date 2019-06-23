"""
On how to deal with particularly tricky iframes.
    
    * This requires Selenium.

The specific function in question is:
    selenium_driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

The selenium driver then focuses on the iframe and the iframe is treated
as a seperate webpage, isolated from the host page, thus it is not possible
to access both the host page and the iframe at any moment of runtime.

It is recommended to find and scrap the source page of the iframe,
as more often than not the source page is static, thus eliminating
the need for selenium, alas sometimes the source is inaccessible.
"""

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))  # switch focus to iframe

# Alternatively, if the iframe has a name attribute, you may directly reference it by
driver.switch_to.frame("name")

# Access the iframe data

driver.switch_to.default_content()  # switch focus to host page/initial page
