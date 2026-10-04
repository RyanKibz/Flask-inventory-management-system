import requests

URL = "https://world.openfoodfacts.org/api/v2/product"
HEADERS = {"User-Agent": "InventoryProject/1.0"}


def find_product(barcode):
    try:
        response = requests.get(
            f"{URL}/{barcode}.json",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "barcode": barcode,
            "ingredients": product.get("ingredients_text", "")
        }

    except requests.RequestException as error:
        print("API error:", error)
        return None