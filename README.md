# JonesBackend

Backend API for the Jones restauraunt.

**How to run**

- cd into the directory, with Pipenv installed run the following command: `pipenv install`
- rename `dev.env` to `.env`. Optional and highly recommended: use your own securely generated `SECRET_KEY` and plug it into the .dev file.
- Go into the pipenv shell with: `pipenv shell`
- run the Flask server with: `flask run`

To run the tests use: `pytest -v `

**API Functionality**

`/api/place-order` : place order. `POST` request, must supply a JSON in the following format:

> {

    "customer_name": name,
    "dish": dish,
    "comments": comments

}

Customer_name and dish must not be empty. Dish must exist on the menu otherwise the API will return an error.

`/api/orders` : last orders. `GET` request - a JSON of all of the orders placed in the last day, in the following format:

```
[
    {
        order_time: "Sun, 31 Oct 2021 10:21:39 GMT",
        id: 123,
        customer_name: foo,
        dish: pizza,
        comments: without cheese
    },
    {
        order_time: "Sun, 31 Oct 2021 12:05:34 GMT",
        id: 128,
        customer_name: bar,
        dish: bar,
        comments: without onion
    }
]
```
