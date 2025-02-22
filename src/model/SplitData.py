
class SplitData():
    def __init__(self, df):
        n = len(df)
        train_df = df[0:int(n * 0.7)]
        val_df = df[int(n * 0.7):int(n * 0.9)]
        test_df = df[int(n * 0.9):]

        self.num_features = df.shape[1]

        train_mean = train_df.mean()
        train_std = train_df.std()

        self.train_df = (train_df - train_mean) / train_std
        self.val_df = (val_df - train_mean) / train_std
        self.test_df = (test_df - train_mean) / train_std

    def __repr__(self):
        return '\n'.join([
            f"Data set sizes:",
            f'Train df size: {self.train_df.shape}',
            f'Values df size: {self.val_df.shape}',
            f'Test df size: {self.test_df.shape}'])