## docsdk-python

This is the official Python SDK v2 for the [DocSDK](https://docsdk.com/api/v2) _API v2_. 
For API v1, please use [v1 branch](https://github.com/dossdk/docsdk-python/tree/v1) of this repository.


![PyPI](https://img.shields.io/pypi/v/cloudconvert)
## Installation

```
 pip install docsdk
```

## Creating API Client

```
  import docsdk
 
  docsdk.configure(api_key = 'API_KEY', sandbox = False)
```

Or set the environment variable `DOCSDK_API_KEY` and use:

```
  import docsdk
 
  docSDK.default()
```

## Creating Jobs

```js
 import docSDK

 docsdk.configure(api_key = 'API_KEY')

 docsdk.Job.create(payload={
     "tasks": {
         'import-my-file': {
              'operation': 'import/url',
              'url': 'https://my-url'
         },
         'convert-my-file': {
             'operation': 'convert',
             'input': 'import-my-file',
             'output_format': 'pdf',
             'some_other_option': 'value'
         },
         'export-my-file': {
             'operation': 'export/url',
             'input': 'convert-my-file'
         }
     }
 })

```

## Downloading Files

DocSDK can generate public URLs for using `export/url` tasks. You can use these URLs to download output files.

```js
exported_url_task_id = "84e872fc-d823-4363-baab-eade2e05ee54"
res = docsdk.Task.wait(id=exported_url_task_id) # Wait for job completion
file = res.get("result").get("files")[0]
res = docsdk.download(filename=file['filename'], url=file['url'])
print(res)
```

## Uploading Files

Uploads to DocSDK are done via `import/upload` tasks (see the [docs](https://docsdk.com/api/v2/import#import-upload-tasks)). This SDK offers a convenient upload method:

```js
job = docsdk.Job.create(payload={
    'tasks': {
        'upload-my-file': {
            'operation': 'import/upload'
        }
    }
})

upload_task_id = job['tasks'][0]['id']

upload_task = docsdk.Task.find(id=upload_task_id)
res = docsdk.Task.upload(file_name='path/to/sample.pdf', task=upload_task)

res = docsdk.Task.find(id=upload_task_id)
```
## Webhook Signing

The node SDK allows to verify webhook requests received from DocSDK.

```js
payloadString = '...'; # The JSON string from the raw request body.
signature = '...'; # The value of the "DocSDK-Signature" header.
signingSecret = '...'; # You can find it in your webhook settings.

isValid = docsdk.Webhook.verify(payloadString, signature, signingSecret); # returns true or false
```

## Unit Tests

```
# Run Task tests
$ python tests/unit/testTask.py

# Run Job tests
$ python tests/unit/testJob.py

# Run Webhook tests
$ python tests/unit/testWebhookSignature.py
 
```


## Integration Tests
```
# Run Integration test for task
$ python tests/integration/testTasks.py 

# Run Integration test for Job
$ python tests/integration/testJobs.py 

```


## Resources

* [API v2 Documentation](https://docsdk.com/api/v2)
* [DocSDK Blog](https://docsdk.com/blog)
