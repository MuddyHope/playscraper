from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from automation.browser_management import BrowserManager
from automation.login_page import LoginPage
from automation.product_page import ProductPage

app = FastAPI(title="Automation API", version="1.0")

class AutomationRequest(BaseModel):
    url: str
    username: str
    password: str
    product: str
    login: bool = True



@app.post("/run-task")
def run_task(request: AutomationRequest):
    """Trigger the automation task via API"""
    try:
        with BrowserManager(headless=not request.debug) as page:
            if request.login:
                login = LoginPage(page)
                if not login.login(request.url, request.username, request.password):
                    raise HTTPException(status_code=400, detail="Login failed")

            product = ProductPage(page)
            names_prices = product.search_product(request.product)
            if names_prices:
                return {"status": "success", "data": names_prices}
            else:
                raise HTTPException(status_code=404, detail="Product not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
