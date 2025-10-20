from playwright.sync_api import Page, TimeoutError
from rapidfuzz import fuzz
from utils.logger import logger


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def is_match(self, name: str, keyword: str, threshold: int = 80):
        """Return True if product name matches any keyword fuzzily."""
        _curr_ration = fuzz.partial_ratio(name.lower(), keyword.lower())
        if _curr_ration >= float(threshold):
            return True
        return False

    def search_product(self, keywords, ratio: int = 70):
        """Search for products that match the keywords using fuzzy logic."""
        try:
            # Wait for inventory container to appear
            self.page.wait_for_selector("#inventory_container", timeout=10000)
            container = self.page.query_selector("#inventory_container")
            products = container.query_selector_all(".inventory_item")

            found_products = []
            for product in products:
                name = product.query_selector(".inventory_item_name").inner_text()
                price = product.query_selector(".inventory_item_price").inner_text()

                if self.is_match(name, keywords, ratio):
                    found_products.append({name: price})

            if not found_products:
                logger.info("No matching products found.")
            return found_products

        except TimeoutError:
            logger.debug("Inventory container not found (timeout).")
        except Exception as e:
            logger.error(f"Error searching products: {e}")
        return []
