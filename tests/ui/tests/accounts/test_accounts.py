from tests.ui.services.basic import login


def test_basic_login(py):
    login(py)
    py.visit("http://127.0.0.1:8000/")
    py.get("[name='username']").type('Mark')
    py.get("[name='password']").type('F1shcake')
    py.get("[type='submit']").submit()
    assert py.contains('Your Recent Results')