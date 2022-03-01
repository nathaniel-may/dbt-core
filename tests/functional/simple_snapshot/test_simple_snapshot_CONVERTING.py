from test.integration.base import DBTIntegrationTest, use_profile
from datetime import datetime
import pytz
import dbt.exceptions
import pytest


NUM_SNAPSHOT_MODELS = 1

def models(self):
    return "models"

def run_snapshot(self):
    return self.run_dbt(['snapshot'])

def dbt_run_seed_snapshot(self):
    if self.adapter_type == 'postgres':
        self.run_sql_file('seed_pg.sql')
    else:
        self.run_sql_file('seed.sql')

    results = self.run_snapshot()
    assert len(results) == self.NUM_SNAPSHOT_MODELS

def assert_case_tables_equal(self, actual, expected):
    # this does something different on snowflake, but here it's just assertTablesEqual
    self.assertTablesEqual(actual, expected)

def assert_expected(self):
    self.run_dbt(['test'])
    self.assert_case_tables_equal('snapshot_actual', 'snapshot_expected')


def project_config(self):
    return {
        'config-version': 2,
        "seed-paths": ['seeds'],
        "snapshot-paths": ['snapshots-pg'],
        'macro-paths': ['macros'],
    }



# def test_ref_snapshot(project):
#     path = os.path.join(project.snapshot_data_dir, "seed_pg.sql")
#     project.run_sql_file(path)

#     results = self.run_dbt(['run'])
#     assert len(results) == 1

# def test__postgres__simple_snapshot(self):
#     self.dbt_run_seed_snapshot()

#     self.assert_expected()

#     self.run_sql_file("invalidate_postgres.sql")
#     self.run_sql_file("update.sql")

#     results = self.run_snapshot()
#     assert len(results) == self.NUM_SNAPSHOT_MODELS

#     self.assert_expected()



def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models-checkall"

def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        'macro-paths': ['macros-custom-snapshot', 'macros'],
        'snapshot-paths': ['snapshots-checkall'],
        'seeds': {
            'quote_columns': False,
        }
    }

def _run_snapshot_test(self):
    self.run_dbt(['seed'])
    self.run_dbt(['snapshot'])
    database = self.default_database
    results = self.run_sql(
        'select * from {}.{}.my_snapshot'.format(database, self.unique_schema()),
        fetch='all'
    )
    assert len(results) == 3
    for result in results:
        assert len(result) == 6

    self.run_dbt(['snapshot', '--vars', '{seed_name: seed_newcol}'])
    results = self.run_sql(
        'select * from {}.{}.my_snapshot where last_name is not NULL'.format(database, self.unique_schema()),
        fetch='all'
    )
    assert len(results) == 3

    for result in results:
        # new column
        assert len(result) == 7
        assert result[-1] is not None

    results = self.run_sql(
        'select * from {}.{}.my_snapshot where last_name is NULL'.format(database, project.unique_schema()),
        fetch='all'
    )
    assert len(results) == 3
    for result in results:
        # new column
        assert len(result) == 7

def test_postgres_renamed_source(self):
    self._run_snapshot_test()


def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        'macro-paths': ['macros-custom-snapshot', 'macros'],
        'snapshot-paths': ['snapshots-pg-custom'],
    }

# TODO: are teh next 2 tests teh same as up above?
def test__postgres_ref_snapshot(self):
    self.dbt_run_seed_snapshot()
    results = self.run_dbt(['run'])
    assert len(results) == 1

def test__postgres__simple_custom_snapshot(self):
    self.dbt_run_seed_snapshot()

    self.assert_expected()

    self.run_sql_file("invalidate_postgres.sql")
    self.run_sql_file("update.sql")

    results = self.run_snapshot()
    assert len(results) == self.NUM_SNAPSHOT_MODELS

    self.assert_expected()


def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        'macro-paths': ['macros-custom-snapshot', 'macros'],
        'snapshot-paths': ['snapshots-pg-custom-namespaced'],
    }

def test__postgres__simple_custom_snapshot_namespaced(self):
    self.dbt_run_seed_snapshot()

    self.assert_expected()

    self.run_sql_file("invalidate_postgres.sql")
    self.run_sql_file("update.sql")

    results = self.run_snapshot()
    assert len(results) == self.NUM_SNAPSHOT_MODELS

    self.assert_expected()


