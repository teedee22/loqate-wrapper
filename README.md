# Loqate wrapper

## Summary
Rest endpoint wrapping Loqate's geolocation service

## Endpoints
| Endpoint | REST | Description |
|---|---|---|
|/ | GET | *returns a healthcheck message* |
| /loqate | POST | *returns geolocation data, querying https://api.addressy.com/Geocoding/International/Geocode/v1.10/xmla.ws?* |

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

## CICD

.gitlab-ci will build docker image when a git tag is pushed
registry images can be seen here: https://gitlab.com/teedee22/loqate/container_registry