import pytest
from playwright.sync_api import expect


def test_register_enabled_only_for_valid_fields(page, live_url):
    page.goto(live_url)
    register = page.get_by_role('button', name='Register', exact=True)
    username = page.get_by_label('Username', exact=True)
    password = page.get_by_label('Password', exact=True)
    expect(register).to_be_disabled()
    username.fill('User123')
    expect(register).to_be_disabled()
    password.fill('Abcd1!')
    expect(register).to_be_enabled()
    for invalid in ['', 'a b', 'a_b', 'é', '用户']:
        username.fill(invalid)
        expect(register).to_be_disabled()
        username.fill('User123')
        expect(register).to_be_enabled()
    for invalid in ['', 'Aa1!', 'abcd1!', 'ABCD1!', 'Abcde!', 'Abcde1', 'Abcd1 ', 'Abcd1é', 'Abcd١!']:
        password.fill(invalid)
        expect(register).to_be_disabled()
        password.fill('Abcd1!')
        expect(register).to_be_enabled()
    register.click()
    expect(page.get_by_role('status')).to_have_text('Registration successful')
    expect(password).to_be_empty()


def test_password_visibility_preserves_value(page, live_url):
    page.goto(live_url)
    password = page.get_by_label('Password', exact=True)
    password.fill('Abcd1!')
    expect(password).to_have_attribute('type', 'password')
    page.get_by_role('button', name='Show password', exact=True).click()
    expect(password).to_have_attribute('type', 'text')
    expect(password).to_have_value('Abcd1!')
    page.get_by_role('button', name='Hide password', exact=True).click()
    expect(password).to_have_attribute('type', 'password')
    expect(password).to_have_value('Abcd1!')
    expect(page.get_by_role('status')).to_have_count(0)


@pytest.mark.parametrize('width', [375, 1280])
def test_responsive_guidance_and_feedback(page, live_url, width):
    page.set_viewport_size({'width': width, 'height': 900})
    page.goto(live_url)
    for text in ['At least 6 characters', 'One uppercase ASCII letter (A–Z)',
                 'One lowercase ASCII letter (a–z)', 'One digit (0–9)',
                 'One ASCII punctuation character (e.g. !, @, #)']:
        expect(page.get_by_text(text, exact=True)).to_be_visible()
    username = page.get_by_label('Username', exact=True)
    username.fill('bad name')
    expect(username).to_have_attribute('aria-invalid', 'true')
    expect(page.get_by_text('Use only ASCII letters and digits.', exact=True)).to_be_visible()
    username.fill('Good123')
    expect(username).to_have_attribute('aria-invalid', 'false')
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    box = page.locator('main').bounding_box()
    assert box['width'] <= 560
    for control in page.locator('input, button').all():
        assert control.bounding_box()['height'] >= 44
