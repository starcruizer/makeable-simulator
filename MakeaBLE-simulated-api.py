#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pandas as pd

from fastapi import FastAPI

def read_sample_data(filepath):
    data = pd.read_csv(filepath + 'dataset_new.csv')
    labels = pd.read_csv(filepath + 'labels_new.csv')
    return data, labels

data, labels = read_sample_data('./Simulated/')

sample_id = 0 # index for data retrieval

app = FastAPI()


@app.get("/sim/{sample_id}")
async def getRecord(sample_id : int):
    res = data.iloc[sample_id,1:]
    return res.to_json()

@app.get("/sim_labels")
async def getLabels():
    res = labels.to_json()
    return res

@app.get("/sim_all")
async def getAllRecords():
    res = data.to_json()
    return res