# Restaurant API Reference


## Orders

### Schema

| Column Name | Type |
| --- | --- |
| table_id | Number |
| menu_items | Collection of Menu |

### Routes

```GET /order```

Gets the list of all the orders

```GET /order/ObjectID```

Gets the order for the given objectId


```POST /order/ObjectID```

Creats a new order with the arguments given in body
table_id -> expects as a string
menu_its -> string of object_ids delimited by commas 


```PUT /order/ObjectID```

Updates the order with the arguments specified in the body for the given objectId


```DELETE /order/ObjectID```

Deletes the order with the given ObjectID



## Menu

### Schema

| Column Name | Type |
| --- | --- |
| title | String |
| description | String |
| price | Number |
| ingridients | Collection of type ingridient |

### Routes

```GET /menu```

Gets the list of all the menus

```GET /menu/ObjectID```

Gets the menu for the given objectId


```POST /menu/ObjectID```

Creats a new menu with the arguments given in body
title -> expects as a string
description -> expects as a string
price -> expects as a number
ingridients -> string of object_ids delimited by commas 

```PUT /menu/ObjectID```

Updates the menu with the arguments specified in the body for the given objectId


```DELETE /menu/ObjectID```

Deletes the menu with the given ObjectID




## Ingridients

### Schema

| Column Name | Type |
| --- | --- |
| name | String |
| description | String |

### Routes

```GET /ingridients```

Gets the list of all the Ingridients

```GET /ingridients/ObjectID```

Gets the Ingridients for the given objectId


```POST /ingridients/ObjectID```

Creats a new ingridient with the arguments given in body
name -> expects as a string
description -> expects as a string 


```PUT /ingridients/ObjectID```

Updates the ingridient with the arguments specified in the body for the given objectId


```DELETE /ingridients/ObjectID```

Deletes the ingridient with the given ObjectID





## Inventory

### Schema

| Column Name | Type |
| --- | --- |
| ingridients | type of Ingridient |
| quantity | Number |

### Routes

```GET /inventory```

Gets the list of all the Inventory items

```GET /inventory/ObjectID```

Gets the Inventory for the given objectId


```POST /inventory/ObjectID```

Creats a new order with the arguments given in body
table_id -> expects as a string
menu_its -> string of object_ids delimited by commas 


```PUT /inventory/ObjectID```

Updates the inventory with the arguments specified in the body for the given objectId


```DELETE /inventory/ObjectID```

Deletes the inventory item with the given ObjectID


