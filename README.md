<p align="center">
  <img width="108px" src="https://yuntu-images.oss-cn-hangzhou.aliyuncs.com/xlogo.jpg" />
</p>

<h1 align="center">DocSDK</h1>
<p align="center">English | <a href="doc/README-zh-CN.md">中文</a></p>

## About DocSDK

> DocSDK is a development kit for smart file conversion. We support the conversion of various types of documents, including pdf, doc, docx, xls, xlsx, ppt, pptx, dwg, caj, svg, html, json, png, jpg, gif and other formats, more conversion formats can be viewed on our [website](https://www.docsdk.com/). There are 8 kinds of SDK support, including Java, Node.js, PHP, Python, Swift, CLI, AWS-Lambda and Laravel.
> 
> **Keywords: document conversion, file conversion, PDF to Word, PDF to PPT, PDF to HTML**

## docsdk-python

This is the official Python SDK for the [DocSDK API](https://docsdk.com/api/v2).

![PyPI](https://img.shields.io/pypi/v/docsdk)

### Installation

```
 pip install docsdk
```

### Creating API Client

```
  import docsdk
 
  docsdk.configure(api_key = 'API_KEY', sandbox = False)
```

Or set the environment variable `DOCSDK_API_KEY` and use:

```
  import docsdk
 
  docSDK.default()
```

### Creating Jobs

```js
 import docSDK

 docsdk.configure(api_key = 'API_KEY')

 docsdk.Job.create(payload={
     "tasks": {
         'ImportURL': {
              'operation': 'import/url',
              'url': 'https://file-url'
         },
         'ConvertFile': {
             'operation': 'convert',
             'input': 'ImportURL',
             'output_format': 'pdf',
             'some_other_option': 'value'
         },
         'ExportResult': {
             'operation': 'export/url',
             'input': 'ConvertFile'
         }
     }
 })

```

### Downloading Files

DocSDK can generate public URLs for using `export/url` tasks. You can use these URLs to download output files.

```js
res = docsdk.Job.wait(job_id) # Wait for job completion
file = res.get("result").get("files")[0]
res = docsdk.download(filename=file['filename'], url=file['url'])
print(res)
```

### Uploading Files

Uploads to DocSDK are done via `import/upload` tasks. This SDK offers a convenient upload method:

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

### Resources
* [DocSDK API Documentation](https://www.docsdk.com/docAPI)
* [DocSDK home page](https://www.docsdk.com/)

### 关于 DocSDK
> DocSDK 是一个在线文件转换的开发工具包。我们支持各类文档的转换，其中包括 pdf、doc、docx、xls、xlsx、ppt、pptx、dwg、caj、svg、html、json、png、jpg 和 gif 等等各种格式的转换，更多转换格式可查看[网站](https://www.docsdk.com/) 。现有八种 SDK 的支持，其中包括 Java、Node.js、PHP、Python、Swift、CLI、AWS-Lambda 和 Laravel。
> 
> **关键词： 文档转换，文件转换，PDF转Word，PDF转PPT，PDF转HTML**