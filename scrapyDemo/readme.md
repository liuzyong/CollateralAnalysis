## 安装Scrapy  
 ```pip install Scrapy```

## 创建 项目 
  进入自定义的项目目录中，运行下列命令： 
  ```scrapy startproject scrapyDemo ```
  
  得到
  scrapy.cfg: 项目的配置文件。
  scrapyDemo/: 项目的Python模块，将会从这里引用代码。
  scrapyDemo/items.py: 项目的目标文件。设置数据存储模板，用于结构化数据
  scrapyDemo/pipelines.py: 项目的管道文件。数据处理行为，如：一般结构化的数据持久化
  scrapyDemo/settings.py: 项目的设置文件。
  scrapyDemo/spiders/: 存储爬虫代码目录。
## 创建 爬虫
  ```scrapy genspider demo "jscq.com"```
## 启动 爬虫
  ```scrapy crawl demo```