def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        'macro-paths': ['macros-custom-snapshot', 'macros'],
        'snapshot-paths': ['snapshots-pg-custom-invalid'],
    }

def run_snapshot(self):
    return self.run_dbt(['snapshot'], expect_pass=False)

def test__postgres__simple_custom_snapshot_invalid_namespace(self):
    self.dbt_run_seed_snapshot()


def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models"

def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        "snapshot-paths": ['snapshots-select',
                            'snapshots-pg'],
        'macro-paths': ['macros'],
    }

def test__postgres__select_snapshots(self):
    self.run_sql_file('seed_pg.sql')

    results = self.run_dbt(['snapshot'])
    assert len(results) == 4
    self.assertTablesEqual('snapshot_castillo', 'snapshot_castillo_expected')
    self.assertTablesEqual('snapshot_alvarez', 'snapshot_alvarez_expected')
    self.assertTablesEqual('snapshot_kelly', 'snapshot_kelly_expected')
    self.assertTablesEqual('snapshot_actual', 'snapshot_expected')

    self.run_sql_file("invalidate_postgres.sql")
    self.run_sql_file("update.sql")

    results = self.run_dbt(['snapshot'])
    assert len(results) == 4
    self.assertTablesEqual('snapshot_castillo', 'snapshot_castillo_expected')
    self.assertTablesEqual('snapshot_alvarez', 'snapshot_alvarez_expected')
    self.assertTablesEqual('snapshot_kelly', 'snapshot_kelly_expected')
    self.assertTablesEqual('snapshot_actual', 'snapshot_expected')

def test__postgres_exclude_snapshots(self):
    self.run_sql_file('seed_pg.sql')
    results = self.run_dbt(['snapshot', '--exclude', 'snapshot_castillo'])
    assert len(results) == 3
    self.assertTableDoesNotExist('snapshot_castillo')
    self.assertTablesEqual('snapshot_alvarez', 'snapshot_alvarez_expected')
    self.assertTablesEqual('snapshot_kelly', 'snapshot_kelly_expected')
    self.assertTablesEqual('snapshot_actual', 'snapshot_expected')

def test__postgres_select_snapshots(self):
    self.run_sql_file('seed_pg.sql')
    results = self.run_dbt(['snapshot', '--select', 'snapshot_castillo'])
    assert len(results) == 1
    self.assertTablesEqual('snapshot_castillo', 'snapshot_castillo_expected')
    self.assertTableDoesNotExist('snapshot_alvarez')
    self.assertTableDoesNotExist('snapshot_kelly')
    self.assertTableDoesNotExist('snapshot_actual')


def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        "snapshot-paths": ['snapshots-select-noconfig'],
        "snapshots": {
            "test": {
                "target_schema": self.unique_schema(),
                "unique_key": "id || '-' || first_name",
                'strategy': 'timestamp',
                'updated_at': 'updated_at',
            },
        },
        'macro-paths': ['macros'],
    }


NUM_SNAPSHOT_MODELS = 1
def setUp(self):
    super().setUp()
    self._created_schemas.add(
        self._get_schema_fqn(self.default_database, self.target_schema()),
    )


def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models"

def project_config(self):
    paths = ['snapshots-pg']
    return {
        'config-version': 2,
        'snapshot-paths': paths,
        'macro-paths': ['macros'],
    }

def target_schema(self):
    return "{}_snapshotted".format(self.unique_schema())

def run_snapshot(self):
    return self.run_dbt(['snapshot', '--vars', '{{"target_schema": {}}}'.format(self.target_schema())])

def test__postgres__cross_schema_snapshot(self):
    self.run_sql_file('seed_pg.sql')

    results = self.run_snapshot()
    assert len(results) == self.NUM_SNAPSHOT_MODELS

    results = self.run_dbt(['run', '--vars', '{{"target_schema": {}}}'.format(self.target_schema())])
    assert len(results) == 1


def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models"

def project_config(self):
    return {
        'config-version': 2,
        "snapshot-paths": ['snapshots-invalid'],
        'macro-paths': ['macros'],
    }

def test__postgres__invalid(self):
    with pytest.raises(dbt.exceptions.ParsingException) as exc:
        self.run_dbt(['compile'], expect_pass=False)

    assert 'Snapshots must be configured with a \'strategy\'' in str(exc.exception)


