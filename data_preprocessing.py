import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler
from imblearn.over_sampling import SMOTE

def load_and_preprocess_data():
    data = pd.read_csv('./fraudTrain.csv')
    std_scaler = StandardScaler()
    robust_scaler = RobustScaler()
    data.loc[:, 'V1':'V10'] = std_scaler.fit_transform(data.loc[:, 'V1':'V10'])
    data[['trans_date_trans_time', 'amt']] = robust_scaler.fit_transform(data[['trans_date_trans_time', 'amt']])
    X = data.drop('Class', axis=1)
    y = data['Class']
    smote = SMOTE(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return X_resampled, y_resampled