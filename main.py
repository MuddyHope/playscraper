import argparse
from automation.browser_management import BrowserManager
from automation.login_page import LoginPage
from automation.product_page import ProductPage
import config

def main():
    parser = argparse.ArgumentParser(description="Automate product search task")
    parser.add_argument("--product", required=True, help="Product to search for")
    parser.add_argument("--match", required=False, help="Matching Ratio for keywords", default=70)
    args = parser.parse_args()

    with BrowserManager(headless=False) as page:
        login = LoginPage(page)
        if not login.login(config.BASE_URL, config.USERNAME, config.PASSWORD):
            print("Login failed")
            return

        product = ProductPage(page)
        names_prices = product.search_product(args.product, args.match)
        if names_prices:
            print("Task completed successfully!")
            print(names_prices)
        else:
            print("Task failed — product not found.")

if __name__ == "__main__":
    main()
