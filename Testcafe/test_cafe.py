from playwright.sync_api import Page, expect

def test_cafe(page: Page) -> None:
    page.goto("https://devexpress.github.io/testcafe/example/")
    page.locator("#developer-name").click()
    page.locator("#developer-name").press_sequentially("Kirill", delay=100)
    expect(page.locator("#developer-name")).to_have_value("Kirill")
    page.locator("#windows").click()
    expect(page.locator("#windows")).to_be_checked()
    page.locator("#remote-testing").click()
    expect(page.locator("#remote-testing")).to_be_checked()
    page.locator("#reusing-js-code").click()
    expect(page.locator("#reusing-js-code")).to_be_checked()
    page.locator("#background-parallel-testing").click()
    expect(page.locator("#background-parallel-testing")).to_be_checked()
    page.locator("#continuous-integration-embedding").click()
    expect(page.locator("#continuous-integration-embedding")).to_be_checked()
    page.locator("#traffic-markup-analysis").click()
    expect(page.locator("#traffic-markup-analysis")).to_be_checked()
    page.locator("#tried-test-cafe").click()
    expect(page.locator("#tried-test-cafe")).to_be_checked()
    page.locator("#slider").click()
    page.keyboard.press("ArrowRight")
    expect(page.locator("[tabindex='0']")).to_have_attribute("style", 'left: 55.5556%;')
    page.locator("#comments").click()
    page.locator("#comments").fill("Good comment")
    expect(page.locator("#comments")).to_have_value("Good comment")
    page.locator("#submit-button").click()
    expect(page).to_have_url("https://devexpress.github.io/testcafe/example/thank-you.html")
    expect(page.locator("h1")).to_contain_text("Thank you, Kirill!")
    expect(page.locator("p")).to_contain_text("To learn more about TestCafe, please visit:")






