from database import Base, BaseModel
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship


# Association table
product_category = Table(
    'product_category',
    Base.metadata,
    Column('product_id', ForeignKey('products.id', ondelete='CASCADE')),
    Column('category_id', ForeignKey('categories.id', ondelete='CASCADE'))
)

class Product(BaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    image = Column(String)  # Fayl yo'li sifatida
    quantity = Column(Integer, default=0)
    barcode = Column(String, unique=True)

    unit_id = Column(Integer, ForeignKey('units.id', ondelete='SET NULL'), nullable=True)
    unit = relationship('Unit', back_populates='products')

    categories = relationship(
        'Category',
        secondary=product_category,
        back_populates='products'
    )

class Category(BaseModel):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    products = relationship(
        'Product',
        secondary=product_category,
        back_populates='categories'
    )

# Association table
class OrderProduct(Base):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True)
    
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    order = relationship("Order", back_populates="products")

    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"))
    product = relationship("Product", back_populates="orders")

    product_name = Column(String)  # Product nomi o'sha paytdagi holatda
    price = Column(String)         # Narxi buyurtma vaqtida
    count = Column(Integer)        # Buyurtma qilingan miqdor

class Unit(BaseModel):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Client(BaseModel):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    other_info = Column(Text)

class Debt(BaseModel):
    __tablename__ = "debts"

    id = Column(Integer, primary_key=True)
    description = Column(Text)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"), nullable=True)
    total_price = Column(Integer, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)

    order = relationship("Order", back_populates="debts")
    client = relationship("Client")

# Association table
association_debt_sellpayment = Table(
    "debt_sellpayment",
    Base.metadata,
    Column("sell_payment_id", ForeignKey("sell_payments.id", ondelete="CASCADE")),
    Column("debt_id", ForeignKey("debts.id", ondelete="CASCADE"))
)

class SellPayment(BaseModel):
    __tablename__ = "sell_payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))

    order = relationship("Order", back_populates="payments")
    debts = relationship("Debt", secondary=association_debt_sellpayment, backref="sell_payments")

class Order(BaseModel):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    description = Column(Text)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)
    total_price = Column(Integer)

    client = relationship("Client")
    order_products = relationship("OrderProduct", back_populates="order", cascade="all, delete")
    payments = relationship("SellPayment", back_populates="order", cascade="all, delete")
    debts = relationship("Debt", back_populates="order", cascade="all, delete-orphan")

class Setting(BaseModel):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    string = Column(Text)
    number = Column(Integer)

class Data(BaseModel):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    string = Column(Text)
    number = Column(Integer)
