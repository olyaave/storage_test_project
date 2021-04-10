# storage_test_project

 <p>Storage for files with Http access. It was developed using the Django framework.</p>

## Running 

Clone the repository:
```
git clone https://github.com/olyaave/storage_test_project.git
cd storage_test_project
```

## API

### Upload
```
POST /upload/
```
### Download
```
POST /download/
``` 
In the request body, specify the hash of the file for download.
```
{
    "hash_name": "{hash_name}"
}
```

### Delete
```
POST /delete/
``` 
In the request body, specify the hash of the file for delete.
```
{
    "hash_name": "{hash_name}"
}
```

With gunicorn+nginx, you can run this application as a daemon.

Thank you!
