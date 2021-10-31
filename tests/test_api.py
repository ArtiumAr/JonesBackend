def order(client, customer_name, dish, comments):
    rv = client.post(
        "/api/place-order",
        json={"customer_name": customer_name, "dish": dish, "comments": comments},
        follow_redirects=True,
    ).get_json()
    return rv


def test_correct_order(client):
    """Test that properly structured orders work."""
    rv = order(client, "tioma", "pizza", "no onions")
    assert rv["order status"] == "success"


def test_incorrect_order(client):
    """Test that improperly structured orders fail."""
    rv = order(client, "", "pizza", "no onions")
    assert rv["order status"] == "failure"


def test_none_menu_orders(client):
    """Test that orders not in menu fail."""
    rv = order(client, "tioma", "chicken masala", "light on the curry")
    assert rv["order status"] == "failure"


def test_get_orders(client):
    """Test that API properly sends the right amount of orders."""
    order(client, "tioma", "pizza", "no onions")
    order(client, "tioma", "burger", "medium rare")
    order(client, "tioma", "carbonara", "extra pepper")
    rv = client.get("/api/orders").get_json()
    assert len(rv) == 3
