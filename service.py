# This is the core file with our business logic

from peewee import fn
import joblib
import pandas as pd
from database import User
from utils import convert_userdata_to_df
from constants import SAMPLE_MODELINPUT


SINGLE_PERSON_DATA = {
    "CREDIT_LIMIT": 500000.0,
    "SEX": 1,
    "EDUCATION": 3,
    "MARITALSTATUS": 1,
    "AGE": 47,
    "PAYMENTDELAY_1": 0,
    "PAYMENTDELAY_2": 0,
    "PAYMENTDELAY_3": 0,
    "PAYMENTDELAY_4": 0,
    "PAYMENTDELAY_5": 0,
    "PAYMENTDELAY_6": 0,
    "BILL_AMT1": 18033.0,
    "BILL_AMT2": 8783.0,
    "BILL_AMT3": 13202.0,
    "BILL_AMT4": 16546.0,
    "BILL_AMT5": 12585.0,
    "BILL_AMT6": 14287.0,
    "PAID_AMT1": 8783.0,
    "PAID_AMT2": 13357.0,
    "PAID_AMT3": 16600.0,
    "PAID_AMT4": 12585.0,
    "PAID_AMT5": 14287.0,
    "PAID_AMT6": 25793.0,
}


def predict_one(user_data: dict) -> dict:
    """
    Predicts the loan risk for a single user.

    Args:
        user_data (dict): A dictionary containing the features of the loan application.

    Returns:
        dict: A dictionary containing the predicted class and its associated confidence.

    Example:
        {
            "PREDICTION": 1,
            "CONFIDENCE": 0.95
        }
    """
    # 1. Load the data into a dataframe
    df = pd.DataFrame([user_data])
    # 2. Load our loan classification model
    model = joblib.load("risk_radar_model")
    # 3. Return the predictions
    prediction = model.predict(df).item()
    confidence = model.predict_proba(df).max(axis=1).item()

    return {"PREDICTION": prediction, "CONFIDENCE": confidence}


def get_all_users() -> list[dict]:
    """
    Retrieve a limited set of users from the database

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing user data. Each dictionary
            has the following keys:
                - "USER_ID" (int): The unique identifier for the user.
                - "USER_NAME" (str): The username of the user.
    Example:
        [{
            "USER_ID": 22341,
            "USER_NAME": "Sandra Lewis"
        }]
    """
    results = []
    return results


def get_user_details(user_id) -> dict:
    """
    Retrieves all details for a specific user from the database.

    Args:
        user_id (int): The unique identifier of the user to retrieve details for.

    Returns:
        Dict[str, Any]: A dictionary containing the user's demograpphic and payment details..

    Example:
        {
            "USER_ID": 24,
            "USER_NAME": 24,
            "AGE": 24,
            "CREDIT_LIMIT": 20000,
            "DID_DEFAULT_PAYMENT": 1,
            "EDUCATION": 2,
            "MARITALSTATUS": 1,
            "PAYMENT_DATA": [
                {
                "BILL_AMT": 3913,
                "MONTH": 1,
                "PAID_AMT": 0,
                "PAYMENTDELAY": 2
                },
                ...
            ],
            "SEX": 2,
            "USER_ID": 1,
            "USER_NAME": "Sandra Lewis"
        }
    """
    user_dict = {}
    return user_dict


def predict(user_id: int) -> dict:
    """
    Predicts the payment default risk for a single user.

    Args:
        user_id (int): The id of the user to predict for.

    Returns:
        dict: A dictionary containing the predicted class and its associated confidence.

    Example:
        {
            "PREDICTION": 1,
            "CONFIDENCE": 0.95
        }
    """
    user_details = get_user_details(user_id)
    user_data = convert_userdata_to_df(user_details)
    prediction = predict_one(user_data)
    return prediction


if __name__ == "__main__":
    print("********")
    print("    Getting prediction for User: 22341 by passing the full data")
    print("********")

    test_data = {}
    prediction = predict_one(SINGLE_PERSON_DATA)
    print(prediction)

    exit()
    print("\n\n")

    print("********")
    print("    Getting all users")
    print("********")

    users = get_all_users()
    print(users)

    print("\n\n")

    print("********")

    user_id_to_predict = 3
    print(
        f"    Getting prediction for  User: {user_id_to_predict} by using the user_id"
    )
    print("********")

    users = predict(user_id_to_predict)
    print(users)
