#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
#%%
from matplotlib import rcParams
rcParams['font.family'] = 'Angsana New'
rcParams.update({'font.size': 22})
rcParams['axes.unicode_minus'] = False
#%%
# df_read = pd.read_csv('data/corrected_data.csv')
df_read = pd.read_csv('data/chol-bangkla-corrected-2017-2022-hourly-corrected.csv', parse_dates=["datetime"])
df_read_original = pd.read_csv('data/chol-bangkla-corrected-2017-2022-hourly.csv', parse_dates=["datetime"])

#%%
df = df_read.copy()
print(df.dtypes)

#%%
# df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['datetime'])
print(df.dtypes)

#%%
df = df.sort_values(by=['datetime'])

#%%
df = df.set_index(pd.DatetimeIndex(df['date'])).drop(['date'], axis=1)

#%%

plt.figure(figsize=(16,32))
plt.subplot(3,1,1)
plt.title('Displays EC values from 2016 to 2022.')
plt.xlabel('Date')
plt.ylabel('EC')
plt.plot(df_read_original['ec'], label='Original')
plt.plot(df['ec'], label='Corrected')
plt.legend()

# plt.subplot(3,1,2)
# plt.title('Displays Temp. values from March to September.')
# plt.xlabel('Date')
# plt.ylabel('°C')
# plt.plot(df['temperature'], label='OG temp.')
# plt.plot(df['temp_new_1'], label='temp_new_1')
# plt.plot(df['temp_new_2'], label='temp_new_2')
# plt.plot(df['temp_new_3'], label='temp_new_3')
# plt.plot(df['temp_new_4'], label='temp_new_4')
# plt.plot(df['temp_new_.5'], label='temp_new_.5')
# plt.legend()

# plt.subplot(3,1,3)
# plt.title('Displays pH. values from March to September.')
# plt.xlabel('Date')
# plt.ylabel('pH')
# plt.plot(df['pH'], label='OG pH')
# plt.plot(df['pH_new_1'], label='pH_new_1')
# plt.plot(df['pH_new_2'], label='pH_new_2')
# plt.plot(df['pH_new_3'], label='pH_new_3')
# plt.plot(df['pH_new_4'], label='pH_new_4')
# plt.plot(df['pH_new_.5'], label='pH_new_.5')
# plt.legend()

#%%
# print(df["ec"].min())
# print(df["ec"].max())

#%%
# =============================================================================
# กำหนดตัวแปรที่ต้องการใช้ train ตัว model
# =============================================================================

data = df.filter(['ec'])
dataset = data.values

#%%
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

#%%
# =============================================================================
# StandardScaler
# =============================================================================

# scaler = StandardScaler()
# scaler = scaler.fit(dataset)
# dataset_scaled = scaler.transform(dataset)

# dataset_scaled = scaler.fit_transform(dataset)

#%%
# =============================================================================
# MinMaxScaler
# =============================================================================

scaler = MinMaxScaler(feature_range=(0,1))
scaler = scaler.fit(dataset)
dataset_scaled = scaler.transform(dataset)

# dataset_scaled = scaler.fit_transform(dataset)

#%%
# =============================================================================
# ไม่สเกล dataset
# =============================================================================

# dataset_scaled = dataset

#%%
n_future = 24
n_past = 48

#%%
# import math

# train_set_len = math.ceil(len(dataset) * 0.80)
# valid_set_len = math.ceil(len(dataset) * 0.10)

# first 3yrs
train_set_len = 26280

# last year
valid_set_len = 17544

#%%
# =============================================================================
# Train set
# =============================================================================

#%%
# train_set = dataset_scaled[0:train_set_len, :]
# train_set = dataset_scaled[0:train_set_len, :]


# x_train = []
# y_train = []

# for i in range(n_past, len(train_set) - n_future + 1):
#     x_train.append(train_set[i - n_past:i, 0:dataset.shape[1]])
#     y_train.append(train_set[i + n_future - 1:i + n_future, 0])

#%%
# x_train, y_train = np.array(x_train), np.array(y_train)

#%%
# =============================================================================
# Validation set
# =============================================================================

#%%
# valid_set = dataset_scaled[train_set_len - n_past:train_set_len + valid_set_len, :]

# x_valid = []
# y_valid = []

