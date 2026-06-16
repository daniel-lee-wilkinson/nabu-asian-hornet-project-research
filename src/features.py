
class DataCleaner:
    def __init__(self, df, core_cols=None):
        self.df = df.copy()
        self.core_cols = core_cols

    def select_core_cols(self):
        """Filter to core columns if specified."""
        if self.core_cols is not None:
            self.df = self.df[self.core_cols]
        return self

    def clean_column_names(self):
        """Snake_case, remove spaces, and convert to lowercase."""
        self.df.columns = self.df.columns.str.lower().str.replace(" ", "_")
        return self

    def cast_small_string_variables(self):
        """Cast string columns with less than 5 unique values to category."""
        for col in self.df.select_dtypes(include=['object']).columns:
            if self.df[col].nunique() < 5:
                self.df[col] = self.df[col].astype('category')
        return self

    def drop_null_columns(self):
        """Drop any columns that are 100% null."""
        self.df = self.df.dropna(axis=1, how='all')
        return self

    def drop_single_value_columns(self):
        """Drop any columns with only one unique value."""
        self.df = self.df.loc[:, self.df.nunique() > 1]
        return self

    def remove_special_characters(self):
        """Remove special characters from string columns."""
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].str.replace(r'[^\w\s]', '', regex=True)
        return self

    def get(self):
        return self.df