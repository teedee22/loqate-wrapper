# Loqate wrapper

## Summary
Rest endpoint wrapping Loqate's geolocation service

![Interaction Diagram](./docs/interaction-diagram.png)

## Endpoints
| Endpoint | REST | Description |
|---|---|---|
|/ | GET | *returns a healthcheck message* |
| /loqate | POST | *returns * |

## Payload
POST /loqate (json)
```json
{
    "countrycode": "GBR",
    "postcode": "SW1A2AH",
    "secretkey": "API_KEY"

}
```
Expected return:
```json
[
    {
        "Latitude": "51.5024",
        "Longitude": "-0.1281",
        "Name": "King Charles Street, London"
    }
]
```