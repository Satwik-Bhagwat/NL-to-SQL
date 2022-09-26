import json
import torch
import os
#from matplotlib.pylab import *

def get_data(file_path: str,batch_size: int):
    '''
    Gets data from the dataset and creates a data loader
    Arguments:
    file_path: The path to the directory in which the dataset is contained
    batch_size: Batch size to be used for the data loaders
    Returns:
    train_data: Training dataset (Natural Language utterances)
    dev_data: Development dataset (Natural Language utterances) 
    train_loader: Training dataset loader
    '''
    # Loading Dev Files(Development Dataset)

    with open(file_path + '/dev.json') as dev_data_file:
        dev_data = json.load(dev_data_file)
    
    # Loading Train Files(Training Dataset)

    with open(file_path + '/train_spider.json') as train_data_file:
        train_data = json.load(train_data_file)

    with open(file_path + '/train_others.json') as train_others_data_file:
        train_data.extend(json.load(train_others_data_file))

    train_loader = torch.utils.data.DataLoader(
        batch_size=batch_size,
        dataset=train_data,
        shuffle=True,
        num_workers=4,
        collate_fn=lambda x: x  # now dictionary values are not merged!
    )

    return train_data, dev_data, train_loader

def get_fields(data):
    natural_language_utterance = []
    tokenized_natural_language_utterance = []
    sql_indexing = []
    sql_query = []
    tables = []
    columns = []
    headers = []

    for one_data in data:
        natural_language_utterance.append(one_data['question'])
        tokenized_natural_language_utterance.append(one_data['question_toks'])
        sql_indexing.append(one_data['sql'])
        sql_query.append(one_data['query'])
        with open('./tableInfo.json') as table_info:
            tableInfo = json.load(table_info)
            tables.append([tableName for tableName in (tableInfo[one_data['db_id']].keys())])
            columns.append(tableInfo[one_data['db_id']])
            headers.append(tables)
            headers.append(columns)
        
    return natural_language_utterance,tokenized_natural_language_utterance,sql_indexing,sql_query,headers


tt,td,tl = get_data('.',2)
for bi,b in enumerate(tl):
    nlu,nlut,si,sq,head = get_fields(b)
    break

