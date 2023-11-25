from twilio.rest import Client

account_sid = "AC663a0679384a3dba2b4d607db9e3c210"
auth_token = "058f5fb8ff57dcff17f9b6495dcbb09e"

client = Client(aacount_sid, auth_token)

message = client.api.account.message.create(
		to="+919518573652",
		from_="+12058430554",
		body="Accident Happened, Location: 17.6904° N, 75.9098° E")