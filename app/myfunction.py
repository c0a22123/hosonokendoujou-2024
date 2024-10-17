from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
import qrcode
import io
from .database import *
from .bingodatabase import *

def bingo_lists(user_id:str, event_id:str):
    bingo_list = []
    rows = loadb_db(user_id,event_id)
    for row in rows:
        for word in row:  
            bingo_list.append(word)
    return bingo_list
    
