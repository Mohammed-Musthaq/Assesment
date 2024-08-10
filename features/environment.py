from behave import fixture
from Helper import login_successfully

# def before_feature(context, feature):
#     print("Runs Before Each Feature")
def before_scenario(context, scenario):
    if "3 Order a product" in scenario.name:
        login_successfully(context)