# for i in range(n_past, len(valid_set) - n_future + 1):
#     x_valid.append(valid_set[i - n_past:i, 0:dataset.shape[1]])
#     y_valid.append(valid_set[i + n_future - 1:i + n_future, 0])

#%%
# x_valid, y_valid = np.array(x_valid), np.array(y_valid)

#%%
# =============================================================================
# Test set
# =============================================================================    

#%%
# test_set = dataset_scaled[(train_set_len + valid_set_len) - n_past:, :]
# test_real = dataset[(train_set_len + valid_set_len) - n_past:, :]

# x_test = []
# y_test = []

# for i in range(n_past, len(test_set) - n_future + 1):
#     x_test.append(test_set[i - n_past:i, 0:dataset.shape[1]])
#     y_test.append(test_real[i + n_future - 1:i + n_future, 0])

#%%
# x_test, y_test = np.array(x_test), np.array(y_test)

#%%
# =============================================================================
# window slicing for multiple outputs (testing!!!)
# =============================================================================

#%%
# =============================================================================
# Train set (multiple outputs)
# =============================================================================

#%%
train_set = dataset_scaled[0:train_set_len, :]

x_train = []
y_train = []

for i in range(n_past, len(train_set) - n_future + 1):
    x_train.append(train_set[i - n_past:i, 0:dataset.shape[1]])
    y_train.append(train_set[i:i + n_future, 0])

#%%
x_train, y_train = np.array(x_train), np.array(y_train)
y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1], 1))

#%%
# =============================================================================
# Validation set (multiple outputs)
# =============================================================================

#%%
valid_set = dataset_scaled[train_set_len - n_past:train_set_len + valid_set_len, :]

x_valid = []
y_valid = []

for i in range(n_past, len(valid_set) - n_future + 1):
    x_valid.append(valid_set[i - n_past:i, 0:dataset.shape[1]])
    y_valid.append(valid_set[i:i + n_future, 0])

#%%
x_valid, y_valid = np.array(x_valid), np.array(y_valid)
y_valid = np.reshape(y_valid, (y_valid.shape[0], y_valid.shape[1], 1))

#%%
# =============================================================================
# Test set (multiple outputs)
# =============================================================================    

#%%
test_set = dataset_scaled[(train_set_len + valid_set_len) - n_past:, :]
test_real = dataset[(train_set_len + valid_set_len) - n_past:, :]

x_test = []
y_test = []

for i in range(n_past, len(test_set) - n_future + 1):
    x_test.append(test_set[i - n_past:i, 0:dataset.shape[1]])
    y_test.append(test_real[i:i + n_future, 0])

#%%
x_test, y_test = np.array(x_test), np.array(y_test)
y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1], 1))

#%%
plt.figure(figsize=(16,8))
plt.title('Displays Train set, Validation set, and Test set.')
plt.xlabel('Date')
plt.ylabel('EC')
plt.plot(df[0:train_set_len]["ec"], label='Train')
plt.plot(df[train_set_len - n_past:train_set_len + valid_set_len]["ec"], label='Validation')
plt.plot(df[(train_set_len + valid_set_len) - n_past:]["ec"], label='Test')
plt.legend()
plt.show()

#%%
# =============================================================================
# Build Model
# =============================================================================

#%%
from keras import Model
from keras.models import Sequential
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import SimpleRNN
from keras.layers import LSTM
# from keras.layers import CuDNNLSTM
from keras.layers import Bidirectional
# from tensorflow.keras.layers import Bidirectional
from keras.optimizers import Adam, SGD, RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint

#%%
# =============================================================================
# RNN
# =============================================================================

# model = Sequential()
# model.add(SimpleRNN(192, return_sequences=True, input_shape=(x_train.shape[1],x_train.shape[2])))
# # model.add(SimpleRNN(192, return_sequences=True))
# model.add(SimpleRNN(192, return_sequences=False))
# model.add(Dense(n_future))

# model.add(SimpleRNN(128, return_sequences=True, input_shape=(x_train.shape[1],x_train.shape[2])))
# model.add(SimpleRNN(64, return_sequences=True))
# model.add(SimpleRNN(64, return_sequences=False))
# model.add(Dense(16))
# model.add(Dense(1))

#%%
# =============================================================================
# LSTM
# =============================================================================

model = Sequential()
model.add(LSTM(192, return_sequences=True, input_shape=(x_train.shape[1],x_train.shape[2])))
# model.add(LSTM(192, return_sequences=True))
model.add(LSTM(192, return_sequences=False))
model.add(Dense(n_future))

