# Myntra GENZ Section — Selenium Automation Framework

## Tech Stack
- Python 3.x · Selenium 4 · Behave (BDD) · Page Object Model · Allure Reports

## Project Structure
```
myntra_genz_automation/
├── features/
│   ├── environment.py              # Behave hooks (driver setup, teardown, screenshots)
│   ├── tc01_e2e_dresses.feature    # TC-01 E2E — Women's Western Wear → Dresses
│   ├── tc02_positive_tshirts.feature
│   ├── tc03_positive_kurtas.feature
│   ├── tc04_positive_casual_shoes.feature
│   ├── tc05_positive_skincare.feature
│   ├── tc06_negative_jewellery.feature
│   └── tc07_negative_heels.feature
├── steps/
│   └── genz_steps.py              # All step definitions
├── pages/
│   ├── base_page.py               # Common Selenium utilities
│   ├── home_page.py               # HomePage + GenzPage
│   ├── product_listing_page.py    # Filter, sort, product cards
│   ├── product_detail_page.py     # Size, wishlist, Add to Bag
│   └── checkout_page.py           # BagPage + CheckoutPage
├── utils/
│   ├── config.py                  # YAML + env var config loader
│   └── screenshot_utils.py        # Screenshot on failure
├── config/
│   └── config.yaml                # Base URL, browser, timeouts
├── reports/
│   └── screenshots/               # Auto-created on failure
├── behave.ini
└── requirements.txt
```

## Setup

```bash
# 1. Clone / unzip project
cd myntra_genz_automation

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. ChromeDriver — webdriver-manager handles this automatically
```

## Running Tests

```bash
# All tests
behave

# Specific test case by tag
behave --tags=@tc01
behave --tags=@tc02
behave --tags=@negative
behave --tags=@positive
behave --tags=@smoke

# Run E2E only
behave --tags=@e2e

# Headless mode
HEADLESS=true behave

# Firefox
BROWSER=firefox behave

# With Allure reporting
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure serve reports/allure-results
```

## Test Cases Summary

| TC | Category | Product | Type |
|----|----------|---------|------|
| TC-01 | Women's Western Wear | Dresses | E2E |
| TC-02 | Men's Casual Wear | T-Shirts | Positive |
| TC-03 | Men's Occasion Wear | Kurtas | Positive |
| TC-04 | Men's Footwear | Casual Shoes | Positive |
| TC-05 | Beauty & Grooming | Skincare | Positive |
| TC-06 | Accessories | Jewellery | Negative |
| TC-07 | Women's Footwear | Heels | Negative |

## Notes
- All waits are explicit (no `time.sleep` except listing refresh guard)
- Screenshots saved to `reports/screenshots/` on each failure
- Browser and headless mode configurable via env vars or `config/config.yaml`
- Locators use multiple CSS fallbacks to handle Myntra's dynamic class names
