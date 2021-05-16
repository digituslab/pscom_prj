import pytest
from pscom import *
import time

def test_object_instantiation():
    object = Pscom()
    assert object != None

port_name_list = [
    ('COM0',False),
    ('COM1',False),
    ('COM2',False),
    ('COM3',True),
    ('COM4',False),
    ('COM5',False),
    ('COM6',False),
    ('COM7',False),
    ('COM8',False),
    ('COM9',False),
    ('COM10',False)
]

def test_sending_text():
    time.sleep(1)
    object = Pscom()
    object.open_port('COM3',9600)
    result = object.send_text("GUEST")
    assert result != "ERROR"

@pytest.mark.parametrize("port_name,expected",port_name_list)
def test_opening_a_port(port_name:str,expected:bool):
    object = Pscom()
    result = object.open_port(port_name,9600)
    assert result == expected


