import streamlit as st
import pandas as pd
from objects.app import App
import threading


def app():
    start_app = App()
    threading.Thread(target = start_app.executeApp()).start()
    
if __name__ == "__main__":
    app()