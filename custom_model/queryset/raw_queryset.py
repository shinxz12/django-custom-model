from django.db.models.sql.query import RawQuery
from django.db.models.query import RawQuerySet


class BookRawQueryset(RawQuerySet):
    def __init__(self, filters={}, *args, **kwargs):
        """

        :param check_in:
        :type check_in datetime.date
        :param check_out:
        :type check_out datetime.date
        :param filters:
        :param args:
        :param kwargs:
        """
        self.params = []
        self.filters = filters
        super(BookRawQueryset, self).__init__(None, *args, **kwargs)
        self.query = RawQuery(self.sql, using=self.db)

    @property
    def sql(self):
        return '''
        select booking_with_discount.*, max(booking_with_discount.price_discount) as max_price,
        min(booking_with_discount.price_discount) as min_price
        from (
            select book.id,
            discount.name as discount_name,
            CASE
            when discount.discount_percentage is not null and discount.discount_value is not null
            then book.price*(100-discount.discount_percentage)/100 - discount.discount_value
            when discount.discount_percentage is null and discount.discount_value is not null
            then book.price - discount.discount_value
            when discount.discount_percentage is not null and discount.discount_value is null
            then book.price*(100-discount.discount_percentage)/100
            END
            as price_discount
            from custom_model_book as book
            left join custom_model_discount_book as discount_book
            on book.id = discount_book.book_id
            left join custom_model_discount as discount
            on discount.id = discount_book.discount_id
            where book.name='Math book'
            ) as booking_with_discount
        '''

        # def join_many(self)