# model = Sequential()
# model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1],x_train.shape[2])))
# model.add(LSTM(64, return_sequences=False))
# model.add(Dense(n_future))
# model.add(Dense(16))
# model.add(Dense(1))

#%%
# =============================================================================
# Bidirectional LSTM
# =============================================================================

# model = Sequential()
# model.add(Bidirectional(LSTM(192, return_sequences=True), input_shape=(x_train.shape[1],x_train.shape[2])))
# # model.add(Bidirectional(LSTM(96, return_sequences=True)))
# model.add(Bidirectional(LSTM(192, return_sequences=False)))
# model.add(Dense(n_future))

# model.add(Dense(16))
# model.add(Dense(1))

#%%
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])
model.summary()

#%%
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=20)

#%%
checkpoint_filepath = 'checkpoint/01-lstm-24-3-2-1-retrain.h5'
model_checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_filepath,
    monitor='val_loss',
    mode='min',
    save_best_only=True,
    save_freq='epoch',
    verbose=1
    )

#%%
model_fit = model.fit(
    x_train,
    y_train,
    batch_size=24,
    epochs=128,
    validation_data=(x_valid, y_valid),
    callbacks=[model_checkpoint_callback, early_stopping_callback]
    )

#%%
plt.figure(figsize=(16,8))
plt.title('LSTM: loss rate, 0-1 MinMaxScale, 24-output train-val-test: 3-2-1')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(model_fit.history['loss'], label='Training loss')
plt.plot(model_fit.history['val_loss'], label='Validation loss')
plt.legend()
plt.show()


# #%%
# from keras.models import load_model

# model = load_model('checkpoint/01-bilstm-24-3-2-1.h5')

# #%%
# pred = model.predict(x_test)

# #%%
# if dataset.shape[1] > 1:
#     pred = np.repeat(pred, dataset.shape[1], axis=-1)

# #%%
# y_pred = scaler.inverse_transform(pred)[:,0]

# #%%
# y_pred = np.reshape(y_pred, (y_pred.shape[0], 1))

# #%%
# from sklearn.metrics import mean_squared_error

# rmse = mean_squared_error(y_test, y_pred, squared=False)
# print(f'RMSE of Bi-LSTM = {rmse}')            

# #%%
# # rmse = np.sqrt(np.mean(np.square((y_test - y_pred))))
# # print(rmse)

# #%%
# rmspe = (np.sqrt(np.mean(np.square((y_test - y_pred) / y_test)))) * 100
# print(f'RMSPE of Bi-LSTM = {rmspe}')


# #%%
# df_compare = pd.DataFrame({'Actual EC':df['ec_corrected'][train_set_len + valid_set_len:]})
# df_compare['Predicted EC'] = y_pred

# #%%
# plt.figure(figsize=(16,8))
# plt.title('Displays Actual EC vs. Predicted EC.')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.plot(df_compare['Actual EC'], label='Actual')
# plt.plot(df_compare['Predicted EC'], label='Predicted')
# plt.legend()
# plt.show()

# #%%
# plt.figure(figsize=(16,8))
# plt.title('Displays All Actual EC vs. Predicted EC.')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.plot(df['ec_new_.5'], label='All Actual EC')
# plt.plot(df_compare['Predicted EC'], label='Predicted')
# plt.legend()
# plt.show()

#%%
# =============================================================================
# multiple outputs (testing!!!)
# =============================================================================

#%%
from keras.models import load_model

model = load_model('checkpoint/01-lstm-24-3-2-1-retrain.h5')

#%%

#%%
pred = model.predict(x_test)

#%%
rpred = None

#%%
for i in range(pred.shape[1]):
    tpred = pred[:,i]
    tpred = np.reshape(tpred, (tpred.shape[0], 1))
    tpred = np.repeat(tpred, dataset.shape[1], axis=-1)
    tpred = scaler.inverse_transform(tpred)[:,0]
    tpred = np.reshape(tpred, (tpred.shape[0], 1))
    if rpred is None:
        rpred = tpred
    else:
        rpred = np.append(rpred, tpred, axis=1)

#%%
y_pred = rpred[:,0]
y_pred = np.reshape(y_pred, (y_pred.shape[0], 1))

