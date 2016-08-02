
import psycopg2

THREAD_MIN = 1
THREAD_MAX = 8

BAD_THREADS_ERROR = """Invalid value given for "threads" in active run-target.
Value given was {supplied} but it should be an int between {min_val} and {max_val}"""

class RedshiftTarget:
    def __init__(self, cfg):
        assert cfg['type'] == 'redshift'
        self.host = cfg['host']
        self.user = cfg['user']
        self.password = cfg['pass']
        self.port = cfg['port']
        self.dbname = cfg['dbname']
        self.schema = cfg['schema']
        self.threads = self.__get_threads(cfg)

    def __get_threads(self, cfg):
        supplied = cfg.get('threads', 1)

        bad_threads_error = RuntimeError(BAD_THREADS_ERROR.format(run_target="...", supplied=supplied, min_val=THREAD_MIN, max_val=THREAD_MAX))

        if type(supplied) != int:
            raise bad_threads_error

        if supplied >= 1 and supplied <= 8:
            return supplied
        else:
            raise bad_threads_error

    def __get_spec(self):
        return "dbname='{}' user='{}' host='{}' password='{}' port='{}'".format(
            self.dbname,
            self.user,
            self.host,
            self.password,
            self.port
        )

    def get_handle(self):
        return psycopg2.connect(self.__get_spec())

