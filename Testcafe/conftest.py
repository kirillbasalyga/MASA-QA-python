import pytest

@pytest.fixture(scope="module")
def shared_page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()