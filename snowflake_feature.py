from datetime import timedelta

import pandas as pd
import yaml

#anna

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    PushSource,
    RequestSource,
    SnowflakeSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64
#test
# Define an entity for the driver. You can think of an entity as a primary key used to
# fetch features.
driver = Entity(name="driver", join_keys=["DRIVER_ID"])

# Defines a data source from which feature values can be retrieved. Sources are queried when building training
# datasets or materializing features into an online store.
project_name = yaml.safe_load(open("feature_store.yaml"))["project"]

driver_stats_source = SnowflakeSource(
    # The Snowflake table where features can be found
    database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
    table="DRIVER_STATS",
    # The event timestamp is used for point-in-time joins and for ensuring only
    # features within the TTL are returned
    timestamp_field="EVENT_TIMESTAMP",
    # The (optional) created timestamp is used to ensure there are no duplicate
    # feature rows in the offline store or when building training datasets
    created_timestamp_column="CREATED",
)

# Feature views are a grouping based on how features are stored in either the
# online or offline store.
driver_stats_fv = FeatureView(
    # The unique name of this feature view. Two feature views in a single
    # project cannot have the same name
    name="driver_hourly_stats_new_super",
    description="FEATURE TEST DESCRIPTION",
    # The list of entities specifies the keys required for joining or looking
    # up features from this feature view. The reference provided in this field
    # correspond to the name of a defined entity (or entities)
    entities=[driver],
    # The timedelta is the maximum age that each feature value may have
    # relative to its lookup time. For historical features (used in training),
    # TTL is relative to each timestamp provided in the entity dataframe.
    # TTL also allows for eviction of keys from online stores and limits the
    # amount of historical scanning required for historical feature values
    # during retrieval
    ttl=timedelta(weeks=52 * 10),  # Set to be very long for example purposes only
    # The list of features defined below act as a schema to both define features
    # for both materialization of features into a store, and are used as references
    # during retrieval for building a training dataset or serving features
    schema=[
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna*", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna?", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna*", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna?", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna*", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="anna?", dtype=Float32,tags={"team": "TEST@"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA@"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA@"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA*"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA["}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA$"}),
        Field(name="CONV_RATE", dtype=Float32,tags={"team": "ANNA_anna"}),
        Field(name="ACC_RAT1E", dtype=Float32),
        Field(name="ACC_RATE2", dtype=Float32),
        Field(name="ACC_RATE4", dtype=Float32),
        Field(name="ACC_RATE3111", dtype=Float32),
        Field(name="ACC_RATE33", dtype=Float32),
        Field(name="ACC_RATE5", dtype=Float32),
        Field(name="ACC_RATE6", dtype=Float32),
        Field(name="ACC_RATE66", dtype=Float32),
        Field(name="ACC_RATE7", dtype=Float32),
        Field(name="ACC_RATE8", dtype=Float32),
        Field(name="ACC_RATE9", dtype=Float32),
        Field(name="rateACC_RATE", dtype=Float32),
        Field(name="ACC_RATE11", dtype=Float32),
        Field(name="ACC_RATE22", dtype=Float32),
        Field(name="ACC_RATE", dtype=Float32),
        Field(name="ACC_RATE", dtype=Float32),
        Field(name="ACC_RATE", dtype=Float32),
        Field(name="ACC_RATE", dtype=Float32),
        Field(name="AVG_DAILY_TRIPS1", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS2", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS3", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS4", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS5", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS6", dtype=Int64,tags={"team": "eng"}),
        Field(name="7AVG_DAILY_TRIPS", dtype=Int64,tags={"team": "eng"}),
        Field(name="8AVG_DAILY_TRIPS", dtype=Int64,tags={"team": "eng"}),
        Field(name="1AVG_DAILY_TRIPS", dtype=Int64,tags={"team": "eng"}),
        Field(name="2AVG_DAILY_TRIPS", dtype=Int64,tags={"team": "eng"}),
        Field(name="3AVG_DAILY_TRIPS", dtype=Int64,tags={"team": "eng"}),
        Field(name="test", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS99", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS88", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS888", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS7777", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS77", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS77", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS77", dtype=Int64,tags={"team": "eng"}),
        Field(name="AVG_DAILY_TRIPS77", dtype=Int64,tags={"team": "eng"}),
    ],
    source=driver_stats_source,
    # Tags are user defined key/value pairs that are attached to each
    # feature view
    tags={"team": "TEST"},
    
)

# Define a request data source which encodes features / information only
# available at request time (e.g. part of the user initiated HTTP request)
input_request = RequestSource(
    name="vals_to_add",
    schema=[
        Field(name="val_to_add", dtype=Int64),
        Field(name="val_to_add_2", dtype=Int64),
    ],
)


# Define an on demand feature view which can generate new features based on
# existing feature views and RequestSource features
@on_demand_feature_view(
    sources=[driver_stats_fv, input_request],
    schema=[
        Field(name="conv_rate_plus_val1", dtype=Float64),
        Field(name="conv_rate_plus_val2", dtype=Float64),
    ],
)
def transformed_conv_rate(inputs: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["conv_rate_plus_val1"] = inputs["CONV_RATE"] + inputs["val_to_add"]
    df["conv_rate_plus_val2"] = inputs["CONV_RATE"] + inputs["val_to_add_2"]
    return df


# This groups features into a model version
driver_activity_v1 = FeatureService(
    name="driver_activity_v1",
    features=[
        driver_stats_fv[["CONV_RATE"]],  # Sub-selects a feature from a feature view
        transformed_conv_rate,  # Selects all features from the feature view
    ],
)
driver_activity_v2 = FeatureService(
    name="driver_activity_v2", features=[driver_stats_fv, transformed_conv_rate]
)

# Defines a way to push data (to be available offline, online or both) into Feast.
driver_stats_push_source = PushSource(
    name="driver_stats_push_source",
    batch_source=driver_stats_source,
)

# Defines a slightly modified version of the feature view from above, where the source
# has been changed to the push source. This allows fresh features to be directly pushed
# to the online store for this feature view.
driver_stats_fresh_fv = FeatureView(
    name="driver_hourly_stats_fresh",
    entities=[driver],
    ttl=timedelta(weeks=52 * 10),  # Set to be very long for example purposes only
    schema=[
        Field(name="CONV_RATE", dtype=Float32),
        Field(name="ACC_RATE", dtype=Float32),
        Field(name="AVG_DAILY_TRIPS", dtype=Int64),
    ],
    online=True,
    source=driver_stats_push_source,  # Changed from above
    tags={"team": "driver_performance"},
)


# Define an on demand feature view which can generate new features based on
# existing feature views and RequestSource features
@on_demand_feature_view(
    sources=[driver_stats_fresh_fv, input_request],  # relies on fresh version of FV
    schema=[
        Field(name="conv_rate_plus_val1", dtype=Float64),
        Field(name="conv_rate_plus_val2", dtype=Float64),
    ],
)
def transformed_conv_rate_fresh(inputs: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["conv_rate_plus_val1"] = inputs["CONV_RATE"] + inputs["val_to_add"]
    df["conv_rate_plus_val2"] = inputs["CONV_RATE"] + inputs["val_to_add_2"]
    return df


driver_activity_v3 = FeatureService(
    name="driver_activity_v3",
    features=[driver_stats_fresh_fv, transformed_conv_rate_fresh],
)
