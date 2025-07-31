# parametrize
import pytest


@pytest.mark.parametrize(['cn','pw'],[('Archana','A123'),('Seema','S123'),('Rama','R123')])
def test_create_customer(cn,pw):
    print(f'create customer: name {cn} password {pw}')

# collecting ... collected 3 items
#
# test_demo3.py::test_create_customer[Archana-A123] PASSED                 [ 33%]create customer: name Archana password A123
#
# test_demo3.py::test_create_customer[Seema-S123] PASSED                   [ 66%]create customer: name Seema password S123
#
# test_demo3.py::test_create_customer[Rama-R123] PASSED                    [100%]create customer: name Rama password R123
