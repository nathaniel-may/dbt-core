from dbt.adapters.postgres import PostgresAdapter
from dbt.logger import GLOBAL_LOGGER as logger  # noqa


class RedshiftAdapter(PostgresAdapter):

    @classmethod
    def type(cls):
        return 'redshift'

    @classmethod
    def date_function(cls):
        return 'getdate()'

    @classmethod
    def dist_qualifier(cls, dist):
        dist_key = dist.strip().lower()

        if dist_key in ['all', 'even']:
            return 'diststyle {}'.format(dist_key)
        else:
            return 'diststyle key distkey("{}")'.format(dist_key)

    @classmethod
    def sort_qualifier(cls, sort_type, sort):
        valid_sort_types = ['compound', 'interleaved']
        if sort_type not in valid_sort_types:
            raise RuntimeError(
                "Invalid sort_type given: {} -- must be one of {}"
                .format(sort_type, valid_sort_types)
            )

        if type(sort) == str:
            sort_keys = [sort]
        else:
            sort_keys = sort

        formatted_sort_keys = ['"{}"'.format(sort_key)
                               for sort_key in sort_keys]
        keys_csv = ', '.join(formatted_sort_keys)

        return "{sort_type} sortkey({keys_csv})".format(
            sort_type=sort_type, keys_csv=keys_csv
        )
