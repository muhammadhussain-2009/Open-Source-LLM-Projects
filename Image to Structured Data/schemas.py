from pydantic import BaseModel, Field
from typing import List, Optional

class ProductAttribute(BaseModel):
    
    value: str

class StructuredProduct(BaseModel):
    """A single product extracted from an image."""
    name: str
    brand: Optional[str]
    price: Optional[float]
    currency: Optional[str]
    attributes: List[ProductAttribute]
    summary: str

# These are the ones the error is looking for:
class ProductCollection(BaseModel):
    """A collection of all products found in the image."""
    products: List[StructuredProduct]

class InvoiceData(BaseModel):
    """A single invoice or line item extracted from an image."""
    date: str
    total_amount: float
    items: List[str]

class InvoiceCollection(BaseModel):
    """A collection of invoices or line items found."""
    invoices: List[InvoiceData]