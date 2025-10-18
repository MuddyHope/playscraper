from playwright.sync_api import Page, TimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, url, username, password):
        try:
            self.page.goto(url, timeout=10000)
            self.page.fill("#user-name", username)
            self.page.fill("#password", password)
            self.page.click("#login-button")
            self.page.wait_for_selector("#shopping_cart_container", timeout=10000)
            print("✅ Login successful")
        except TimeoutError:
            print("❌ Login failed: Timeout while logging in")
            return False
        except Exception as e:
            print(f"❌ Login error: {e}")
            return False
        return True
