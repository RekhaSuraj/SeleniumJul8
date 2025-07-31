#meaning of below statement: execute delete customer only if both create customer and edit customer is passed

import  pytest

@pytest.mark.run(order=2)
@pytest.mark.dependency(name="edit_customer")
def test_edit_customer():
    print("edit customer")
    assert True


@pytest.mark.run(order=4)
@pytest.mark.dependency(name='logout',depends=['test_create_customer','edit_customer','deletecustomer'])
def test_logout_customer():
    print('logout customer')


@pytest.mark.run(order=3)
#meaning of below statement: execute delete customer only if both create customer and edit customer is passed
@pytest.mark.dependency(name='deletecustomer',depends=["test_create_customer","edit_customer"])
def test_delete_customer():
    print("delete customer")
    assert False


@pytest.mark.run(order=1)
@pytest.mark.dependency(name="test_create_customer")
def test_create_customer():
    print("create customer")
    assert True