NUM_SNAPSHOT_MODELS = 2
def _assertTablesEqualSql(self, relation_a, relation_b, columns=None):
    # When building the equality tests, only test columns that don't start
    # with 'dbt_', because those are time-sensitive
    if columns is None:
        columns = [c for c in self.get_relation_columns(relation_a) if not c[0].lower().startswith('dbt_')]
    return super()._assertTablesEqualSql(relation_a, relation_b, columns=columns)

def assert_expected(self):
    super().assert_expected()
    self.assert_case_tables_equal('snapshot_checkall', 'snapshot_expected')

def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        "snapshot-paths": ['snapshots-check-col'],
        'macro-paths': ['macros'],
    }


def project_config(self):
    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        "snapshot-paths": ['snapshots-check-col-noconfig'],
        "snapshots": {
            "test": {
                "target_schema": self.unique_schema(),
                "unique_key": "id || '-' || first_name",
                "strategy": "check",
                "check_cols": ["email"],
            },
        },
        'macro-paths': ['macros'],
    }


    def _assertTablesEqualSql(self, relation_a, relation_b, columns=None):
        revived_records = self.run_sql(
            '''
            select
                id,
                updated_at,
                dbt_valid_from
            from {}
            '''.format(relation_b),
            fetch='all'
        )

        for result in revived_records:
            # result is a tuple, the updated_at is second and dbt_valid_from is latest
            assert isinstance(result[1], datetime)
            assert isinstance(result[2], datetime)
            assert result[1].replace(tzinfo=pytz.UTC) == result[2].replace(tzinfo=pytz.UTC)

        if columns is None:
            columns = [c for c in self.get_relation_columns(relation_a) if not c[0].lower().startswith('dbt_')]
        return super()._assertTablesEqualSql(relation_a, relation_b, columns=columns)

    def assert_expected(self):
        super().assert_expected()
        self.assertTablesEqual('snapshot_checkall', 'snapshot_expected')


    def project_config(self):
        return {
            'config-version': 2,
        'seed-paths': ['seeds'],
            "snapshot-paths": ['snapshots-check-col-noconfig'],
            "snapshots": {
                "test": {
                    "target_schema": self.unique_schema(),
                    "unique_key": "id || '-' || first_name",
                    "strategy": "check",
                    "check_cols" : "all",
                    "updated_at": "updated_at",
                },
            },
            'macro-paths': ['macros'],
        }



def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models"

def run_snapshot(self):
    return self.run_dbt(['snapshot'])

def project_config(self):
    return {
        'config-version': 2,
        "snapshot-paths": ['snapshots-longtext'],
        'macro-paths': ['macros'],
    }

def test__postgres__long_text(self):
    self.run_sql_file('seed_longtext.sql')
    results = self.run_dbt(['snapshot'])
    assert len(results) == 1

    with self.adapter.connection_named('test'):
        status, results = self.adapter.execute(
            'select * from {}.{}.snapshot_actual'.format(self.default_database, self.unique_schema()),
            fetch=True
        )
    assert len(results) == 2
    got_names = set(r.get('longstring') for r in results)
    assert got_names == {'a' * 500, 'short'}



def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models-slow"

def run_snapshot(self):
    return self.run_dbt(['snapshot'])

def project_config(self):
    return {
        "config-version": 2,
        "snapshot-paths": ['snapshots-slow'],
        "test-paths": ["test-snapshots-slow"],
    }

def test__postgres__slow(self):
    results = self.run_dbt(['snapshot'])
    assert len(results) == 1

    results = self.run_dbt(['snapshot'])
    assert len(results) == 1

    results = self.run_dbt(['test'])
    assert len(results) == 1



def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models-slow"

def run_snapshot(self):
    return self.run_dbt(['snapshot'])

def project_config(self):
    return {
        "config-version": 2,
        "snapshot-paths": ['snapshots-changing-strategy'],
        "test-paths": ["test-snapshots-changing-strategy"],
    }

def test__postgres__changing_strategy(self):
    results = self.run_dbt(['snapshot', '--vars', '{strategy: check, step: 1}'])
    assert len(results) == 1

    results = self.run_dbt(['snapshot', '--vars', '{strategy: check, step: 2}'])
    assert len(results) == 1

    results = self.run_dbt(['snapshot', '--vars', '{strategy: timestamp, step: 3}'])
    assert len(results) == 1

    results = self.run_dbt(['test'])
    assert len(results) == 1


