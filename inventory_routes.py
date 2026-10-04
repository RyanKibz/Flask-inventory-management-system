from flask import Blueprint, jsonify, request
from data import inventory
from external_api import find_product

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.get("/inventory")
def get_inventory():
    return jsonify(inventory), 200

# Reading
@inventory_bp.get("/inventory/<int:item_id>")
def get_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# POST -> creating
@inventory_bp.post("/inventory")
def add_item():
    data = request.get_json()
    if not data or not data.get("product_name"):
        return jsonify({"error": "Product name is required"}), 400

    new_item = {
        "id": max((item["id"] for item in inventory), default=0) + 1,
        "product_name": data["product_name"],
        "brand": data.get("brand", ""),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }
    inventory.append(new_item)
    return jsonify(new_item), 201
# Patch-> editing
@inventory_bp.patch("/inventory/<int:item_id>")
def update_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "No update data provided"}), 400
    item.update(data)
    return jsonify(item), 200

@inventory_bp.delete("/inventory/<int:item_id>")
def delete_item(item_id):
    item = next(
        (item for item in inventory if item["id"] == item_id),
        None
    )
    if not item:
        return jsonify({"error": "Item not found"}), 404
    inventory.remove(item)
    return jsonify({"message": "Item deleted"}), 200

@inventory_bp.get("/products/search/<barcode>")
def search_product(barcode):
    product = find_product(barcode)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200