#%%
y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1]))

#%%
y_real = y_test[:,0]
y_real = np.reshape(y_real, (y_real.shape[0], 1))

#%%
plt.figure(figsize=(16,8))
plt.title('Bi-LSTM 0-1 scale train-val-test: 3-2-1')
plt.plot(y_real, label='y_real')
plt.plot(y_pred, label='y_pred')
plt.legend()
plt.show()

#%%
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(y_test, rpred, squared=False)
print("RMSE of LSTM =",rmse)

#%%
from sklearn.metrics import mean_absolute_percentage_error

# calculate MAPE
mape = mean_absolute_percentage_error(y_test, rpred)
print(f'MAPE of LSTM = {mape}')

#%%
df_compare = pd.DataFrame({'Actual EC':df['ec_corrected'][train_set_len + valid_set_len:-(n_future-1)]})
df_compare['Predicted EC'] = y_pred

#%%
plt.figure(figsize=(16,8))
plt.title('Displays Actual EC vs. Predicted EC.')
plt.xlabel('Date')
plt.ylabel('Value')
plt.plot(df_compare['Actual EC'], label='Actual')
plt.plot(df_compare['Predicted EC'], label='Predicted')
plt.legend()
plt.show()

#%%
plt.figure(figsize=(16,8))
plt.title('Displays All Actual EC vs. Predicted EC.')
plt.xlabel('Date')
plt.ylabel('Value')
plt.plot(df['ec_new_.5'], label='All Actual EC')
plt.plot(df_compare['Predicted EC'], label='Predicted')
plt.legend()
plt.show()



#%%
# =============================================================================
# Hyperparameter Tuning (ไม่จำเป็น)
# =============================================================================

#%%
import keras_tuner
from keras_tuner.tuners import BayesianOptimization, Hyperband

#%%
# def build_model(hp):
    
#     inputs = Input(shape=(14,5))
#     x = inputs
    
#     num_layers = hp.Int('num_rnn_layers', min_value=1, max_value=3, step=1)
#     for i in range(num_layers):
#         if i == num_layers - 1:
#             x = LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=False)(x)
#             if hp.Boolean(f'lstm_{i}_dropout'):
#                 x = Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
#         else:
#             x = LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=True)(x)
#             if hp.Boolean(f'lstm_{i}_dropout'):
#                 x = Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
    
#     if hp.Boolean('dense_bef_out'):
#         x = Dense(units=hp.Int('dense_bef_out_units', min_value=8, max_value=32, step=4))(x)
#         if hp.Boolean('dense_bef_out_dropout'):
#             x = Dropout(rate=hp.Float('dense_bef_out_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
            
#     outputs = Dense(units=1)(x)
    
#     model = Model(inputs, outputs)
    
#     hp_optimizer = hp.Choice("optimizer",values = ["adam","RMSprop","SGD"])
#     hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
    
#     optimizer = None
#     if hp_optimizer == "adam":
#         optimizer = Adam(learning_rate = hp_learning_rate)
#     elif hp_optimizer == "RMSprop":
#         optimizer = RMSprop(learning_rate = hp_learning_rate)
#     elif hp_optimizer == "SGD":
#         optimizer = SGD(learning_rate = hp_learning_rate)
    
#     model.compile(optimizer=optimizer,loss='mse',metrics = ['mse'])
    
#     return model

#%%
class MyHyperModel(keras_tuner.HyperModel):
    def build(self, hp):
        
        model = Sequential()        
        # model.add(Input(shape=(14,5)))
        
        num_layers = hp.Int('num_rnn_layers', min_value=1, max_value=3, step=1)
        for i in range(num_layers):
            if i == num_layers - 1:
                model.add(LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=False))
                if hp.Boolean(f'lstm_{i}_dropout'):
                    model.add(Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1)))
            else:
                model.add(LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=True))
                if hp.Boolean(f'lstm_{i}_dropout'):
                    model.add(Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1)))
               
        if hp.Boolean('dense_bef_out'):
            model.add(Dense(units=hp.Int('dense_bef_out_units', min_value=8, max_value=32, step=4)))
            if hp.Boolean('dense_bef_out_dropout'):
                model.add(Dropout(rate=hp.Float('dense_bef_out_dropout_rate', min_value=0.1, max_value=0.5, step=0.1)))
        
        model.add(Dense(units=1))
        
        # hp_optimizer = hp.Choice("optimizer",values = ["adam","RMSprop","SGD"])
        # hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
        
        # optimizer = None
        # if hp_optimizer == "adam":
        #     optimizer = Adam(learning_rate = hp_learning_rate)
        # elif hp_optimizer == "RMSprop":
        #     optimizer = RMSprop(learning_rate = hp_learning_rate)
        # elif hp_optimizer == "SGD":
        #     optimizer = SGD(learning_rate = hp_learning_rate)
        
        model.compile(optimizer='adam',loss='mse',metrics = ['mse'])
        
        return model

    def fit(self, hp, model, *args, **kwargs):
        return model.fit(
            *args,
            batch_size=hp.Choice('batch_size', values=[4,8,16,32,64,128]),
            **kwargs,
        )
    
