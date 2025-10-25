# Memechat QA Automation Suite

End-to-end mobile test automation for Memechat that validates the critical user journey:
  
  1.creating (test) Gmail accounts
  
  2.signing up inside the app
  
  3.logging in, and
  
  4.navigating core screens to verify stability and UX flows.



# Tech Stack

Language: Python
Mobile Drivers: Appium (Android), ADB utilities

Web/Signup Helpers: Selenium (for web email verification pages if needed)

Test Runner: pytest

Patterns: Page Object Model (POM), data-driven tests

Reporting: Allure (or pytest-html)

Device Farm : BrowserStack

Secrets: .env + OS keychain/secret manager
