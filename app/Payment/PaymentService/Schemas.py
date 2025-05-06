from datetime import datetime

from dataclasses import dataclass, field
from Directory.DirectoryService.Schemas import StatusSchema, TypeSchema, CategorySchema, SubcategorySchema


@dataclass
class PaymentSchema():
    """DTO Платежа"""
    status: StatusSchema
    payment_type: TypeSchema
    category: CategorySchema
    subcategory: SubcategorySchema
    amount: float
    create_date: datetime = field(default=datetime.now())
    id: int | None = field(default=None)
    comment: str = field(default='')
    hr_create_date: float = field(init=False)

    def __post_init__(self):
        self.hr_create_date = self.create_date.strftime('%d-%m-%y')


@dataclass
class PaymentFilter():
    """DTO Фильтра платежей"""
    payment_type_id: int | None = field(default=None)
    category_id: int | None = field(default=None)
    subcategory_id: int | None = field(default=None)
    status_id: int | None = field(default=None)
    timeEnd: datetime | None = field(default=None)
    timeStart: datetime | None = field(default=None)

    def to_dict(self):
        self.normalize()
        return self.__dict__.copy()

    def normalize(self):
        self.timeEnd = datetime.strptime(
            self.timeEnd, '%Y-%m-%dT%H:%M') if self.timeEnd else None
        self.timeStart = datetime.strptime(
            self.timeStart, '%Y-%m-%dT%H:%M') if self.timeStart else None
        self.status_id = int(self.status_id) if self.status_id else None
        self.category_id = int(self.category_id) if self.category_id else None
        self.subcategory_id = int(
            self.subcategory_id) if self.subcategory_id else None
        self.payment_type_id = int(
            self.payment_type_id) if self.payment_type_id else None