#%%
# class MyHyperModel(keras_tuner.HyperModel):
#     def build(self, hp):
        
#         inputs = Input(shape=(14,5))
#         x = inputs
        
#         num_layers = hp.Int('num_rnn_layers', min_value=1, max_value=3, step=1)
#         for i in range(num_layers):
#             if i == num_layers - 1:
#                 x = LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=False)(x)
#                 if hp.Boolean(f'lstm_{i}_dropout'):
#                     x = Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
#             else:
#                 x = LSTM(units=hp.Int(f'lstm_{i}_units', min_value=32, max_value=128, step=16), return_sequences=True)(x)
#                 if hp.Boolean(f'lstm_{i}_dropout'):
#                     x = Dropout(rate=hp.Float(f'lstm_{i}_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
        
#         if hp.Boolean('dense_bef_out'):
#             x = Dense(units=hp.Int('dense_bef_out_units', min_value=8, max_value=32, step=4))(x)
#             if hp.Boolean('dense_bef_out_dropout'):
#                 x = Dropout(rate=hp.Float('dense_bef_out_dropout_rate', min_value=0.1, max_value=0.5, step=0.1))(x)
                
#         outputs = Dense(units=1)(x)
        
#         model = Model(inputs, outputs)
        
#         hp_optimizer = hp.Choice("optimizer",values = ["adam","RMSprop","SGD"])
#         hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
        
#         optimizer = None
#         if hp_optimizer == "adam":
#             optimizer = Adam(learning_rate = hp_learning_rate)
#         elif hp_optimizer == "RMSprop":
#             optimizer = RMSprop(learning_rate = hp_learning_rate)
#         elif hp_optimizer == "SGD":
#             optimizer = SGD(learning_rate = hp_learning_rate)
        
#         model.compile(optimizer=optimizer,loss='mse',metrics = ['mse'])
        
#         return model

#     def fit(self, hp, model, *args, **kwargs):
#         return model.fit(
#             *args,
#             batch_size=hp.Choice('batch_size', values=[32,64,128]),
#             **kwargs,
#         )

#%%
# =============================================================================
# BayesianOptimization (not used)
# =============================================================================

#%%
tuner = BayesianOptimization(
    # build_model,
    MyHyperModel(),
    objective="val_loss",
    max_trials=50,
    overwrite=True,
    directory="bayes_dir",
    project_name="bayes_hypermodel",
)

#%%
tuner.search_space_summary()

#%%
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

#%%
tuner.search(
    x_train,
    y_train,
    # batch_size=64,
    epochs=128,
    validation_data=(x_valid, y_valid),
    callbacks=[early_stopping_callback]
    )

#%%
models = tuner.get_best_models(num_models=2)
best_model = models[0]
best_model.build(input_shape=(None,x_train.shape[1], x_train.shape[2]))
best_model.summary()

#%%
# =============================================================================
# Hyperband (not used)
# =============================================================================

#%%
tuner = Hyperband(
    # build_model,
    MyHyperModel(),
    objective="val_loss",    
    max_epochs=64,    
    overwrite=True,
    directory="hyband_dir",
    project_name="hyband_hypermodel",
)

#%%
tuner.search_space_summary()

#%%
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

#%%
tuner.search(
    x_train,
    y_train,
    # batch_size=64,
    validation_data=(x_valid, y_valid),
    callbacks=[early_stopping_callback]
    )

#%%
models = tuner.get_best_models(num_models=2)
best_model = models[0]
best_model.build(input_shape=(None,x_train.shape[1], x_train.shape[2]))
best_model.summary()


