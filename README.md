[![Health IT Logo](https://healthit.com.au/wp-content/uploads/2019/06/HIT-proper-logo.png)](https://healthit.com.au)

# pyconnectwise - a client for simplifying interactions with the ConnectWise Manage API in Python

pyconnectwise is a full featured, type annotated API client written in Python for the ConnectWise API's. 

This library has been developed with the intention of making the ConnectWise API's simple and accessible to non-coders while allowing experienced coders to utilize all features the API has to offer without the boilerplate.

Currently, it only supports ConnectWise Manage, but more is planned.
- - - - 
Features:
=========
- 100% API Coverage. All endpoints and response schemas have had their code generated from the ConnectWise Manage OpenAPI Schema.
- Beginner and expert friendly.
- Focus on type annotations and DX (Developer Experience). Models are declared and parsed using [Pydantic](https://github.com/pydantic/pydantic)

pyconnectwise is currently in **pre-release**. This means that while it does work, you may come across issues and inconsistencies. 

As all Endpoint and Model code has been generated, not all of it has been tested. YMMV.
- - - - 
Known Issues:
=============
- The ConnectWise API spec doesn't label optional fields correctly - for example, the mergedParentTicket field on a service ticket is only included in an API response if the ticket has a parent.
  - Because these aren't labelled, the models generated can't correctly identify what exactly an optional field is. There's 3 potential solutions for this, all with caveats:
    - Manually edit the schema or models
      - This isn't maintainable - if a new version comes out, it'll need to be re-done. It's also very manual labour intensive.
    - Annotate every field in a model as ```<type> | None```
      - This negatively impacts DX (Developer Experience). Every field would need to be checked for None manually otherwise the type checker would yell at you.
    - Opt out of Pydantic validation altogether.
      - We miss out on the best part of Pydantic this way, and it also introduces the risk of accessing fields (such as ```TicketModel.mergedParentTicket```) without being notified of it potentially being None.
      - This is the option I've opted for for the time being. I'd like to find a better solution to this.
- Currently only parses **Response** models. No input models yet.
- As this project is still a WIP, documentation or code commentary may not always align. 
- Little to no error handling just yet

- - - - 
Planned and in progress:
=============
- Automate API Support
- Input model validation
- Robust error handling

- - - - 
How-to:
======
- [Install](#install)
- [Initialize API client](#initialize-api-client)
- [Working with Endpoints](#working-with-endpoints)
  - [Get](#get)
  - [Child Endpoints](#child-endpoints)
- [Pagination](#pagination)
- [Examples](#examples)

- - - - 
# Install

Open a terminal and run ```pip install pyconnectwise```

- - - - 
# Initialize API client
```python
from pyconnectwise import ConnectWiseManageAPIClient

# init client
api = ConnectWiseManageAPIClient(
  # your company name,
  # manage instance url,
  # your api client id,
  # your api public key,
  # your api private key
)
```

- - - - 
# Working with Endpoints
Endpoints are 1:1 to what's available with ConnectWise Manage as code is generated from their OpenAPI schema.

For more information, check out the [ConnectWise Manage REST API Docs (requires ConnectWise Developer account)](https://developer.connectwise.com/Products/ConnectWise_PSA/REST)

# Get
```python
# sends get request to /company/companies endpoint
companies = api.company.companies.get()
```

# Get one
```python
# sends get request to /company/companies/{id} endpoint
companies = api.company.companies.id(250).get()
```

# Get with params
```python
# sends get request to /company/companies with a condition query string
conditional_get = api.company.companies.get(params={
  'conditions': 'company/id=250'
})
```

# Child Endpoints
The ConnectWise API has many instances of nested endpoints - for example, ```/company/companies/{company_id}/sites```

This is replicated in the library. Endpoints provide an ```id``` method for setting the ID and traversing down the path.

###### Example using ```/company/companies/{company_id}/sites```
```python
sites = api.company.companies.id(250).sites.get()
```

# Pagination
The ConnectWise API paginates data for performance reasons through the ```page``` and ```pageSize``` query parameters. ```pageSize``` is limited to a maximum of 1000.

To make working with paginated data easy, Endpoints that implement a GET response with an array also supply a ```paginated()``` method. Under the hood this wraps a GET request, but does a lot of neat stuff to make working with pages easier.

Working with pagination
```python
# initialize a PaginatedResponse instance for /company/companies, starting on page 1 with a pageSize of 100
paginated_companies = api.company.companies.paginated(1,100)

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
- - - -
# Examples
## Get all agreements, then all additions for an agreement
```python
agreements = api.finance.agreements.paginated(1, 1000)
for agreement in agreements.all():
    additions = api.finance.agreements.id(agreement.id).additions.get()
```

## Get all service tickets with an ID > 1000
```python
tickets = api.service.tickets.get(params={
    'conditions': 'id > 1000'
})
```
