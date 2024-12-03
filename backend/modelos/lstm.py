import numpy as np
import yfinance as yf
from neuralforecast import NeuralForecast
from neuralforecast.auto import AutoLSTM
from modelos.wmape import WMAPE
from core.config import Settings

# Define the ticker symbol
ticker_symbol = Settings.TICKER_SYMBOL

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
historical_data = ticker.history(period="1y")  # data for the last year

df = historical_data.reset_index(level=[0])
df = df.rename(columns={'Date': 'ds', 'Volume': 'y'})
df['unique_id'] = ticker_symbol

def wmape(y_true, y_pred):
    return np.abs(y_true - y_pred).sum() / np.abs(y_true).sum()

def get_model(dt_start_train:str, dt_end_train:str,dt_start_valid:str,dt_end_valid, num_samples:int,val_size:int):

    train = df.loc[(df['ds'] >= dt_start_train) & (df['ds'] < dt_end_train)]
    valid = df.loc[(df['ds'] >= dt_start_valid) & (df['ds'] < dt_end_valid)]
    h = valid['ds'].nunique()

    models = [AutoLSTM(h=h,
                       num_samples=num_samples, loss=WMAPE())]

    model = NeuralForecast(models=models, freq='D')

    model.fit(train, val_size=val_size)

    p = model.predict().reset_index()
    p = p.merge(valid[['ds', 'unique_id', 'y']], on=['ds', 'unique_id'], how='left')

    return p
