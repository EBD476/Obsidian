
### GET All Filters [GET METHOD]
	- localhost:8084/api/v1/filter/all
### GET Filter By ID  [GET METHOD]
	- localhost:8084/api/v1/filter/id/{filterID}
### Create Filter [POST METHOD]
	- localhost:8084/api/v1/filter/add
[Request Body]
```json
{
  
     "filterName" : "Filter-DATASOURCE-1",
     "filterType": 1,
     "filterConditionType":1,
     "active":1,
     "datasource":{
         "id": 662
     },
     "filterConditions": [
         {
         "fieldName": "CREATED_AT",
         "fieldValue": "2013-05-31",
         "operator": "=",
         "conditionType": 1,
         "valueSource":3
         }
     ]
  }
```

### Delete Filter [DELETE METHOD]
	- localhost:8084/api/v1/filter/remove
  [Request Body]
```json
	  {
	   "id":964
	  }
```

### Run Filter By FilterID [GET METHOD]
	- localhost:8084/api/v1/filter/run/{filterID}
### Run Filter By Filter Body[POST METHOD]
	- localhost:8084/api/v1/filter/run/{filterID}
 [Request Body]
 ```json
   {
  
    "filterName" : "Filter-FMKVSH_CASE_RELATION_ACCOUNTS3",
    "filterType": 1,
    "filterConditionType":1,
    "active":1,
    "datasource":{
        "id": 662
     },
    "filterConditions": [
        {
        "fieldName": "CREATED_AT",
        "fieldValue": "2013-05-31",
        "operator": "=",
        "conditionType": 1,
        "valueSource":3
      }
  }
```
