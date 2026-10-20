# User Registration — Specification

Build a simple user registration page using Python and Flask.

Use `wireframe.png` as a reference for the page layout, not its exact appearance. Create a modern, clean, responsive design with clear labels, spacing, and helpful feedback.

## Username
- Required.
- Only ASCII letters (`A–Z`, `a–z`) and digits (`0–9`) are allowed.
- Spaces and other characters are not allowed.

## Password
- Required; at least 6 characters.
- Must contain at least:
  - One uppercase ASCII letter (`A–Z`).
  - One lowercase ASCII letter (`a–z`).
  - One digit (`0–9`).
  - One special ASCII punctuation character (such as `!`, `@`, `#`).
- Spaces and other whitespace do not count as special characters.

## Register
- Include a Register button that is disabled by default.
- Enable the button only when both fields are valid.
- Disable it again if either field becomes invalid.
- Validate the same rules on the server, even if browser validation is bypassed.
- Reject invalid submissions and display a confirmation for successful ones.

## User Interface
- Show clear field labels and password requirements.
- Include a button to show or hide the password without clearing it.
- Make the page usable on desktop and mobile.
- Use accessible form labels and buttons.

## Scope
- Use Flask, HTML, CSS, and minimal vanilla JavaScript.
- No database, account storage, or login system is needed.
- Use pytest for backend tests and Playwright with real Chromium for browser tests.
- Let the AI discover the test cases and implement the features incrementally using TDD. Do not prescribe a fixed number of development cycles.