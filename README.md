# Demo of Django in graphql

This is a demo with a simple crud.

* Django
* Graphql

> 1.get all

```
query{
  allCategorys{
    id
    name
  }
  
}
```

> 2.get by id
```
query{
  categorys(id:2){
    id
    name
  }
  
}
```

> 3.post to create
```
mutation addcategory{
  createCategory(name:"newcat"){
    category{
      id
      name
    }
  }
}
```

> 4.put to update or modify
```
mutation updatecategory{
  updateCategory(id:5,name:"newcat3"){
    category{
      id
      name
    }
  }
}
```

> 5.delete by id
```
mutation deletecategory{
  deleteCategory(id:6){
    category{
      id
      name
    }
  }
}
```
