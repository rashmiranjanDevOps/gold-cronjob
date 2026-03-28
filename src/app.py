import requests
import boto3
import os

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
AWS_REGION = os.getenv("AWS_REGION")

def get_gold_price():
    url = "https://www.goldapi.io/api/XAU/INR"

    headers = {
        "x-access-token": os.getenv("API_KEY"),   # 🔐 from secret
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        print("FULL API RESPONSE:", data)

        if "error" in data:
            print("API failed, using fallback")
            return 6000

        price = data.get("price") or data.get("price_gram_24k")
        return price if price else 6000

    except Exception as e:
        print("Error:", e)
        return 6000


def send_to_sns(price):
    try:
        client = boto3.client("sns", region_name=AWS_REGION)

        message = f"Gold Price Today: {price} INR"

        response = client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Gold Price Alert"
        )

        print("SNS Sent:", response)

    except Exception as e:
        print("SNS Error:", e)


if __name__ == "__main__":
    price = get_gold_price()
    print("Fetched Price:", price)
    send_to_sns(price)