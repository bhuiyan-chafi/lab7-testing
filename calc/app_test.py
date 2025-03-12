import app as main_app
import pytest

flask_app = main_app.app

def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def test_mul_positive_numbers():
    assert mul(2,3) == 6
def test_mul_negative_numbers():
    assert mul(-2,-3) == 6
def test_mul_mixed_numbers():
    assert mul(-2,3) == -6  
def test_mul_zero():
    assert mul(0,3) == 0
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1,0)

# Client based testing
def test_add():
    with flask_app.test_client() as client:
        response = client.get('/add?a=1&b=2')
        assert response.status_code == 200
        assert response.json['s'] == 3
        
def mock_save_last(op,args,res):
    print(f"Mock save_last: {op} {args} {res}", flush=True)

main_app.mock_save_last = mock_save_last 