# These tests uses the same seed data, containing 20 records of which we hard delete the last 10.
# These deleted records set the dbt_valid_to to time the snapshot was ran.
NUM_SNAPSHOT_MODELS = 1
def schema(self):
    return "simple_snapshot_004"

def models(self):
    return "models"

def project_config(self):
    paths = ['snapshots-pg']

    return {
        'config-version': 2,
        'seed-paths': ['seeds'],
        "snapshot-paths": paths,
        'macro-paths': ['macros'],
    }

def test__postgres__snapshot_hard_delete(self):
    self.run_sql_file('seed_pg.sql')
    self._test_snapshot_hard_delete()

def _test_snapshot_hard_delete(self):
    self._snapshot()

    self.assertTablesEqual("snapshot_expected", "snapshot_actual")

    self._invalidated_snapshot_datetime = None
    self._revived_snapshot_datetime = None

    self._delete_records()
    self._snapshot_and_assert_invalidated()
    self._revive_records()
    self._snapshot_and_assert_revived()

def _snapshot(self):
    begin_snapshot_datetime = datetime.now(pytz.UTC)
    results = self.run_dbt(['snapshot', '--vars', '{invalidate_hard_deletes: true}'])
    assert len(results) == self.NUM_SNAPSHOT_MODELS

    return begin_snapshot_datetime

def _delete_records(self):
    database = self.default_database

    self.run_sql(
        'delete from {}.{}.seed where id >= 10;'.format(database, self.unique_schema())
    )

def _snapshot_and_assert_invalidated(self):
    self._invalidated_snapshot_datetime = self._snapshot()

    database = self.default_database

    snapshotted = self.run_sql(
        '''
        select
            id,
            dbt_valid_to
        from {}.{}.snapshot_actual
        order by id
        '''.format(database, self.unique_schema()),
        fetch='all'
    )

    assert len(snapshotted) == 20
    for result in snapshotted[10:]:
        # result is a tuple, the dbt_valid_to column is the latest
        assert isinstance(result[-1], datetime)
        assert result[-1].replace(tzinfo=pytz.UTC) >= self._invalidated_snapshot_datetime

def _revive_records(self):
    database = self.default_database

    revival_timestamp = datetime.now(pytz.UTC).strftime(r'%Y-%m-%d %H:%M:%S')
    self.run_sql(
        '''
        insert into {}.{}.seed (id, first_name, last_name, email, gender, ip_address, updated_at) values
        (10, 'Rachel', 'Lopez', 'rlopez9@themeforest.net', 'Female', '237.165.82.71', '{}'),
        (11, 'Donna', 'Welch', 'dwelcha@shutterfly.com', 'Female', '103.33.110.138', '{}')
        '''.format(database, self.unique_schema(), revival_timestamp, revival_timestamp)
    )

def _snapshot_and_assert_revived(self):
    self._revived_snapshot_datetime = self._snapshot()

    database = self.default_database

    # records which weren't revived (id != 10, 11)
    invalidated_records = self.run_sql(
        '''
        select
            id,
            dbt_valid_to
        from {}.{}.snapshot_actual
        where dbt_valid_to is not null
        order by id
        '''.format(database, self.unique_schema()),
        fetch='all'
    )

    assert len(invalidated_records) == 11
    for result in invalidated_records:
        # result is a tuple, the dbt_valid_to column is the latest
        assert isinstance(result[1], datetime)
        assert result[1].replace(tzinfo=pytz.UTC) >= self._invalidated_snapshot_datetime

    # records which weren't revived (id != 10, 11)
    revived_records = self.run_sql(
        '''
        select
            id,
            dbt_valid_from,
            dbt_valid_to
        from {}.{}.snapshot_actual
        where dbt_valid_to is null
        and id IN (10, 11)
        '''.format(database, self.unique_schema()),
        fetch='all'
    )

    assert len(revived_records) == 2
    for result in revived_records:
        # result is a tuple, the dbt_valid_from is second and dbt_valid_to is latest
        assert isinstance(result[1], datetime)
        # there are milliseconds (part of microseconds in datetime objects) in the
        # invalidated_snapshot_datetime and not in result datetime so set the microseconds to 0
        assert result[1].replace(tzinfo=pytz.UTC) >= self._invalidated_snapshot_datetime.replace(microsecond=0)
        assert result[2] is None
