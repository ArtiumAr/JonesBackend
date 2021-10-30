def test_correct_order(client):
    """Test that properly structured orders work."""
    rv = client.post('/api/place-order', json={
        "customer_name":"tioma",
        "dish":"pizza",
        "comments": "no onions"
    }, follow_redirects=True).get_json()
    assert rv['order status'] == 'success'

def test_incorrect_order(client):
    """Test that improperly structured orders fail."""
    rv = client.post('/api/place-order', json={
        "customer_name":"",
        "dish":"pizza",
        "comments": "no onions"
    }, follow_redirects=True).get_json()
    assert rv['order status'] == 'failure'

def test_none_menu_orders(client):
    """Test that orders not in menu fail."""
    rv = client.post('/api/place-order', json={
        "customer_name":"",
        "dish":"pizza",
        "comments": "no onions"
    }, follow_redirects=True).get_json()
    assert rv['order status'] == 'failure'


def test_get_orders(client):
    pass
