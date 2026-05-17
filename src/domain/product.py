# src/domain/product.py

class Product:
    def __init__(self, sku: str, name: str, base_price: float, shipping_price: float, currency: str):
        self.sku = sku
        self.name = name
        self.base_price = base_price
        self.shipping_price = shipping_price
        self.currency = currency

    @property
    def total_price(self) -> float:
        """Regla de Negocio: El precio real es la suma del precio base y el envío"""
        return self.base_price + self.shipping_price

    def to_dict(self):
        """Utilidad para guardar en MongoDB de forma estructurada"""
        return {
            "sku": self.sku,
            "name": self.name,
            "base_price": self.base_price,
            "shipping_price": self.shipping_price,
            "total_price": self.total_price,
            "currency": self.currency
        }