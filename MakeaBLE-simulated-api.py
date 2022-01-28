#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def read_sample_data(filepath):
    data = pd.read_csv(filepath + 'dataset_new.csv')
    labels = pd.read_csv(filepath + 'labels_new.csv')
    return data, labels

data, labels = read_sample_data('./Simulated/')

flag = True

sample_id = 0 # index for data retrieval

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sim/{sample_id}")
async def getRecord(sample_id : int):
    global flag
    res = data.iloc[sample_id,1:]
    if flag == True:
        return res.to_json()
    else:
        return "Device Not Found!"

@app.get("/sim_labels")
async def getLabels():
    res = labels.to_json()
    return res

@app.get("/sim_all")
async def getAllRecords():
    res = data.to_json()
    global flag
    if flag == True:
        return res
    else:
        return "Device Not Found!"

@app.get("/switch")
async def turnOnOff():
    res = "The device is "
    global flag
    if flag == True:
        flag = False
        res = res + "successfully turned off!"
    else:
        flag = True
        res = res + "successfully turned on!"
    return res

@app.get("/status")
async def getStatus():
    global flag
    if flag == True:
        return 1
    else:
        return 0