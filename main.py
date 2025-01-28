import collections
from sqlite3.dbapi2 import paramstyle

import pytest
import psycopg2 as ps
from psycopg2 import OperationalError
import os
import dotenv
from psycopg2.extras import DictCursor
from psycopg2.extras import NamedTupleCursor
import psycopg2
delete_id = collections.defaultdict(list)
def awfj(name_table,param):

    delete_id[name_table].append(param)
    return  delete_id

awfj("places", 2)
awfj("places", 5)
awfj("mater", 5)

for line in delete_id:
    print(line)
    for dd in delete_id[line]:
        print(dd)


print(delete_id.items())
