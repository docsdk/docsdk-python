<p align="center">
  <img width="108px" src="https://yuntu-images.oss-cn-hangzhou.aliyuncs.com/xlogo.jpg" />
</p>

<h1 align="center">DocSDK</h1>
<p align="center"><a href="/README.md">English</a> | 中文</p>

## 关于 DocSDK
> DocSDK 是一个在线文件转换的开发工具包。我们支持各类文档的转换，其中包括 pdf、doc、docx、xls、xlsx、ppt、pptx、dwg、caj、svg、html、json、png、jpg 和 gif 等等各种格式的转换，更多转换格式可查看[网站](https://www.docsdk.com/) 。现有八种 SDK 的支持，其中包括 Java、Node.js、PHP、Python、Swift、CLI、AWS-Lambda 和 Laravel。
> 
> **关键词： 文档转换，文件转换，PDF转Word，PDF转PPT，PDF转HTML**

## docsdk-python

> 这是 [DocSDK API](https://www.docsdk.com/docAPI#sdk) 官方的 Python 开发工具包.

![PyPI](https://img.shields.io/pypi/v/docsdk)

### 安装

```
 pip install docsdk
```

### 创建 API Client

```
  import docsdk
 
  docsdk.configure(api_key = 'API_KEY', sandbox = False)
```

或者使用环境变量 `DOCSDK_API_KEY`：

```
  import docsdk
 
  docSDK.default()
```

### 创建 Jobs

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

### 下载文件

DocSDK 可以使用 `export/url` 生成公开的链接，您可以使用这些 URL 下载输出文件。

```js
res = docsdk.Job.wait(job_id) # Wait for job completion
file = res.get("result").get("files")[0]
res = docsdk.download(filename=file['filename'], url=file['url'])
print(res)
```

### 上传文件

可通过 `import/upload` 上传文件。这是一种简单的上传方法：

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


### 参考资源
* [DocSDK API 文档](https://www.docsdk.com/docAPI)
* [DocSDK 主页](https://www.docsdk.com/)
