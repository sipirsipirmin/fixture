# Fixture Service

## Environment Variables


| Environment Variablename | Type | Default Value |
|--------------------------|------|----------------|
| FIXTURE_URL              | `string` |`https://apigateway.beinsports.com.tr/api/fixture/rewriteid/current/super-lig` | 
| HOURS_INTERVAL_FEATURE| `int` |`1`|
| HOURS_INTERVAL_PAST| `int` |`2`|
| BIG_TEAMS | `string` | `439,425,2311,4633` |


Please not that `BIG_TEAMS` must be comma seperated numbers. Because slitting process making by comma and result converting to integer.

## Install Dependencies

```
pip3 install -r requirements.txt
```

##  Run Application

### Flask or Gunicorn

```
flask run 
````

or 

```
gunicorn wsgi:app
```

### Docker

```
docker build -t <tag> .
docker run <tag>
``` 