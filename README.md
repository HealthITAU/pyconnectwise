[![Health IT Logo](https://healthit.com.au/wp-content/uploads/2019/06/HIT-proper-logo.png)](https://healthit.com.au)

# pyConnectWise - An API library for ConnectWise Manage and ConnectWise Automate, written in Python

pyConnectWise is a full-featured, type annotated API client written in Python for the ConnectWise APIs based off their OpenAPI schemas. 

This library has been developed with the intention of making the ConnectWise APIs simple and accessible to non-coders while allowing experienced coders to utilize all features the API has to offer without the boilerplate.

pyConnectWise currently supports both ConnectWise Manage and ConnectWise Automate.

Features:
=========
- **100% API Coverage.** All endpoints and response models have had their code generated from the ConnectWise Manage and ConnectWise Automate OpenAPI schemas.
- **Non-coder friendly.** 100% annotated for full IDE auto-completion. Clients handle requests and authentication - just plug the right details in and go!
- **Fully annotated.** This library has a strong focus on type safety and type hinting. Models are declared and parsed using [Pydantic](https://github.com/pydantic/pydantic)

pyConnectWise is currently in **pre-release**. This means that while it does work, you may come across issues and inconsistencies. 

As all Endpoint and Model code has been generated, not all of it has been tested. YMMV.

Endpoint generation is custom-built, but Pydantic models have been generated using a customised fork of [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)

Known Issues:
=============
- Currently only parses **Response** models. No input models yet.
- As this project is still a WIP, documentation or code commentary may not always align.

Roadmap:
=============
- **Automate API Support** - Done :white_check_mark:
- **Robust error handling** - In Progress :construction: 
- **Input model validation** - Planned :chart_with_upwards_trend: 
- **ScreenConnect (Control) API Support** - Planned :chart_with_upwards_trend:
- **Batch requests** - Planned :chart_with_upwards_trend:

How-to:
=============
- [Install](#install)
- [Initializing the API Clients](#initialize-api-client)
  - [ConnectWise Manage](#connectwise-manage)
  - [ConnectWise Automate](#connectwise-automate)
- [Working with Endpoints](#working-with-endpoints)
  - [Get Many](#get-many)
  - [Get One](#get-one)
  - [Get With Params](#get-with-params)
  - [Path Parameters](#child-endpoints)
- [Pagination](#pagination)
- [Additional Configuration](#additional-configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [Supporting the project](#supporting-the-project)

# Install
Open a terminal and run ```pip install pyconnectwise```

# Initializing the API Clients

### ConnectWise Manage
```python
from pyconnectwise import ConnectWiseManageAPIClient

# init client
manage_api_client = ConnectWiseManageAPIClient(
  # your company name,
  # manage instance url,
  # your api client id,
  # your api public key,
  # your api private key,
  # optionally, a Config object for customizing API interactions. See [Additional Configuration].
)
```

### ConnectWise Automate
```python
from pyconnectwise import ConnectWiseAutomateAPIClient

# init client
automate_api_client = ConnectWiseAutomateAPIClient(
  # your automate url
  # your client id
  # automate api username
  # automate api password,
  # optionally, a Config object for customizing API interactions. See [Additional Configuration].
)
```


# Working with Endpoints
Endpoints are 1:1 to what's available for both the ConnectWise Manage and ConnectWise Automate as code is generated from their OpenAPI spec.

For more information, check out the following resources:
- [ConnectWise Manage REST API Docs (requires ConnectWise Developer account)](https://developer.connectwise.com/Products/ConnectWise_PSA/REST)
- [ConnectWise Automate REST API Docs (requires ConnectWise Developer account)](https://developer.connectwise.com/Products/ConnectWise_Automate/Integrating_with_Automate/API/REST)

### Get many
```python
### Manage ###

# sends GET request to /company/companies endpoint
companies = manage_api_client.company.companies.get()

### Automate ###

# sends GET request to /clients endpoint
clients = automate_api_client.clients.get()
```

### Get one
```python
### Manage ###

# sends GET request to /company/companies/{id} endpoint
company = manage_api_client.company.companies.id(250).get()

### Automate ###

# sends GET request to /clients/{id} endpoint
client = automate_api_client.clients.id(250).get()
```

### Get with params
```python
### Manage ###

# sends GET request to /company/companies with a conditions query string
conditional_company = manage_api_client.company.companies.get(params={
  'conditions': 'company/id=250'
})

### Automate ###
# sends GET request to /clients endpoint with a condition query string
# note that the Automate API expects the string 'condition' where-as the Manage API expects the string 'conditions'
conditional_client = automate_api_client.clients.get(params={
  'condition': 'company/id=250'
})
```

# Child Endpoints
The ConnectWise APIs have many instances of endpoints with path parameters - for example, ```/company/companies/{company_id}/sites```

This also exists in the library. Endpoints provide an ```id``` method for setting the ID and traversing down the path.

##### Example using ```/company/companies/{company_id}/sites```
```python
# equivalent to GET /company/companies/250/sites  
sites = manage_api_client.company.companies.id(250).sites.get()
```

# Pagination
The ConnectWise Manage API paginates data for performance reasons through the ```page``` and ```pageSize``` query parameters. ```pageSize``` is limited to a maximum of 1000.

To make working with paginated data easy, Endpoints that implement a GET response with an array also supply a ```paginated()``` method. Under the hood this wraps a GET request, but does a lot of neat stuff to make working with pages easier.

Working with pagination
```python
# initialize a PaginatedResponse instance for /company/companies, starting on page 1 with a pageSize of 100
paginated_companies = manage_api_client.company.companies.paginated(1,100)

# access the data from the current page using the .data field
page_one_data = paginated_companies.data

# if there's a next page, retrieve the next page worth of data
paginated_companies.get_next_page()

# if there's a previous page, retrieve the previous page worth of data
paginated_companies.get_previous_page()

# iterate over all companies on the current page
for company in paginated_companies:
  # ... do things ...
  
# iterate over all companies in all pages
# this works by yielding every item on the page, then fetching the next page and continuing until there's no data left
for company in paginated_companies.all():
  # ... do things ...
```

# Additional Configuration
As of version ```0.4.6```, pyConnectWise clients now accept a new ```Config``` object for additional API interaction configuration.

### Implementation

```python
from pyconnectwise import ConnectWiseManageAPIClient, ConnectWiseAutomateAPIClient
from pyconnectwise.config import Config

# create an instance of Config with your own changes...
config = Config(max_retries = 5)

# ... and hand off to the clients during initialization
manage_api_client = ConnectWiseManageAPIClient(config = config)
automate_api_client = ConnectWiseAutomateAPIClient(config = config)
```

### Supported Options
As of version ```0.4.6```, the following Config options are supported:
* ```max_retries``` - The number of times to re-attempt a request if a HTTP 500 error occurs. Defaults to 3.

# Examples

### Get all agreements, then all additions for an agreement
```python
agreements = api.finance.agreements.paginated(1, 1000)
for agreement in agreements.all():
    additions = api.finance.agreements.id(agreement.id).additions.get()
```

### Get all service tickets with an ID > 1000
```python
tickets = api.service.tickets.get(params={
    'conditions': 'id > 1000'
})
```

# Contributing
Contributions to the project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

When working on the project, please note that there's a few requirements you'll need to install in order to run the project locally. These requirements are stored in [requirements.txt](requirements.txt)

You can install these requirements by opening a terminal, navigating to the repo's directory and running ```pip install -r requirements.txt```

# Supporting the project
:heart: the project and would like to show your support? Please consider donating to the following charities:
- [Black Dog](https://donate.blackdoginstitute.org.au/)
- [Cure4 CysticFibrosis Foundation](https://app.etapestry.com/onlineforms/Cure4CFFoundation/Donatenow.html)
- [Vinnies CEO Sleepout](https://www.ceosleepout.org.au/donation)
- [Care.org.au's Ukraine Humanitarian Crisis fund](https://www.care.org.au/appeals/ukraine-humanitarian-crisis/)
- [RedFrogs Australia](https://redfrogs.com.au/support/donate)
- [Love Your Sister (Sam's 1000)](https://www.loveyoursister.org/makeadonation)
