# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

import os
import pandas as pd
# from itemadapter import ItemAdapter


class ScrapydemoPipeline:
    def process_item(self, item, spider):
        temp = pd.DataFrame([item])
        data = pd.DataFrame([item])
        path = 'data/data.csv'
        # print(os.path.exists(path))
        if os.path.exists(path):
            data = pd.read_csv(path)
            data = data.append(temp, ignore_index=True)
        data.to_csv(path, index=False)

        return item
