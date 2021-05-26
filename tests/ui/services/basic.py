"""

Basic services for the UI (pylenium) tests

"""
import pylenium


def login(py: pylenium):
    """
    Log in as user Mark and go to the dashboard
    """
    py.visit('http://127.0.0.1:8000/dashboard')
    py.get("[name='username']").type('Mark')
    py.get("[name='password']").type('F1shcake')
    py.get("[type='submit']").submit()
    assert py.contains('Your Recent Results')
