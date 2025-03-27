from domino.data_sources import DataSourceClient

# instantiate a client and fetch the datasource instance
ds = DataSourceClient().get_datasource("anna")

# res is a simple wrapper of the query result
res = ds.query("select * from {{table_reference}}")

# to_pandas() loads the result into a pandas dataframe
df = res.to_pandas()
