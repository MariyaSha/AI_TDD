const form = document.querySelector('form');
const username = form.elements.username;
const password = form.elements.password;
const register = form.querySelector('[type=submit]');
function validate() {
  const value = password.value;
  const validPassword = Array.from(value).length >= 6 && /[A-Z]/.test(value)
    && /[a-z]/.test(value) && /[0-9]/.test(value)
    && /[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]/.test(value);
  const validUsername = /^[A-Za-z0-9]+$/.test(username.value);
  username.setAttribute('aria-invalid', String(username.value !== '' && !validUsername));
  password.setAttribute('aria-invalid', String(value !== '' && !validPassword));
  document.querySelector('#password-feedback').textContent = value === '' ? '' : validPassword ? 'Password meets all requirements.' : 'Password must meet all requirements.';
  register.disabled = !(validUsername && validPassword);
}
form.addEventListener('input', validate);
window.addEventListener('pageshow', validate);
validate();
const toggle = document.querySelector('#toggle-password');
toggle.addEventListener('click', () => {
  const show = password.type === 'password';
  password.type = show ? 'text' : 'password';
  toggle.textContent = show ? 'Hide password' : 'Show password';
  toggle.setAttribute('aria-pressed', String(show));
});
